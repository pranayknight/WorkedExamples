from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Firefox(executable_path="/home/pranay/Drivers/geckodriver-v0.24.0-linux64/geckodriver")
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")

button = driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")
actions = ActionChains(driver)
actions.context_click(button).perform()
