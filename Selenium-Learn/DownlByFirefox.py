from selenium import webdriver

fp = webdriver.FirefoxProfile()
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain,application/pdf")
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", "/home/pranay/Documents")
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("pdfjs.disabled", True)

driver = webdriver.Firefox(executable_path="/home/pranay/Drivers/geckodriver-v0.24.0-linux64/geckodriver",
                           firefox_profile=fp)
driver.get("http://demo.automationtesting.in/FileDownload.html")


# Download text file
driver.find_element_by_id("textbox").send_keys("Testing Download Text File")
driver.find_element_by_id("createTxt").click()
driver.find_element_by_id("link-to-download").click()

# Download pdf file
driver.find_element_by_id("pdfbox").send_keys("Testing pdf")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()