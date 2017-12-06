'''
Created on Apr 25, 2017

@author: Stan-Lee
'''
import requests
from bs4 import BeautifulSoup


page = requests.get("http://gomovies.to")

soup = BeautifulSoup(page.content,"html.parser")

qualitytop = soup.find(class_="movies-list-wrap mlw-topview mt20").findAll(class_="mli-quality")

qualitylat = soup.find(class_="movies-list-wrap mlw-latestmovie").findAll(class_="mli-quality")

title = soup.find(class_="movies-list-wrap mlw-topview mt20").findAll(class_="mli-info")

link = soup.findAll()
i=0
for q in qualitylat:
    print(title[i].text + " " + qualitytop[i].text) #+ " " + q.text)
    i += 1