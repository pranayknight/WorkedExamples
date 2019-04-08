from bs4 import BeautifulSoup
import requests
url = "https://boston.craigslist.org/search/sof"
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, 'html.parser')
jobs = soup.find_all('p', {'class': 'result-info'})
for job in jobs:
    title = job.find('a', {'class': 'result-title'}).text
    address_tag = job.find('span', {'class': 'result-hood'})
    address = address_tag.text if address_tag else "N/A"
    date = job.find('time', {'class': 'result-date'}).text
    link = job.find('a', {'class': 'result-title'}).get('href')
    print('Job Title: ', title, '\nLocation: ', address, '\nDate: ', date, '\nLink: ', link, '\n---')
