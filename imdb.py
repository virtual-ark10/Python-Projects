'''
Created on Apr 26, 2017

@author: virtual-ark
'''

import requests
from bs4 import BeautifulSoup
import webbrowser
import re
import sys



def search(movie):
    if movie == "" or movie == " ":
        print("Please Enter a Valid Movie Title!")
    
    else:
        movie.replace(" ", "+")
        page = requests.get("http://www.imdb.com/find?ref_=nv_sr_fn&q=" + movie)
        soup = BeautifulSoup(page.content,"html.parser")
        try:
            link = soup.findAll("a", {"href":re.compile("(\/title\/.*)$")})[0].get("href")
            return link
        except IndexError as ie:
            print(ie, "movie not found in imdb")
   
def rate(movie):
    if movie == "" or movie == " ":
        print("Please Enter A Valid Movie Title!")
        
    else:
        
        link = search(movie)
        page = requests.get("http://www.imdb.com" + link)
        soup = BeautifulSoup(page.content, "html.parser")
    try:
        rating = soup.findAll(itemprop="ratingValue")[0].text
        return rating 
    except IndexError:
        print("No Rating Found for" + movie + "!")
    

def trailer(movie):
    if movie == "" or movie == " ":
        print("Please Enter A Valid Movie Title!")
    else:
        url = "https://www.youtube.com/results?search_query=" + movie + "+trailer"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        try:
            trail = soup.findAll("a",{"href":re.compile("(\/watch\?v=.*)$")})[0].get("href")
            webbrowser.open("http://www.youtube.com" + trail) 
        except IndexError:
            print("Sorry, " + movie + " dosen't have a trailer!")
    
        sys.exit(0)

def about(movie):
    if movie == "" or movie == " ":
        print("Please Enter A Valid Movie Title!")
    else:
        link = search(movie)
        page = requests.get("http://www.imdb.com" + link)
        soup = BeautifulSoup(page.content,"html.parser")
        try:
            summary = soup.findAll(class_="summary_text")[0].text.strip()
            return summary
        except IndexError:
            print("Sorry no Summary of " + movie + " was found")
        sys.exit(0)
    

trailer("hannibal")


