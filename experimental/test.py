from lxml import html
import requests

# Testing with Sonata Acrtica website

page = requests.get('http://sonataarctica.info/tour')
tree = html.fromstring(page.content)

#buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#prices = tree.xpath('//span[@class="item-price"]/text()')

dates = tree.xpath('//td[@class="date"]//text()')
venues = tree.xpath('//td[@class="venue"]/a//text()')
cities = tree.xpath('//td[@class="city"]//text()')
#print('Buyers:', buyers)
#print('\n')
#print('Prices:', prices)
print('Dates:', dates)
print('Venues:', venues)
print('Cities:', cities)
