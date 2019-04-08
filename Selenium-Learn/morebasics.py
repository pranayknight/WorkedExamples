import time

from selenium import webdriver

driver = webdriver.Firefox(executable_path="/home/pranay/Drivers/geckodriver-v0.24.0-linux64/geckodriver")
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)
print(driver.current_url)
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
time.sleep(5)
driver.close()   # Closes only the tab that is mentioned
driver.quit()    # Quits the browser entirely