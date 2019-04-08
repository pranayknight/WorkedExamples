from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromeoptions = Options()
chromeoptions.add_experimental_option("prefs", {"download.default_directory": "/home/pranay/Documents"})


driver = webdriver.Chrome(executable_path="/home/pranay/Drivers/chromedriver_linux64/chromedriver", chrome_options=chromeoptions)

driver.get("http://demo.automationtesting.in/FileDownload.html")

# Download text file
driver.find_element_by_id("textbox").send_keys("Testing Download Text File")
driver.find_element_by_id("createTxt").click()
driver.find_element_by_id("link-to-download").click()

# Download pdf file
driver.find_element_by_id("pdfbox").send_keys("Testing pdf")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()