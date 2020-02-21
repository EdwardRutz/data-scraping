from urllib.request import urlopen
from bs4 import BeautifulSoup

import re

site_links = []

def internal_links(linkURL):
    html = urlopen('https://treehouse-projects.github.io/horse-land/{}'
                .format(linkURL))
    soup = BeautifulSoup(html, 'html.parser')

    return soup.find('a', href=re.compile('(.html)$'))

if __name__ == '__main__':
    urls = internal_links('index.html')

    while len(urls) > 0:
        page = urls.attrs['href']
        if page not in site_links:
            site_links.append(page)

            print(page)
            print('\n======================\n')
            urls = internal_links(page)
        else:
            break



# Separate external and internal links
# Go through list of links
# Check to see if the external link is alread listed, if not added it to list
# Use regular expressions to work with URLs