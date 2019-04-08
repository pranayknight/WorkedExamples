from bs4 import BeautifulSoup
import requests
url = 'https://boston.craigslist.org/search/sof'
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, 'html.parser')
titles = soup.find_all('a', {"class": "result-title"})
for title in titles:
    print(title.text)
addresses = soup.find_all('span', {'class': 'result-hood'})
for address in addresses:
    print(address.text)
    