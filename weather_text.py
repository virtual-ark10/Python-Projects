'''
Created on Apr 1, 2017

@author: Stan-Lee
'''
import textmyself
import requests 
from bs4 import BeautifulSoup
import sys

url  = 'http://www.msn.com/en-us/weather/today/Nairobi,Nairobi-Area,Kenya/we-city--1.283,36.817?iso=KE'
        
page = requests.get(url)

soup = BeautifulSoup(page.content, "html5lib")

temp = soup.findAll(class_= "current")[1].get_text()

brief = soup.findAll(class_ = "weather-info")[0].get_text().strip().split("\n")[0]

celcius = round(int((int(temp) - 32) * 0.5556))

print(celcius)

print(brief)

if celcius < 15:
    textmyself.textmyself("It's VERY cold today please carry a jacket \n" + "The temp. is %s \n" % (celcius)
                + brief)
elif 15 < celcius < 25:
    textmyself.textmyself("It is probably going to rain today be sure to carry an umbrella" + "The temp. is %s \n" % (celcius)
                + brief)
else:
    sys.exit()
  
    






