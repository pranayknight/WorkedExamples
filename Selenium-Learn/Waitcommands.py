from selenium import webdriver

driver = webdriver.Firefox(executable_path="/home/pranay/Drivers/geckodriver-v0.24.0-linux64/geckodriver")

driver.get("http://newtours.demoaut.com/")    # Opening URL takes some time

driver.implicitly_wait(10)   # After opening the page the element will wait for the time specified
# implicit wait statement is applicable for all the elements of the page
# Also we need to use this only once and will be applicable for all the codes

assert "Welcome: Mercury Tours" in driver.title
driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")
driver.find_element_by_name("login").click()
