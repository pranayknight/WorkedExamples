# Don't run in wikipedia page change the url some other base page

import requests
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = requests.get("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html.text, 'lxml')
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # We have encountered a new page
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")