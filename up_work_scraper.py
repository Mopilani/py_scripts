import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.upwork.com/freelance-jobs/virtual-assistant/')

print(page.headers)
print('--------------------------------')
print(page.content)
