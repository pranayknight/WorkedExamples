import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Firefox(executable_path="/home/pranay/Drivers/geckodriver-v0.24.0-linux64/geckodriver")
driver.get("https://opensource-demo.orangehrmlive.com")

driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

admin = driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b")
usermgmt = driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
user = driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")

actions = ActionChains(driver)
place = actions.move_to_element(admin).move_to_element(usermgmt).move_to_element(user)
time.sleep(3)
place.click().perform()
