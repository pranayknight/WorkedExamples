import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/w/index.php' + \
      '?title=List_of_Game_of_Thrones_episodes&oldid=802553687'
r = requests.get(url)
html_contents = r.text
html_soup = BeautifulSoup(html_contents, 'lxml')
'''print(html_soup.find('h1'))
print(html_soup.find('', {'id': 'p-logo'}))
for found in html_soup.find_all(['h1', 'h2']):
      print(found)'''

# Find the first h1 tag
first_h1 = html_soup.find('h1')
print(first_h1.name)   #h1
print(first_h1.contents)   # ['List of', [...], 'episodes']

print(str(first_h1))
# Prints out: <h1 class="firstHeading" id="firstHeading" lang="en">List of
#              <i>Game of Thrones</i> episodes</h1>

print(first_h1.text)          # Lists of Game of Thrones Episodes
print(first_h1.get_text())    # Does the same

print(first_h1.attrs)
# Prints out: {'id': 'firstHeading', 'class': ['firstHeading'], 'lang': 'en'}

print(first_h1.attrs['id'])    # First Heading
print(first_h1['id'])          # Does the same
print(first_h1.get('id'))      # Does the same

print('------------CITATIONS------------')

# Find the first five elements with the citation class
cities = html_soup.find_all('cite', class_='citation', limit=5)

for citation in cities:
      print(citation.get_text())
      # Inside this citation element find the first a tag
      link = citation.find('a')
      # and show it url
      print(link.get('href'))
      print()
