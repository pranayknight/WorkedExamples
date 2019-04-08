from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Firefox(executable_path="/home/pranay/Drivers/geckodriver-v0.24.0-linux64/geckodriver")
driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

element = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[1]/div[1]/button")
actions = ActionChains(driver)
actions.double_click(element).perform()  #this action will perform double click on the element
