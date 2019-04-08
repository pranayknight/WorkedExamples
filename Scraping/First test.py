from bs4 import BeautifulSoup
import requests  #imports the request library
url="https://boston.craigslist.org/search/sof"  #defining string for the the specified url needed
response=requests.get(url)  #getting the response code from that url
print(response)    #if it shows Response [200] that means you have successfully opened the url
data=response.text  #getting all the content from the given url page in the form of text
print(data)   #see the raw data in text
