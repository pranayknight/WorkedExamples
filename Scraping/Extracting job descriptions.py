from bs4 import BeautifulSoup
import requests
url = "https://boston.craigslist.org/search/sof"
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, 'html.parser')
jobs = soup.find_all('p', {'class': 'result-info'})

for job in jobs:
    title = job.find('a', {'class': 'result-title'}).text
    location_data = job.find('span', {'class': 'result-hood'})
    location = location_data.text if location_data else "N/A"
    date = job.find('time', {'class': 'result-date'})
    link = job.find('a', {'class': 'result-title'}).get('href')
    job_response = requests.get(link)
    job_data = job_response.text
    job_soup = BeautifulSoup(job_data, 'html.parser')
    job_description = job_soup.find('section', {'id': 'postingbody'}).text
    job_attributes_tag = job_soup.find('p', {'class': 'attrgroup'})
    job_attributes = job_attributes_tag.text if job_attributes_tag else "N/A"
    print('Job Title: ', title, '\nLocation: ', location, '\nDate: ', date, '\nLink: ', link, '\nJob_Description: ', job_description, '\nJob Attributes: ',job_attributes, '\n---')