#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import os
import logging
from soupselect import select
import re

color = 'black,white,red,blue,green,orange'.split(',')
item = 'watch,shoes,tshirt,jeans,sunglasses'.split(',')

def makedir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def scrape_generic(color,item,page=1):
    makedir('%s/%s'%(item,color))
    url = 'http://www.amazon.in/s/ref=nb_sb_noss/276-9260373-9046819?url=search-alias%%3Daps&field-keywords=%s+%s&page=%s'%(color,item,page)
    soup = BeautifulSoup( urllib2.urlopen(url).read() )
    for i in soup.find_all('img',{'class' : 'productImage'}):
        try:
            img_url = i.get('src')
            name = img_url.split('/')[-1]
            path = "%s/%s/%s"%(item,color,name)
            urllib.urlretrieve(img_url, path)
            print path
        except:
            logging.exception('Scraping error')
            print 'Unable to scrape url %s'%(url)

    if page > 5: return 0
    return scrape_generic(color,item,page+1)

def main():
    for i in color:
        for j in item:
            scrape_generic(i,j)


if __name__ == '__main__':
    main()
    #scrape_generic('black','shoes')

    

