from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://boston.craigslist.org/search/npo"

# Create a dictionary
d = {'key': 'value'}
print(d)

# update the dictionary
d['new key'] = 'new value'
print(d)

npo_jobs = {}
job_no = 0

while True:

    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    jobs = soup.find_all('p', {'class': 'result-info'})

    for job in jobs:
        title = job.find('a', {'class': 'result-title'}).text
        location_data = job.find('span', {'class': 'result-hood'})
        location = location_data.text if location_data else "N/A"
        date = job.find('time', {'class': 'result-date'}).text
        link = job.find('a', {'class': 'result-title'}).get('href')
        job_response = requests.get(link)
        job_data = job_response.text
        job_soup = BeautifulSoup(job_data, 'html.parser')
        job_description = job_soup.find('section', {'id': 'postingbody'}).text
        job_attributes_tag = job_soup.find('p', {'class': 'attrgroup'})
        job_attributes = job_attributes_tag.text if job_attributes_tag else "N/A"
        job_no += 1
        npo_jobs[job_no] = [title, location, date, link, job_attributes, job_description]
#        print('Job Title: ', title, '\nLocation: ', location, '\nDate: ', date, '\nLink: ', link, '\nJob_Description: ',
#              job_description, '\nJob Attributes: ', job_attributes, '\n---')

    url_tag = soup.find('a', {'title': 'next page'})
    if url_tag.get('href'):
        url = "https://boston.craigslist.org" + url_tag.get('href')
        print(url)
    else:
        break

print("Total Jobs: ", job_no)
npo_jobs_df = pd.DataFrame.from_dict(npo_jobs, orient='index', columns=['Job Title', 'Location', 'Date', 'Link', 'Job Attributes', 'Job Description'])

npo_jobs_df.to_csv('npo_jobs.csv')