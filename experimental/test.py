from lxml import html
from datetime import datetime
import requests


# Testing with Sonata Acrtica website

page = requests.get('http://sonataarctica.info/tour')
tree = html.fromstring(page.content)

date_strings = tree.xpath('//td[@class="date"]//text()')
venues = tree.xpath('//td[@class="venue"]/a//text()')
cities = tree.xpath('//td[@class="city"]//text()')

#Convert ishort form months to full month names
print('CONVERSIONS')
months = {'Jan':'January', 'Feb':'February', 'Mar':'March', 'Apr':'April', 'Jun':'June', 'Jul':'July', 'Aug':'August', 'Sep':'September', 'Sept':'September', 'Oct':'October', 'Nov':'November', 'Dec':'December'}
for x in date_strings:
    date = str.split(x)
    if date[0] in months:
        print(date[0], months[date[0]])
        date[0] = months[date[0]]
        x = date[0] + ' ' + date[1]



#dates = [datetime.strptime(date, '"%b%d"').date() for date in date_strings]


print('*************************************')
#print('Dates:', date_strings)
#print('Venues:', venues)
#print('Cities:', cities)
#print('')
#print('Date list size', len(date_strings))
#print('Venue list size', len(venues))
#print('City list size', len(cities))

if len(date_strings) == len(venues) == len(cities):
    print('lists equal. Creating Visual Table')

    titles = ['date', 'venue', 'city']
    data = [titles] + list(zip(date_strings, venues, cities))
    for i, d in enumerate(data):
        line = '|'.join(str(x).ljust(25) for x in d)
        print(line)
        if i == 0:
            print('-' * len(line))

else:
    print('ERROR! Lists NOT equal')
