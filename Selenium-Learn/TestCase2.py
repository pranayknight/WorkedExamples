import unittest
from selenium import webdriver

class SearchEnginesTest(unittest.TestCase):
    def test_google(self):
        self.driver = webdriver.Firefox(executable_path="/home/pranay/Drivers/geckodriver-v0.24.0-linux64/geckodriver")
        self.driver.get("https://www.google.com/")
        print("Title of the page: ", self.driver.title)
        self.driver.close()

    def test_bing(self):
        self.driver = webdriver.Firefox(executable_path="/home/pranay/Drivers/geckodriver-v0.24.0-linux64/geckodriver")
        self.driver.get("https://bing.com")
        print("Title of the page: ", self.driver.title)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()