import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(executable_path="/home/pranay/Drivers/geckodriver-v0.24.0-linux64/geckodriver")

driver.implicitly_wait(5)

driver.maximize_window()   #this cmd maximizes the page
driver.get("https://www.expedia.com/")

# driver.find_element_by_id("tab-flight-tab-hp").click()   # We know this method already

driver.find_element(By.ID, "tab-flight-tab-hp").click()   # New approach  // will click on flights button


driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")   # Origin
time.sleep(2)   # From python  //This halts thew program for the specified time

driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")   # Destination

driver.find_element(By.ID, "flight-departing-hp-flight").clear()
driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("04/11/2019")

driver.find_element(By.ID, "flight-returning-hp-flight").clear()
driver.find_element(By.ID, "flight-returning-hp-flight").send_keys("10/11/2019")

driver.find_element(By.XPATH, "//*[@id='gcw-flights-form-hp-flight']/div[7]/label/button").click()  # Search

# Explicit wait statements
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, "stopFilter_stops-0")))


element.click()
time.sleep(3)
driver.quit()
