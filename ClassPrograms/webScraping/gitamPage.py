import requests as rs
from bs4 import BeautifulSoup as bs

page = rs.get('https://www.gitam.edu/')
src = page.content
soup = bs(src, 'lxml')


programs = []

for h2_tag in soup.find_all('h2'):
    if h2_tag.text == "Admissions":
        