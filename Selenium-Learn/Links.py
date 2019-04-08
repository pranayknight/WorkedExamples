from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path="/home/pranay/Drivers/geckodriver-v0.24.0-linux64/geckodriver")
driver.get("http://newtours.demoaut.com/")

# Printing the no. of links present in the page
links = driver.find_elements(By.TAG_NAME, "a")

print("No. of links ", len(links))   # Print how many links present in a page

# Printing the content of the links
for link in links:
    print(link.text)

# Clicking on the link
# driver.find_element(By.LINK_TEXT, "REGISTER").click()

driver.find_element(By.PARTIAL_LINK_TEXT, "REG").click()
