from lxml import html
import datetime
import requests


# Testing with Sonata Acrtica website

page = requests.get('http://sonataarctica.info/tour')
tree = html.fromstring(page.content)

date_raw = tree.xpath('//td[@class="date"]//text()')
venues = tree.xpath('//td[@class="venue"]/a//text()')
cities = tree.xpath('//td[@class="city"]//text()')

#Convert ishort form months to full month names
print('CONVERTING DATES.....')
months = {'Jan':'January', 'Feb':'February', 'Mar':'March', 'Apr':'April', 'Jun':'June', 'Jul':'July', 'Aug':'August', 'Sep':'September', 'Sept':'September', 'Oct':'October', 'Nov':'November', 'Dec':'December'}
date_strings = []

for x in date_raw:
    date = str.split(x)
    if date[0] in months:
        #print(date[0], months[date[0]])
        date[0] = months[date[0]]
        to_insert = date[0] + ' ' + date[1]
        #print(to_insert)
        date_strings.append(to_insert)
        #print(date_strings)

print('Dates Converted')
print('\n'+'Strings')
print(date_strings)

print('\n'+'Date Objects')
dates = [datetime.datetime.strptime(date, "%B %d").date() for date in date_strings]
for x in dates:
    x = x.replace(year=2017)
    print(str(x))
print(dates)

print('\n'+'*************************************'+'\n' )
#print('Dates:', date_raw)
#print('Venues:', venues)
#print('Cities:', cities)
#print('')
#print('Date list size', len(date_raw))
#print('Venue list size', len(venues))
#print('City list size', len(cities))

if len(date_strings) == len(venues) == len(cities):
    print('lists equal. Creating Visual Table'+'\n')

    titles = ['date', 'venue', 'city']
    data = [titles] + list(zip(date_strings, venues, cities))
    for i, d in enumerate(data):
        line = '|'.join(str(x).ljust(25) for x in d)
        print(line)
        if i == 0:
            print('-' * len(line))

else:
    print('ERROR! Lists NOT equal')

print('\n'+'*************************************'+'\n' )
today = datetime.date.today()
print('Today is: '+ str(today) +'\n')
print('Difference between dates and today')

for x in dates:
    diff = x - today
    print(str(x) +' is ' + str(diff.days) + ' days')

