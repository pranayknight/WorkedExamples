from selenium import webdriver
import sqlite3
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True


driver = webdriver.Firefox(options=options)
driver.get("https://cvv-me.su")

keyval = "OF3S67Zw3TMGyB2riXlN47l/GtmG9AuU32yun4KE1Qoa5yOpNkjhDeAQ7Rh4lXO4HoEnLDfSMWW7vGkqnCSHKIJz82voKhBGncstXlzNIrTilURIXfjhC0HR3ftwj+Ks6V95UsrlzfLGoIA7W774JA=="
driver.implicitly_wait(10)
driver.find_element_by_xpath("//textarea[@class='login-key form-control']").send_keys(keyval)
driver.find_element_by_xpath("//button[text()='Log in']").click()
element1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()=' CVV']")))
driver.find_element_by_xpath("//span[text()=' CVV']").click()

txt = []
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//th[@class='reactable-header-sortable ']")))
johnsnow = driver.find_elements_by_xpath("//th[@class='reactable-header-sortable ']")
for rip in johnsnow:
    txt.append(rip.text)
print(txt)



conn = sqlite3.connect('example.db')
c = conn.cursor()
# CREATE TABLE
c.execute("CREATE TABLE BALDILOCKS({} text, {} text, {} text, {} text, {} text, {} text, {} text, {} text, {} text, {} text, {} text)", txt)
'''
for i in range (0, len(driver.find_elements_by_xpath("//td[@label='?']", txt[1]))):
    for j in range (0, len(driver.find_elements_by_xpath("//th[@class='reactable-header-sortable ']"))):
        data = driver.find_elements_by_xpath("//tbody[@class='reactable-data'][j]//td[i]")
        tdata = data.append()
conn.close()
'''

driver.quit()