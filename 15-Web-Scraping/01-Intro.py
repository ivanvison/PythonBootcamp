import os
from unittest import result
os.system('cls')
import requests
import bs4

result = requests.get("http://example.com/")
#print(result.text)
soup = bs4.BeautifulSoup(result.text,"lxml")
#print(soup)
print(soup.select('title')[0].getText())
print(soup.select('p')[0].getText())
