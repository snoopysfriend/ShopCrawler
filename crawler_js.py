from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import time
import urllib
import os
import sqlite3 

# create the DB
con = sqlite3.connect("test.db")
c = con.cursor()
con.execute("create table item(name, price)")

url = 'https://deo.shopeemobile.com/shopee/shopee-mobilemall-live-sg/assets/ShopPage.e361a50379495326ddb2.js'

url = "https://medium.com/dualcores-studio/make-an-android-custom-view-publish-and-open-source-99a3d86df228"
url = 'https://shopee.tw/locklockmall'
driver = webdriver.Chrome('./chromedriver')
content = driver.get(url)
time.sleep(3)
content_elements = driver.find_elements_by_class_name("col-xs-2")

for element in content_elements:
    content_html = element.get_attribute('innerHTML')
    #print(content_html)
    item = [] 
    soup = BeautifulSoup(content_html, 'html.parser')
    name = soup.find_all(class_="_1NoI8_ _1JBBaM")
    #print(name[0].string)
    item.append(name[0].string)
    price = soup.find_all(class_="_341bF0")
    item.append(price[0].string)
    #print(price[0].string)
    c.execute('insert into item(name, price) values (?, ?)', item)
    con.commit()

driver.close()
c.close()
con.close()

