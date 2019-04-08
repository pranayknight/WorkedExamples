from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="/home/pranay/Drivers/geckodriver-v0.24.0-linux64/geckodriver")

driver.get("http://newtours.demoaut.com/")  # Flight reservation Application
print(driver.title)
time.sleep(5)

driver.get("http://pavantestingtools.blogspot.in/")   # Testing Tools Page
print(driver.title)
time.sleep(5)

driver.back()
print(driver.title)
time.sleep(5)

driver.forward()
print(driver.title)
time.sleep(5)
