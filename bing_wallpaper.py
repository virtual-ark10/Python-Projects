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
from datetime import datetime

rand = random.randint(1,4)


os.makedirs("wallpapers/bing_walls", exist_ok=True)
os.makedirs("wallpapers/nasa_walls", exist_ok=True)
os.makedirs("wallpapers/wallhaven", exist_ok=True)

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
    
    //Be Sure To Change The Path To your own path where the wallpaper is saved..
    wallUrl ='file:///home/virtual-ark/workspace/Hello_World/Hello/wallpapers/bing_walls/'  + text.replace(" ", "%20")

    os.system('gsettings set org.gnome.desktop.background picture-uri %s' % (wallUrl))

    print("Wallpaper Changed!")


elif rand == 2:

    print("Retrieving NASA Image of the Day, Relax...")

    url3 = 'https://apod.nasa.gov/apod/'

    page3 = requests.get(url3)

    soup3 = BeautifulSoup(page3.content, "html.parser")

    nasa_image = soup3.select("a")[1].get("href")
    
    print("Downloading Image...")

    nasa_dl = requests.get(url3 + nasa_image)

    print(nasa_image)
    nasa_name = os.path.basename(nasa_image)

    print("Today's Wallpaper is Called " + nasa_name)

    with open(os.path.join("wallpapers/nasa_walls",nasa_name), 'wb') as nasaFile:
        nasaFile.write(nasa_dl.content)
    nasaFile.close()
    
    //Be Sure To Change The Path To your own path..
    os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/virtual-ark/workspace/Hello_World/Hello/wallpapers/nasa_walls/%s" % (nasa_name))

    print("Wallpaper Changed, Karibu!")

elif rand == 3:

    links = [] 

    print('Locating Wallpaper in WallHaven...')

    url4 = "https://alpha.wallhaven.cc/"

    page4 = requests.get(url4)

    soup4 = BeautifulSoup(page4.content,'html.parser')

    haven_image = soup4.find(id='featured').findAll("a")

    for im in haven_image:
        links.append(im.get("href"))
        
    rands = random.randint(0,len(links)-1)

    wall_page = requests.get(links[rands])

    bsoup4 = BeautifulSoup(wall_page.content,'html.parser')

    wall_image = bsoup4.find(class_='scrollbox')

    print("Downloading Wallpaper...")
    for image in wall_image:
        wall_link = image.get("src")
        wall = requests.get("https:"+wall_link)

    wall_name = os.path.basename(wall_link)
    with open(os.path.join("wallpapers/wallhaven/",wall_name), 'wb') as havenFile:
        havenFile.write(wall.content)
    havenFile.close();

    //Be Sure To Change The Path To your own path where the wallpaper is saved..
    os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/virtual-ark/workspace/Hello_World/Hello/wallpapers/wallhaven/%s" % (wall_name))

    print("Wallpaper Changed, Karibu!")

elif rand == 4:

    print("Searching Wallpaper from WallHaven...")

    pick = str(random.randint(1,12914))

    page5 = requests.get("https://alpha.wallhaven.cc/random?page="+pick)

    soup5 = BeautifulSoup(page5.content,'html.parser')

    rand_image = soup5.find(class_='preview')

    rand_image_link = rand_image.get("href")
    
    rand_page = requests.get(rand_image_link)

    bsoup5 = BeautifulSoup(rand_page.content, "html.parser")

    rand_wall = bsoup5.find(class_="scrollbox")

    for image in rand_wall:
        name = image.get("alt")[17:]
        rand_wallpaper = image.get("src")
        real_wall = requests.get("https:"+rand_wallpaper)

    print(pick + " Wallpaper Is Called " + name)
    rand_name = os.path.basename(rand_wallpaper)
    with open(os.path.join("wallpapers/wallhaven/",rand_name),'wb') as randFile:
        randFile.write(real_wall.content)
    randFile.close()

    //Be Sure To Change The Path To your own path where the wallpaper is saved..
    os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/virtual-ark/workspace/Hello_World/Hello/wallpapers/wallhaven/%s" % (rand_name))

    print("Wallpaper Changed, Karibu!")

    
    

