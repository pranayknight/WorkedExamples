import requests
from bs4 import BeautifulSoup

r = requests.get("https://en.wikipedia.org/wiki/Machine_learning")
html_content = r.text
soup = BeautifulSoup(html_content, 'lxml')

contents = soup.select('.toctext')
for content in contents:
    print(content.text)