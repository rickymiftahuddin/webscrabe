import requests
from bs4 import BeautifulSoup

url = 'https://www.goodreads.com/search?utf8=%E2%9C%93&query=dilan'

# membuat request
r = requests.get(url)
# hasil response
request = r.content

soup = BeautifulSoup(request, 'html.parser')
# extract element
title = soup.findAll('a', attrs={'class': 'bookTitle'})
author = soup.findAll('a', attrs={'class': 'authorName'})

count = 0
for i in range(0, len(title)):
    count += 1
    print("{0}. {1}\n   -{2}".format(
        count, title[i].text.strip(), author[i].text.strip()))
