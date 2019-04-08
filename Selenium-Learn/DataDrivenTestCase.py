from XLUtils import getRowCount,readData, writeData
from selenium import webdriver

driver = webdriver.Firefox(executable_path="/home/pranay/Drivers/geckodriver-v0.24.0-linux64/geckodriver")
driver.get("http://newtours.demoaut.com/")
path = "/home/pranay/Documents/Login1.xlsx"

rows = getRowCount(path, "Sheet1")

for r in range(2,rows+1):
    userName = readData(path, "Sheet1", r, 1)
    password = readData(path, "Sheet1", r, 2)

    driver.find_element_by_name("userName").send_keys(userName)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("login").click()

    if driver.title == "Find a Flight: Mercury Tours:":
        print("Test is passed")
        writeData(path, "Sheet1", r, 3, "Test Passed")
    else:
        print("Test Failed")
        writeData(path, "Sheet1", r, 3, "Test Failed")

    driver.find_element_by_link_text("Home").click()