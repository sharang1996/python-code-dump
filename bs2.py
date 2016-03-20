from bs4 import BeautifulSoup
import urllib2
import re

url = urllib2.urlopen("http://www.python.org")
content = url.read()
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True):
    if re.findall('group', a['href']):
        print "Found the URL:", a['href']
