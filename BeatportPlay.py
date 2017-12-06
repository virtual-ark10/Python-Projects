
import requests
from bs4 import BeautifulSoup


page = requests.get("http://classic.beatport.com/genre/trance/7/top-100")

soup = BeautifulSoup(page.content,"html.parser")

title = soup.findAll(class_="secondColumn")

i=0
for t in title:
    print(title[i].text)
    i += 1

print(t)