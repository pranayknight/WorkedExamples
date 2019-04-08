from selenium import webdriver

# driver = webdriver.Chrome(executable_path="/home/pranay/Drivers/chromedriver_linux64/chromedriver")

driver = webdriver.Firefox(executable_path="/home/pranay/Drivers/geckodriver-v0.24.0-linux64/geckodriver")
driver.get("http://newtours.demoaut.com/")
print(driver.title)
print(driver.current_url)
# print(driver.page_source)
driver.implicitly_wait(5)
driver.close()
