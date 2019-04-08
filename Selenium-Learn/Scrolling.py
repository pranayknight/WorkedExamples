from selenium import webdriver
import time


driver = webdriver.Firefox(executable_path="/home/pranay/Drivers/geckodriver-v0.24.0-linux64/geckodriver")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

driver.maximize_window()

# 1. Scroll down by pixel number
driver.execute_script("window.scrollBy(0, 1000)", "")
time.sleep(3)

# 2. Scroll down the page till we find the element
flag = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/table[1]/tbody/tr[86]/td[2]")
driver.execute_script("arguments[0].scrollIntoView();", flag)
time.sleep(3)

# 3. Scroll down the page till end
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")