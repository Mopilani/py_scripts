#!/usr/bin/python3
""" HTML website scraper template """

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

page = requests.get('https://www.example.com/',
headers=headers,
)

print(page.headers)
print('--------------------------------')
print(page.content)

soup = BeautifulSoup(page.text, 'html.parser')
