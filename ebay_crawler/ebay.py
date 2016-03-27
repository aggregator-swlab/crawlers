from bs4 import BeautifulSoup
import requests
import sys
import re
import urllib2


url = "http://www.ebay.in/sch/i.html?_nkw=iphone+6"
page = urllib2.urlopen(url)
soupe = BeautifulSoup(page, "html.parser")
all_links = soupe.find_all("li", class_="sresult lvresult clearfix li")

for i in all_links:
    try:
        title = i.select('h3.lvtitle a.vip')[0].text.encode("utf-8").strip()
    except:
        title = "NA"
    try:
        mrp = i.select('li.lvprice span.bold')[0].text.encode("utf-8").strip()
    except:
        mrp = "NA"
    try:
        link = i.select('h3.lvtitle a.vip')[0].get("href")
    except:
        link = "NA"
    try:
        imgurl = i.select('img.img')[0].get("src")
    except:
        imgurl = "NA"

    print title
    print mrp
    print link
    print imgurl
    print "\n\n************************\n\n"