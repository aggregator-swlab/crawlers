from bs4 import BeautifulSoup
import requests
import sys
import re
import urllib2



url = "http://www.amazon.in/s/ref=nb_sb_noss_2/278-5943722-6241930?url=search-alias%3Daps&field-keywords=lumia+535"
page = urllib2.urlopen(url)
soupe = BeautifulSoup(page, "html.parser")
all_links = soupe.find_all("li", class_="s-result-item celwidget")

for i in all_links:
	try:
		title = i.select('h2.a-text-normal')[0].string
	except:
		title = "NA"
	try:
		price = i.select('div.a-row div.a-span7 div.a-spacing-none a.a-text-normal span')[0].text.encode("utf-8")
	except:
		price = "NA"
	try:
		link = i.select('div.a-col-right div.a-spacing-small a.a-text-normal')[0].get("href")
	except:
		link = "NA"
	try:
		imgurl = i.select('div.a-row div.a-text-center a.a-text-normal img')[0].get("src")
	except:
		imgurl = "NA"
	try:
		rating = i.select('a.a-popover-trigger span.a-icon-alt')[0].text
		if rating.endswith(" out of 5 stars"):
			rating = rating[:-15]
	except:
		rating = "NA"

	print "Title : " + title
	print "Price : " + price
	print link
	print "Img Url : " + imgurl
	print "Rating : " + rating
	print "\n\n************************\n\n"