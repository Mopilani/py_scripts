#!/usr/bin/python3
""" Mostaql website scraper for geting related jops.

Mostaql platform have mail notification system sends new projects related to your
jop name, but not in the realtime.
at all this project is just for learning, it's useless more than useful at this time.
"""

import requests
import datetime
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

url = "https://mostaql.com/projects?category=development&budget_max=10000&sort=latest"

page = requests.get(url,
    headers=headers,
)

# print(page.headers)
# print('--------------------------------')
# print(page.content)

x = datetime.datetime.now()
# f = open("{x}.txt", "b")
# f.write(page.content)
# f.close()

soup = BeautifulSoup(page.text, 'html.parser')


# get all <h1> elements 
# on the page
# h1_elements = soup.find_all('h1')
# print('--------------------------------')
# print(h1_elements)

rows = soup.find_all('td')
print('--------------------------------')
print(rows)
# row = soup.find('td')
# row.;
open_projects = []

# extract the text of the row
for project_data in rows:
    project_data.find()
    url = project_data.find('a', href=True)['href']
    title = project_data.find('a', class_="").text
    time = project_data.find('time')['datetime']
    # offers = project_data.find('li', class_="fa fa-fw fa-ticket")
    offers = project_data.find('li', class_="text-muted").find('i')
    # descriptiion = project_data.find('a', class_="details-url");
    open_projects.append({
        'url': url,
        'title': title,
        'time': time,
        'offers': offers,
        # 'description': descriptiion,
    })
    print('--------------------------------')
    print({
        'url': url,
        'title': title,
        'time': time,
        'offers': offers,
        # 'description': descriptiion,
    })

# Create project tags list to save
project_tags = {
    # Structure:
    #   url : [tag1, tag2, ...]
}

# loop on projects
for project in open_projects:
    # get every project page
    project_url = project['url']
    page = requests.get(project_url,
        headers=headers,
    )

    # parse it
    soup = BeautifulSoup(page.text, 'html.parser')

    # find project tages
    tags = soup.find('')

    project_tags[project_url] = tags

# when tags to be same with wanted tags, send notification


# print(open_projects)

# print(row_td)


# get the element with id="main-title"
# main_title_element = soup.find(id='main-title')
# print('--------------------------------')
# print(main_title_element)

# find the email input element
# through its "name" attribute
# email_element = soup.find(attrs={'name': 'email'})

# find all the centered elements
# on the page
# centered_element = soup.find_all(class_='row-td')
