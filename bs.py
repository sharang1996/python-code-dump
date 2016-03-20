from bs4 import BeautifulSoup
import urllib2
import os
    
#url="some link"
#content = urllib2.urlopen(url).read()
search_term1="red"
search_term2="green"

os.chdir("/home/sharang/search.py/test")
file1=open("/home/sharang/search.py/test/"+os.listdir("/home/sharang/search.py/test")[1],"r").read()
file2=open("/home/sharang/search.py/test/"+os.listdir("/home/sharang/search.py/test")[2],"r").read()
file3=open("/home/sharang/search.py/test/"+os.listdir("/home/sharang/search.py/test")[3],"r").read()
file4=open("/home/sharang/search.py/test/"+os.listdir("/home/sharang/search.py/test")[4],"r").read()

list=[file1,file2,file3,file4]
for file in list:
	soup=BeautifulSoup(file)
	text=soup.get_text()
	if text.find(search_term1) != -1 and text.find(search_term2) != -1 :
		print "found"
		
	
	
	
	

"""  
TagLinks=soup.find_all('a',href=True) #this gives the links with the tags...
    
links=[]  #this will have only links which can be sent get requests...essentially it can be sent recursively..
    
for link in TagLinks:
    links.append(link.get("href"))
        
for link in links:
    url=link
    #c = urllib2.urlopen(url).read()
    #soup = BeautifulSoup(c)
    #text = soup.get_text()
    #print text
    print url
"""
