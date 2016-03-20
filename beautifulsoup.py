from bs4 import BeautifulSoup
import urllib2

urls=[]
ctr=-1
def get_links(url):
	soup=BeautifulSoup(urllib2.urlopen(url))
	for  i in soup.find_all('a',href=True):
		print type(i)
		global ctr
		link=i['href']
		#print link
		if link[:4]=='http':
			#print link
			global urls
			if len(urls)<=25 :
				urls.append(link)
	
	if len(urls)<=25 :
		ctr=ctr+1
		get_links(urls[ctr])
		print len(urls)
	
def test():
	for i in urls:
		print i	


def search(quiery):
	search_terms=quiery.strip().split()

	for link in urls:
		soup=BeautifulSoup(urllib2.urlopen(link).read())
		text=soup.get_text()
		
	

get_links('http://ankitpati.org/')
test()
