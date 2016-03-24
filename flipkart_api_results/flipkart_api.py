import subprocess
import json
from pprint import pprint

query = "iphone+6"
f = open("flipkart_raw_data", "w")
process = subprocess.call(['curl',  '-H', 'Fk-Affiliate-Id:shariffaz', '-H', 'Fk-Affiliate-Token:c569d5da22704c278e90af8226c42174', 'https://affiliate-api.flipkart.net/affiliate/search/json?query=' + query + '&resultCount=10'], stdout=f)

with open('flipkart_raw_data') as data_file:
	data = json.load(data_file)

# pprint(data)
# print "\n\n*****************\n\n"

# i = 0
# j = 0
# allprods = [[]]
for value in data["productInfoList"]:
	prodcat = value['productBaseInfo']['productIdentifier']['categoryPaths']['categoryPath'][0][0]['title']
	prodid = value['productBaseInfo']['productIdentifier']['productId']
	prodtitle = value['productBaseInfo']['productAttributes']['title']
	prodimgurl = value['productBaseInfo']['productAttributes']['imageUrls']['unknown']
	prodmrp = value['productBaseInfo']['productAttributes']['maximumRetailPrice']['amount']
	prodsp = value['productBaseInfo']['productAttributes']['sellingPrice']['amount']
	produrl = value['productBaseInfo']['productAttributes']['productUrl']
	prodbrand = value['productBaseInfo']['productAttributes']['productBrand']

	print prodcat
	print prodid
	print prodtitle
	print prodimgurl
	print prodmrp
	print prodsp
	print produrl
	print prodbrand
	print "\n\n*****************\n\n"

	# allprods[i] = array(prodid,prodcat,prodtitle,prodimgurl,prodmrp,prodsp,produrl,prodbrand)