'''
Created on Apr 2, 2017

@author: Virtual-ark
'''

from getpass import getpass
import sys
import re
import requests
from bs4 import BeautifulSoup
import webbrowser


def torrent(searchWord):
 
    url = 'https://thepiratebay.org/search/' + searchWord
    
    page = requests.get(url)

    
    soup = BeautifulSoup(page.text, 'html.parser')
    
    tors = soup.find_all('a',class_ = 'detLink' ,limit=10)
    i = 0
    k = 0
    list = [] 
    print("*"*40 + " The PirateBay Results: " + "*"*40 + "\n")
    for j in tors:
        list.append(j.get("href"))
        seeds = soup.find_all('td',{'align' : 'right'})
        print(str(k + 1) +". " + tors[i].text + "  " + seeds[i].text + "\n" + "-"*10)
        i = i + 1
        k = k + 1 
    #print(tors[0].text)
    
    searchWord.replace(" ", '+')
    url2 = 'https://extratorrent.cc/search/?search=' + searchWord + "&s_cat=&pp=&srt=seeds&order=desc"
    
    page2 = requests.get(url2)
    
    soup2 = BeautifulSoup(page2.content, "html.parser")
    
    tor = soup2.findAll("a",{"href":re.compile("(magnet:\?.*)$")}, limit=10)
    title = soup2.findAll(class_="tli")
    seeds1 = soup2.findAll(class_="sy")

    
    i = 0
    j = 10
    list2 = []
    print("*"*40 + " Extratorrent Results: " + "*"*40 + "\n")
    for link in tor:
        list2.append(link.get("href"))
        try:
            print(str(j + 1) + ". " + title[i].text+ " " + seeds1[i].text  + "\n" + "-"*10)
        except IndexError:
            print("No seeds")
        i += 1     
        j += 1
        
    searchWord.replace(" ","+")
    url3 = "http://1337x.to/search/" + searchWord + "/1/"
    
    page3 = requests.get(url3)
    
    soup3 = BeautifulSoup(page3.content,"html.parser")
    
    torr = soup3.find_all("a",{"href":re.compile("(\/torrent\/.*)$")},limit=10)
    
    title3 = soup3.findAll(class_="coll-1 name")[1:]
    
    seeds3 = soup3.find_all(class_="coll-2 seeds")
    
    #for title in title3:
        #print(title.text)
    i=0
    m = 20
    list3 = []
    print("*"*40 + " 1337x Results: " + "*"*40 + "\n")
    for link in torr:
        list3.append(link.get("href"))
        print(str(m + 1)+ ". " + title3[i].text + " " + seeds3[i].text + "\n" + "-"*10 )
        i += 1
        m += 1
    
    searchWord.replace(" ","-")
    url4 = "https://www.limetorrents.cc/search/all/" + searchWord + "/seeds/1/"
    page4 = requests.get(url4)
    soup4 = BeautifulSoup(page4.content,"html.parser")
    torr4 = soup4.find_all("a",{"href": re.compile("(.*\.html)$")},limit=20)
    title4 = soup4.find_all(class_="tt-name")[3:]
    seeds4 = soup4.findAll(class_="tdseed")[3:]
    
    
    i=0
    n=30
    list4 = []
    print("*"*40 + " limetorrents Results: " + "*"*40 + "\n")
    for ln in torr4:
        list4.append(ln.get("href"))
        print(str(n + 1) + ". " + title4[i].text + " " + seeds4[i].text + "\n" + "-"*10)
        i += 1
        n += 1
       
    """searchWord.replace(" " , "+")
    
    url5 = "https://katcr.co/new/torrents-search.php?search=" + searchWord
    
    page5 = requests.get(url5)
    
    soup5 = BeautifulSoup(page5.content,"html.parser")
    
    link5 = soup5.getAll()"""
    
    
    
    option = int(input("Select Choice: "))
    if option <= 10:
        print("Downloading " + tors[option-1].text)
        url = "https://thepiratebay.org" + list[option-1]
        pages = requests.get(url)
        soupbay = BeautifulSoup(pages.text, "html.parser")
        magnet = soupbay.find_all(title = "Get this torrent")
        webbrowser.open(magnet[0].get("href"))
        sys.exit()
        
    elif option <= 20:
        print("Downloading " + title[option-11].text)
        webbrowser.open(list2[option-11])
        sys.exit()
    
    elif option <= 30:
        print("Downloading " + title3[option-21].text)
        url = "https://1337x.to" + list3[option-21]
        webx = requests.get(url)
        soupx = BeautifulSoup(webx.text,"html.parser")
        mag = soupx.findAll("a",{"href": re.compile("(magnet:\?.*)$")})
        webbrowser.open(mag[0].get("href"))
        sys.exit()
    
    elif option <= 50:
        print("Downloading " + title4[option-31].text)
        url = "https://www.limetorrents.cc" + list4[option-31]
        webl = requests.get(url)
        soupl = BeautifulSoup(webl.text,"html.parser")
        limemag = soupl.findAll("a",{"href": re.compile("(magnet:\?.*)$")})
        webbrowser.open(limemag[0].get("href"))
        sys.exit()
        
    
    
    
    
torrent('quality of earnings')
    

       
    

               




    
    

