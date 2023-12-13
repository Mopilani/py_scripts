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


# get all <h1> elements 
# on the page
h1_elements = soup.find_all('h1')
print('--------------------------------')
print(h1_elements)

# get the element with id="main-title"
main_title_element = soup.find(id='main-title')
print('--------------------------------')
print(main_title_element)

# find the email input element
# through its "name" attribute
# email_element = soup.find(attrs={'name': 'email'})

# find all the centered elements
# on the page
# centered_element = soup.find_all(class_='text-center')
