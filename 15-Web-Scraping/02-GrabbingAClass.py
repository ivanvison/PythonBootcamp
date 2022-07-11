import os
from unittest import result
os.system('cls')
import requests
import bs4

result = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
#print(result.text)
soup = bs4.BeautifulSoup(result.text,"lxml")
#print(soup)
#toctext = soup.select('.toctext')
#for t in toctext:
#    print(t.text)

wikiimg = soup.select('.thumbimage')[0]
print(wikiimg)

print(len(wikiimg))
print(wikiimg['src'])
imgsrc = 'https:' + wikiimg['src']
image_link = requests.get(imgsrc)

#image_link.content

f = open('wikiimage.png','wb')
f.write(image_link.content)
f.close()

