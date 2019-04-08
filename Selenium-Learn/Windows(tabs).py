from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(executable_path="/home/pranay/Drivers/geckodriver-v0.24.0-linux64/geckodriver")
driver.get("http://demo.automationtesting.in/Windows.html")


driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

print(driver.current_window_handle)   # Prints the window handle of the parent window

handles = driver.window_handles   # Will store all the handle values of the opened browser windows

for handle in handles:
    driver.switch_to.window(handle)
    time.sleep(3)
    print(driver.title)
    if driver.title == "Frames & windows":
        driver.close()

time.sleep(3)
driver.quit()
print(handles)
