from bs4 import BeautifulSoup
import requests
import sys
import re
import urllib2


url = "http://www.snapdeal.com/search?keyword=iphone%206&noOfResults=48&sort=rlvncy"
page = urllib2.urlopen(url)
soupe = BeautifulSoup(page, "html.parser")
all_links = soupe.find_all("div", class_="col-xs-6 product-tuple-listing js-tuple ")
for i in all_links:
	try:
		title = i.select('p.product-title')[0].string
	except:
		title = "NA"
	try:
		mrp = i.select('span.product-desc-price.strike')[0].string
	except:
		mrp = "NA"
	try:
		sp = i.select('span.product-price')[0].string
	except:
		sp = "NA"
	try:
		link = i.select('div.product-tuple-image a')[0].get("href")
	except:
		link = "NA"
	try:
		imgurl = i.select('div.product-tuple-image img')[0].get("src")
		if imgurl == None:
			imgurl = i.select('div.product-tuple-image img')[0].get("lazysrc")
	except:
		imgurl = "NA"
	try:
		rating = i.select('div.filled-stars')[0].get("style")[6:8]
	except:
		rating = "NA"

	print "Title : " + title
	print "Price : " + mrp
	print "Price : " + sp
	print "Link : " + link
	print imgurl
	print "Rating : " + rating
	print "\n\n************************\n\n"