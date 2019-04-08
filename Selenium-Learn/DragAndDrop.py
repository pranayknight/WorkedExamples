from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Firefox(executable_path="/home/pranay/Drivers/geckodriver-v0.24.0-linux64/geckodriver")
driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

source_element = driver.find_element_by_id("box6")
target_element = driver.find_element_by_id("box106")
actions = ActionChains(driver)

actions.drag_and_drop(source_element, target_element).perform()
