#!/bin/bash
#!/usr/bin/python3

"""
Created on Apr 8, 2017

@author: virtual-ark
"""
import requests
from bs4 import BeautifulSoup
import os
import random


rand = random.randint(1,2)


os.makedirs("wallpapers/bing_walls", exist_ok=True)
os.makedirs("wallpapers/nasa_walls", exist_ok=True)
os.makedirs("wallpapers/natgeo_walls", exist_ok=True)

if rand == 1:
    url = "https://bingwallpaper.com/"

    page = requests.get(url)

    soup = BeautifulSoup(page.text,"html.parser")

    imageUrl = soup.find_all({"img": "src"})[1].get("src")

    alt = soup.find_all({"img": "src"})[1].get("alt")

    text = alt.split('(')[0]

    print("Downloading Bing Wallpaper...")
    wallpaper = requests.get(imageUrl)

    with open(os.path.join("wallpapers/bing_walls",os.path.basename(text)), 'wb') as bingFile:
        
        bingFile.write(wallpaper.content)
    wallUrl ='file:///home/virtual-ark/workspace/Hello_World/Hello/wallpapers/bing_walls/'  + text.replace(" ", "%20")

    os.system('gsettings set org.gnome.desktop.background picture-uri %s' % (wallUrl))

    print("Wallpaper Changed!")

    #elif rand == 2

    """url = 'http://www.nationalgeographic.com/photography/photo-of-the-day/'
    
page2 = requests.get(url)
time.sleep(20)  
soup2 = BeautifulSoup(page2.content,"lxml")
    
natGeo = soup2.findAll("source", {"srecset":re.compile("(http:\/\/yourshot\.nationalgeographic\.com\/u\/.*\/2048w)$")})
    
        
geo_page = open("natgeo.html", "w")
geo_page.write(str(natGeo))
geo_page.close()
print("copied")"""

elif rand == 2:
    print("Retrieving NASA image of the day...")

    url3 = 'https://apod.nasa.gov/apod/'

    page3 = requests.get(url3)

    soup3 = BeautifulSoup(page3.content, "html.parser")

    nasa_image = soup3.select("a")[1].get("href")
    
    print(nasa_image)
    print("Downloading Image...")

    nasa_dl = requests.get(url3 + nasa_image)

    print(nasa_image)
    nasa_name = os.path.basename(nasa_image)

    print("The name of todays wallpaper is " + nasa_name)

    with open(os.path.join("wallpapers/nasa_walls",nasa_name), 'wb') as nasaFile:
        nasaFile.write(nasa_dl.content)
    nasaFile.close()

    os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/virtual-ark/workspace/Hello_World/Hello/wallpapers/nasa_walls/%s" % (nasa_name))

    print("Wallpaper Changed!")












    
    
    


