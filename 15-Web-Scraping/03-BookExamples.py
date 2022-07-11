import os
from unittest import result
os.system('cls')
import requests
import bs4

# GOAL: Get title of every title with 2 start rating

# base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
# base_url.format('12')
# result = requests.get(base_url.format(1))
# soup = bs4.BeautifulSoup(result.text,"lxml")

# products = soup.select(".product_pod")

# example = products[0]
# print(example)

# Quick and dirty
# print('star-rating two' in str(example))

# print(example.select('.star-rating.Two'))

# print(example.select('a')[1]['title'])

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
two_star_titles = []

for n in range (1,51):
    scrape_url = base_url.format(n)
    result = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(result.text,"lxml")  

    books = soup.select(".product_pod")

    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)

for title in two_star_titles:
    print(title)