from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox(executable_path="/home/pranay/Drivers/geckodriver-v0.24.0-linux64/geckodriver")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

drp = Select(driver.find_element_by_id("RESULT_RadioButton-7"))

# There are various methods to select the elememt from the drop down list

# 1. Select by visible text
# drp.select_by_visible_text("Morning")  # Morning

# 2. Select by index
# drp.select_by_index(2)  # Afternoon

# 3. Select by value
drp.select_by_value("Radio-2")  # Evening

# Count number of options
all_options = drp.options         # This will return all the options present in the drop down box
print(len(all_options))

# Capture all the options and print them as output
for option in all_options:
    print(option.text)

