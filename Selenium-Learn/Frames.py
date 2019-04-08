from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(executable_path="/home/pranay/Drivers/geckodriver-v0.24.0-linux64/geckodriver")

driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")

# Accessing the first frame
driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(3)

# After going to the frame we need to switch to the default page(Overall structure page) to access another frame
driver.switch_to.default_content()

# Now we need access to the second frame
driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("WebDriver").click()
time.sleep(3)

# Again we need to get to the main content to get access to the third frame
driver.switch_to.default_content()

# Now acessing the third frame
driver.switch_to_frame("classFrame")
driver.find_element(By.XPATH, "/html/body/div[1]/ul/li[5]/a").click()