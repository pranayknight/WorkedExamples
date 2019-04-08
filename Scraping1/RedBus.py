from selenium import webdriver
import time

month = input("Enter the month of booking in the format as 'March' or 'April': ")
date = int(input("Enter the exact date of journey: "))

driver = webdriver.Firefox(executable_path="/home/pranay/Drivers/geckodriver-v0.24.0-linux64/geckodriver")
driver.get("https://www.redbus.in/")

driver.find_element_by_xpath("//input[@id='src']").send_keys("Bangalore (All Locations)")
time.sleep(3)
driver.find_element_by_xpath("//input[@id='dest']").send_keys("Goa (All Locations)")
time.sleep(3)

driver.find_element_by_xpath("//label[text()='Onward Date']").click()

if month=='March':
    driver.find_element_by_xpath("//div[@id='rb-calendar_onward_cal']//td[text()='"+str(date)+"']").click()

elif month=='April':
    driver.find_element_by_xpath("//div[@id='rb-calendar_onward_cal']//button[text()='>']").click()
    driver.find_element_by_xpath("//div[@id='rb-calendar_onward_cal']//td[text()='" + str(date) + "']").click()

driver.find_element_by_xpath("//label[text()='Return Date']").click()
time.sleep(5)