import os
from unittest import result
import requests
import bs4

os.system('cls')

#result = requests.get("http://quotes.toscrape.com/")
#print(result.text) # First Task
#soup = bs4.BeautifulSoup(result.text,"lxml")

'''
# Get the name of all the authors in the first page
authors = set()

for name in soup.select('.author'):
    authors.add(name.text)

print(authors)

print('----------')
# TASK: Create a list of all the quotes on the first page.

quotes = []

for quote in soup.select('.text'):
    quotes.append(quote.text)

print(quotes)

print('----------')
# TASK: Inspect the site and use Beautiful Soup to extract the top ten tags from the requests text shown on the top right from the home page

tags = []

for tag in soup.select('.tag-item'):
    tags.append(tag.text.strip('\n'))

print(tags)

print('----------')
'''

# TASK: Unique authors

base_url = 'http://quotes.toscrape.com/page/{}/'
validPage = True
authors = set()
page = 1

while validPage == True:
    #scrape_url = base_url.format(page)
    result = requests.get(base_url.format(page))
    soup = bs4.BeautifulSoup(result.text,"lxml")

    print(f'Checking Page: {page}\n')

    if "No quotes found!" in result.text:
        validPage = False
    else:
        for name in soup.select('.author'):
            authors.add(name.text)
        page += 1

print(f'Done checking pages. Total of {page - 1} pages.\n')    
print(authors)


