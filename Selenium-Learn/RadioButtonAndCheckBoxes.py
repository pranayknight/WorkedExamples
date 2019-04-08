from selenium import webdriver

driver = webdriver.Firefox(executable_path="/home/pranay/Drivers/geckodriver-v0.24.0-linux64/geckodriver")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# Working with the radio buttons

status = driver.find_element_by_id("RESULT_RadioButton-8_0").is_selected()
print(status)

driver.find_element_by_id("RESULT_RadioButton-8_0").click()

status = driver.find_element_by_id("RESULT_RadioButton-8_0").is_selected()
print(status)

# Working with Check boxes

driver.find_element_by_id("RESULT_CheckBox-9_0").click()
driver.find_element_by_id("RESULT_CheckBox-9_6").click()

print(driver.find_element_by_id("RESULT_CheckBox-9_0").is_selected())
print(driver.find_element_by_id("RESULT_CheckBox-9_6").is_selected())
