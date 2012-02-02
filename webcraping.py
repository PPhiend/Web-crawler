#-------------------------------------------------------------------------------
# Name:        webcraping
# Purpose:     given a url seed, webcraper can crawl through all links on the
#              page and scan deep for the given level
#
# Author:      week1 excercise in 50apps
#
# Created:     31/01/2012
# Copyright:   (c) Information 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import sys
from BeautifulSoup import BeautifulSoup
import re
import urllib2



visitedUrl = set()

def crawl(urlToParse, depth,textSearch):
    if (depth == 0):
        return
    if (urlToParse.find('html') != 0):
        return
    if(urlToParse in visitedUrl):
        print 'skip %s' %urlToParse
        return
    visitedUrl.add(urlToParse)

    html = getPage(urlToParse)
    soup = BeautifulSoup(html)

    #Find all links. Note: wee filter anchor that do not have a destination
    links = soup.findAll('a')
    for link in links:
        crawl(link['href'], depth - 1, textSearch)
    if text in soup:
        print ("Found " + urlToParse)


def getPage(url):
    try:
        print url
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        return response.read()
    #when 403 error
    except urllib2.HTTPError, error:
        print "ERROR: ", error.read()
    except:
        raise
if __name__ == '__main__':
    #commandline parameters handling
    if (len(sys.argv) != 4):
        print " Usage: python webcraping.py depth url search_text"
        sys.exit
    depth = int(sys.argv[1])
    url = sys.argv[2]
    searchText = sys.argv[3]
    #searchText = []
    #if len(sys.argv) >=4:
     #   searchText = sys.argv[3:]
    crawl(url, depth, searchText)
    print "Done"