from bs4 import BeautifulSoup
import requests
import sys
import re
import urllib2



url = "http://www.flipkart.com/search?q=lumia+535"
page = urllib2.urlopen(url)
soupe = BeautifulSoup(page, "html.parser")
all_links = soupe.find_all("div", class_="gd-col gu3")
for i in all_links:
	imgurl = i.find('img')['data-src']
	title = i.select('a.fk-display-block')[0].get('title')
	link = i.select('a.fk-display-block')[0].get('href')
	if i.has_attr('div.fk-stars-small'):
		rating = i.select('div.fk-stars-small')[0].get('title')
	else:
		rating = "NA"
	# rating = i.select('div.fk-stars-small')[0].get('title')
	lst = list()
	for j in range(0, len(i.select('ul.pu-usp li'))):
		lst.append(i.select('ul.pu-usp li span')[j].string)
	price = i.select('span.fk-font-17')[0].string
	# feature1 = i.select('ul.pu-usp li span')[0].string
	# feature2 = i.select('ul.pu-usp li span')[1].string
	# feature3 = i.select('ul.pu-usp li span')[2].string
	# feature4 = i.select('ul.pu-usp li span')[3].string

	print "Title : " + title
	print "Price : " + price
	print "Link : www.flipkart.com" + link
	print "Img Url : " + imgurl
	print "Rating : " + rating
	k=1
	for j in lst:
		print "Feature " + str(k) + " : " + j
		k=k+1
	print "\n\n********************************\n\n"