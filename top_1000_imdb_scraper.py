import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/search/title?count=1000&groups=top_1000&sort=user_rating"

site_request = requests.get(url)
site_html = BeautifulSoup(site_request.content, 'html.parser')

item_header = site_html.div.div.findAll('h3', {"class": "lister-item-header"})
item_names = []
for i in item_header:
	item_names.append(i.find('a').contents)
for item in item_names:
	stripped = str(item)[2: -2]
	with open('movielist.txt', 'a') as f:
		f.write(str(stripped) + '\n')
