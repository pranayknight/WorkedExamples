from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path="/home/pranay/Drivers/geckodriver-v0.24.0-linux64/geckodriver")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# How to find the no. of input boxes present in the web page

inputboxes = driver.find_elements(By.CLASS_NAME,'text_field')
print(len(inputboxes))  # provides the no. of text boxes present

# How to get the status of the text boxes
status = driver.find_element(By.ID, 'RESULT_TextField-1').is_displayed()
print("Displayed or not: ", status)

status = driver.find_element(By.ID, 'RESULT_TextField-1').is_enabled()
print("Enabled or not: ", status)

# How to provide value into the text boxes

driver.find_element(By.ID, 'RESULT_TextField-1').send_keys('pavan')
driver.find_element(By.ID, 'RESULT_TextField-2').send_keys('kumar')

driver.find_element_by_id('RESULT_TextField-3').send_keys('3333333333')
