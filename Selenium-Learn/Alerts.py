from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="/home/pranay/Drivers/geckodriver-v0.24.0-linux64/geckodriver")
driver.get("https://testautomationpractice.blogspot.com/")
alert = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[2]/div/aside/div/div[2]/div[1]/button")
alert.click()
time.sleep(5)
driver.switch_to_alert().accept()   # Closes the alert window using the ok button
alert.click()
time.sleep(5)
driver.switch_to_alert().dismiss()   # Closes the alert window using the cancel button