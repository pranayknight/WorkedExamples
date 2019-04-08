from selenium import webdriver

driver = webdriver.Firefox(executable_path="/home/pranay/Drivers/geckodriver-v0.24.0-linux64/geckodriver")
driver.get("file:///home/pranay/Documents/Sample.html")

rows = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr"))   # Count the no. of rows present
cols = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/th"))  # Count the no. of columns

print(rows)
print(cols)
print('Product','  ','Article','  ','Price')

for r in range(2, rows+1):
    for c in range(1, cols+1):
        value = driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value, end='     ')
    print()