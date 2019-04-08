from selenium import webdriver
import sqlite3
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import ActionChains
import time

options = Options()
options.headless = True  # Comment this to see it perform in browser


driver = webdriver.Firefox(options=options)
driver.get("https://cvv-me.su")
driver.maximize_window()

keyval = "OF3S67Zw3TMGyB2riXlN47l/GtmG9AuU32yun4KE1Qoa5yOpNkjhDeAQ7Rh4lXO4HoEnLDfSMWW7vGkqnCSHKIJz82voKhBGncstXlzNIrTilURIXfjhC0HR3ftwj+Ks6V95UsrlzfLGoIA7W774JA=="
driver.implicitly_wait(10)
driver.find_element_by_xpath("//textarea[@class='login-key form-control']").send_keys(keyval)
driver.find_element_by_xpath("//button[text()='Log in']").click()
element1 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//span[text()=' CVV']")))
driver.find_element_by_xpath("//span[text()=' CVV']").click()

# driver.execute_script("document.body.style.zoom='30%'")   works in chrome so better than scrolling

all_headers = []
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//th[@class='reactable-header-sortable ']")))
headers = driver.find_elements_by_xpath("//th[@class='reactable-header-sortable ']")
for header in headers:
    all_headers.append(header.text)
print(all_headers)

row_data = []
table_data = []
new_data = str()
old_data = str()


def replace_incomplete(row_data, old_data):
    replacement = driver.find_element_by_xpath("//option[contains(text(),'{}')]".format(old_data[11:18]))
    row_data.insert(9, replacement.text)
    return row_data


for i in range(1, len(driver.find_elements_by_xpath("//td[@label='Bin']"))+1):
    row_data = []
    time.sleep(1)
    for data in driver.find_elements_by_xpath("//tbody[@class='reactable-data']//tr[{0}]//td".format(str(i))):
        row_data.append(data.text)
    del(row_data[11])
    if (row_data[8] != 'N/A'):
        bank = driver.find_element_by_xpath("//tbody[@class='reactable-data']//tr["+str(i)+"]//td[9]//span[@class='cursor-pointer']")
        if i==15 or i==30:
            driver.execute_script("arguments[0].scrollIntoView();", bank)
            time.sleep(5)
        action = ActionChains(driver)
        action.move_to_element(bank).perform()
        time.sleep(1)
        hoverow_data = driver.find_element_by_xpath("//div[@class='tooltip-inner']").text
        del(row_data[8])
        row_data.insert(8, hoverow_data)
    if (row_data[9][-1:3]=="..."):
        old_data = row_data[9]
        del(row_data[9])
        row_data = replace_incomplete(row_data, old_data)
    table_data.append(row_data)


connection = sqlite3.connect('example.db')
cursor = connection.cursor()
# CREATE TABLE
cursor.execute('''CREATE TABLE IF NOT EXISTS CVVinfo(
Bin TEXT, Exp TEXT, Name TEXT, City TEXT, State TEXT, ZIP TEXT, Country TEXT, Price$ TEXT, Bank TEXT, Base TEXT, Valid_rate TEXT)''')
cursor.executemany("INSERT INTO CVVinfo VALUES(?,?,?,?,?,?,?,?,?,?,?)",table_data)
connection.commit()
cursor.close()
connection.close()

driver.quit()
