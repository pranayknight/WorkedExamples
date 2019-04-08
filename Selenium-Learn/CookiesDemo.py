from selenium import webdriver

driver = webdriver.Firefox(executable_path="/home/pranay/Drivers/geckodriver-v0.24.0-linux64/geckodriver")
driver.get("https://www.amazon.in/")

# Capture all the cookies created by the browser
cookies = driver.get_cookies()

print(len(cookies))   # Print the no. of cookies that has been created

print(cookies)    # Prints all the cookies that has been captured

# Adding new cookies to the browser
cookie = {'name': 'Mycookie', 'value': '1234567890'}
driver.add_cookie(cookie)

cookies = driver.get_cookies()
print(len(cookies))   # Print the no. of cookies after adding the new cookies
print(cookies)    # Prints all the cookie pairs

# Deleting a cookie by name
driver.delete_cookie('Mycookie')
cookies = driver.get_cookies()
print(len(cookies))

# Deleting all the cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print(len(cookies))


driver.quit()