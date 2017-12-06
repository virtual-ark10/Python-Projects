'''
Created on Apr 6, 2017

@author: Stan-Lee
'''

import requests
from bs4 import BeautifulSoup
import os


url = 'http://zenpencils.com/'

zenPath = "C:\\Users\\PAVILION 15\\Desktop\\zencomics"

comicFolder = os.makedirs(zenPath, exist_ok=True)

while not url.endswith("comics/1-ralph-waldo-emerson-make-them-cry/"):
    print("Downloading the page %s" % (url))
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    comic = soup.select("#comic img")
    
    counter = 0
    for link in comic:
        sup = [link["src"]]
        counter = counter + 1
        if counter <= 1:
            comic = soup.select("#comic img")[0].get("src")
            if comic == []:
                print("Comic not Found!")
        
            else:
                print("Downloading comic %s" % (comic))
                dlComic = requests.get("http:" +  comic)
                imageFile = open(os.path.join(zenPath, os.path.basename(comic)), 'wb')
                for chunk in dlComic.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()
    
    
            prevLink = soup.find(class_ = 'navi comic-nav-previous navi-prev').get("href")
            url = prevLink

        else:
            comic = soup.select("#comic img")[0].get("src")
            comic1 = soup.select("#comic img")[1].get("src")
            if comic == [] or comic == []:
                print("Comic not Found!")
            else:
                print("Downloading comic %s\n%s" % (comic, comic1))
                dlComic = requests.get("http:" +  comic)
                dlComic1 = requests.get("http:" +  comic1)
                imageFile = open(os.path.join(zenPath, os.path.basename(comic)), 'wb')
                imageFile1 = open(os.path.join(zenPath, os.path.basename(comic1)), 'wb')

                for chunk in dlComic.iter_content(100000):
                    imageFile.write(chunk)
                    print("Downloaded...")
                for chunk1 in dlComic1.iter_content(100000):
                        imageFile1.write(chunk1)
                        print("Downloaded 2...")
                        #time.sleep(3000)
                imageFile.close()
    
    
            prevLink = soup.find(class_ = 'navi comic-nav-previous navi-prev').get("href")
            url = prevLink
    
print("Done...")
        
    
   
     

