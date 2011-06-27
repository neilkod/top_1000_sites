#!/usr/bin/python
import urllib2
from BeautifulSoup import BeautifulSoup

url = 'http://www.google.com/adplanner/static/top1000/'
source = urllib2.urlopen(url)
soup = BeautifulSoup(source.read())

# get the column names
columns = soup.find('table',{'width':"100%", 'border':"0", 'cellspacing': "0",
	'cellpadding': "0"}).findAll('th')
headers = [x.text for x in columns]
print '\t'.join(headers)

# get the data
data_table = soup.find('table',{'id':'data-table'})
for row in data_table.findAll('tr'):
	data = []
	[data.append(x.text) for x in row.findAll('td')]
	print '\t'.join(data)
