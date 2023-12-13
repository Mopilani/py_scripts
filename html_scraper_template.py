import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.example.com/')

print(page.headers)
print('--------------------------------')
print(page.content)
