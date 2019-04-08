from selenium import webdriver

driver = webdriver.Firefox(executable_path="/home/pranay/Drivers/geckodriver-v0.24.0-linux64/geckodriver")
driver.get("https://testautomationpractice.blogspot.com")

driver.switch_to_frame(0)
driver.find_element_by_id("RESULT_FileUpload-11").send_keys("/home/pranay/others/starburn.txt")
