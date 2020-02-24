from bs4 import BeautifulSoup
from selenium.webdriver import Chrome

import time

driver = Chrome()

driver.get('https://treehouse-projects.github.io/horse-land/index.html')

time.sleep(5)

page_html = driver.page_source

soup = BeautifulSoup(page_html, 'html.parser')
print(soup.prettify())
driver.close()


