from selenium import webdriver

driver = webdriver.Firefox(executable_path="/home/pranay/Drivers/geckodriver-v0.24.0-linux64/geckodriver")
driver.get("http://newtours.demoaut.com/mercurywelcome.php")

driver.save_screenshot("Homepage1.png")
driver.get_screenshot_as_file("Homepage2.jpg")
