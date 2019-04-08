from bs4 import BeautifulSoup
import requests
import pandas as pd
import re


def scrape_details(soup, main_address, no_of_pages):
    # Empty Dictionary in which scraped data will be saved
    scrape_details_dict = {}

    # Maintains count of APIs that are scraped
    api_count = 0

    # Maintains count of pages that are scraped
    page_count = 0

    while True:
        page_count += 1
        print('Scraping API information from Page {}:\n'.format(page_count))
        table_contents = soup.find("table", {"class": "views-table"}).find("tbody").find_all("tr")
        for single_row in table_contents:
            api_count += 1

            # Name of the API
            api_name = single_row.find("td", {"class": "views-field-title"}).text.strip()

            # URL of the API
            api_abs_url = single_row.find("td", {"class": "views-field-title"}).find("a").get("href")

            # Category of the API
            api_category = single_row.find("td", {"class": "views-field-field-article-primary-category"}).text.strip()

            # Date of the API
            api_date = single_row.find("td", {"class": "views-field-created"}).text.strip()

            # Navigate to the Description page of the API
            description_response = requests.get(main_address + api_abs_url).text
            description_soup = BeautifulSoup(description_response, 'html.parser')

            if description_soup.find("div", {"class": "api_description"}):
                # Description of the API
                api_description = description_soup.find("div", {"class": "api_description"}).text.strip()
            else:
                # Description of the API [in some pages the tag is different Eg: API no. 33]
                api_description = description_soup.find("p", {"class": "node-defunct-message"}).text.strip()

            # Save all the details of the API in a dictionary
            scrape_details_dict[api_count] = [api_name, api_abs_url, api_category, api_date, api_description]
            print('API No. {} scraped'.format(api_count))
        next_page_tag = soup.find("a", {"title": "Go to next page"})

        if next_page_tag.get("href"):
            if page_count < no_of_pages:
                next_page_url = main_address + next_page_tag.get("href")
                next_page_response = requests.get(next_page_url).text
                soup = BeautifulSoup(next_page_response, 'html.parser')
            else:
                break
        else:
            break

    print('\nTotal APIs: ', api_count)
    print('Total Pages Scraped: ', page_count)

    # Returns information of the APIs that are scraped.
    return scrape_details_dict
MAIN_ADDRESS = "https://www.programmableweb.com"
URL = MAIN_ADDRESS + "/apis/directory"
response = requests.get(URL)
html_data = response.text
soup = BeautifulSoup(html_data, 'html.parser')
# Number of Pages to be scraped.
# NOTE -> Increasing the number of pages will increase the time it takes to scrape the pages.
no_of_pages = 2
scraped_details = scrape_details(soup, MAIN_ADDRESS, no_of_pages)

api_info_dataframe = pd.DataFrame(data=list(scraped_details.values()), columns=['API Name','API URL','API Category','API Date','API Description'])
# print(api_info_dataframe)
api_info_dataframe.to_csv('Sample_APIs_Details.csv')
