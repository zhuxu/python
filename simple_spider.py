import time
import re
import urlparse
import urllib
from bs4 import BeautifulSoup

# Get user input from command line
#url = raw_input("Please input a url :")            
url = 'http://'+ raw_input("Please input a url :")
#url = "http://www.ahau.edu.cn/"
#url = "http://www.taobao.com/"
#url = "http://www.ifeng.com/"
#url = "http://www.douban.com/"
#url = "http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-828-operating-system-engineering-fall-2006/lecture-notes/"

urls = [url]        # stack of urls to srcape
visited = [url]     # historic record of urls


while len(urls) > 0:
    try:
        htmltext = urllib.urlopen(urls[0]).read()
    except:
        print urls[0]
    soup = BeautifulSoup(htmltext)
    
    urls.pop(0)
    #print len(urls)
    print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+'  >> start'

    #print soup.findAll('a',href=True) # just for test
    for tag in soup.findAll('a',href=True):
        tag['href'] = urlparse.urljoin(url,tag['href'])
        print tag['href']
        #if tag['href'][-1] == 'f':  # find pdf file
            #print tag['href']
        #if url in tag['href'] and tag['href'] not in visited:
            #urls.append(tag['href'])
            #visited.append(tag['href'])

    print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+'  >> end'
#print visited
