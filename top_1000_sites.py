#!/usr/bin/python
import urllib2
from BeautifulSoup import BeautifulSoup

url = 'http://www.google.com/adplanner/static/top1000/'
source = urllib2.urlopen(url)
soup = BeautifulSoup(source.read())

def clean_number(txt):
	return txt.replace(',','')

# get the column names
columns = soup.find('table',{'width':"100%", 'border':"0", 'cellspacing': "0",
	'cellpadding': "0"}).findAll('th')
headers = [x.text for x in columns]
print '\t'.join(headers)

# get the data
data_table = soup.find('table',{'id':'data-table'})
for row in data_table.findAll('tr'):

	data = row.findAll('td')
	position = data[0].text
	site = data[1].text
	category = data[2].text
	unique_visitors = clean_number(data[3].text)
	reach = data[4].text.replace('%','')
	page_views = clean_number(data[5].text)
	has_advertising = data[6].text

	print '\t'.join([position, site, category, unique_visitors, reach, 
		page_views, has_advertising])
