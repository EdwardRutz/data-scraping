from urllib.request import urlopen   # handle server requests to url
from bs4 import BeautifulSoup

html = urlopen('https://treehouse-projects.github.io/horse-land/index.html')  # Pass in the url to scrape
soup = BeautifulSoup(html.read(), 'html.parser')  # create BSoup object, pass in html, call read() and pass in parser

# print(soup.prettify())  # Prettify formats the output
# print(soup.title)

# Find all divs
# divs = soup.find('div', {'class': 'featured'}) # filter by class "featured"
#     print(divs)

for link in soup.find_all('a'):
    print(link.get('href'))
