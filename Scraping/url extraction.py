from bs4 import BeautifulSoup
import requests
url = "https://boston.craigslist.org/search/sof"
response = requests.get(url)
# print(response)
data = response.text
# print(data)
soup = BeautifulSoup(data, 'html.parser')  # arranges the data in proper manner so that when viewed gives a clear idea
tags = soup.find_all('a')   # creating a list in all the 'a' tags
for tag in tags:
    print(tag.get('href'))  # getting all the urls in the given page
