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
from lxml import etree
import StringIO
import re
import urllib2



visitedUrl = set()

def crawl(urlToParse, depth,textSearch):
    if (depth == 0):
        return
    if (urlToParse.find("http") != 0):
        return
    if(urlToParse in visitedUrl):
        print 'skip %s' %urlToParse
        return
    visitedUrl.add(urlToParse)

    html = getPage(urlToParse)
    #using lxml to parse html
    parser = etree.HTMLParser()
    tree = etree.parse(StringIO.StringIO(html), parser)
    content = tree.xpath('string()')
    if (re.match(textSearch, content, re.IGNORECASE)):
        print urlToParse
    #Find all links. Note: wee filter anchor that do not have a destination
    links = tree.xpath('//a[@href]')
    for link in links:
        if ('href' in link.attrib):
            crawl(link.attrib['href'], depth -1, textSearch)

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