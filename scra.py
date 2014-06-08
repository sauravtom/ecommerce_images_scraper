#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2,urllib
from bs4 import BeautifulSoup
import json
import os
import logging
from soupselect import select
import re

scrape_generic(color,item):
    makedir('%s'%item)



def main():
    for i in color:
        for j in item:
            scrape_generic(i,j)


def amazon(url,color):
    print color
    if not os.path.exists('dump/%s'%color):
        os.makedirs('dump/%s'%color)
    
    soup = BeautifulSoup( urllib2.urlopen(url).read() )

    for i in select(soup, 'div.imageBox div'):
        x = str(i.get('style'))
        #m = re.search(r"\[((A-Za-z0-9_)+)\]", x)
        a = re.search('\((.*?)\)',x).group(1)
        img_url = ''.join(a.split(',')[:1])
        name = img_url.split('/')[-1]
        path = "dump/%s/%s"%(color,name)
        urllib.urlretrieve(img_url, path)
        print path
    
    return 0


    for i in soup.find_all('img',{'class' : 'productImage'}):
    #imageBox
    #for i in soup.find_all('div',{'class' : 'imagebox'}):
        try:
            img_url = i.get('src')
            name = img_url.split('/')[-1]
            path = "dump/%s/%s"%(color,name)
            urllib.urlretrieve(img_url, path)
            print path
        except:
            logging.exception('f')
            print 'asdas'
    
    #return 0
    return 0
    #for j in soup.find_all('div',{'class' : 'rsltGrid prod celwidget'} ):
    for j in soup.find_all('div',{'class' : 'imageBox'}):
        dict = {}
        try:
            img_url = j.find('img').get('src')
            name = img_url.split('/')[-1]
            path = "dump/%s/%s"%(color,name)
            urllib.urlretrieve(img_url, path)
            cropped_path = 'crop/'+path
            print path
            '''
            if not os.path.exists(cropped_path):
                os.makedirs(cropped_path)
            os.system('convert -gravity center -crop 110x160+1-12 %s %s'%(path,cropped_path))
            '''
        except:
            print 'error'

def scrape_shirt():
    white = 'http://www.amazon.in/s/ref=lp_1968120031_nr_p_n_size_two_browse-_10?rh=n%3A1571271031%2Cn%3A%211571272031%2Cn%3A1968024031%2Cn%3A1968120031%2Cp_n_size_two_browse-vebin%3A1975332031&bbn=1968120031&ie=UTF8&qid=1402135670&rnid=1974754031'
    black = 'http://www.amazon.in/s/ref=lp_1968120031_nr_p_n_size_two_browse-_1?rh=n%3A1571271031%2Cn%3A%211571272031%2Cn%3A1968024031%2Cn%3A1968120031%2Cp_n_size_two_browse-vebin%3A1975317031&bbn=1968120031&ie=UTF8&qid=1402132870&rnid=1974754031'
    green = 'http://www.amazon.in/s/ref=lp_1968120031_nr_p_n_size_two_browse-_4?rh=n%3A1571271031%2Cn%3A%211571272031%2Cn%3A1968024031%2Cn%3A1968120031%2Cp_n_size_two_browse-vebin%3A1975321031&bbn=1968120031&ie=UTF8&qid=1402137089&rnid=1974754031'
    red = 'http://www.amazon.in/s/ref=lp_1968120031_nr_p_n_size_two_browse-_9?rh=n%3A1571271031%2Cn%3A%211571272031%2Cn%3A1968024031%2Cn%3A1968120031%2Cp_n_size_two_browse-vebin%3A1975329031&bbn=1968120031&ie=UTF8&qid=1402137108&rnid=1974754031'
    blue = 'http://www.amazon.in/s/ref=lp_1968120031_nr_p_n_size_two_browse-_9?rh=n%3A1571271031%2Cn%3A%211571272031%2Cn%3A1968024031%2Cn%3A1968120031%2Cp_n_size_two_browse-vebin%3A1975329031&bbn=1968120031&ie=UTF8&qid=1402137108&rnid=1974754031'
    orange = 'http://www.amazon.in/s/ref=lp_1968120031_nr_p_n_size_two_browse-_6?rh=n%3A1571271031%2Cn%3A%211571272031%2Cn%3A1968024031%2Cn%3A1968120031%2Cp_n_size_two_browse-vebin%3A1975326031&bbn=1968120031&ie=UTF8&qid=1402137144&rnid=1974754031'
    amazon(black,'black')
    amazon(white,'white')
    amazon(green,'green')
    amazon(red,'red')
    amazon(blue,'blue')
    amazon(orange,'orange')

def scrape_shoes():
    shoe_black = 'http://www.amazon.in/s/ref=lp_1983518031_nr_p_n_size_two_browse-_0?rh=n%3A1571283031%2Cn%3A%211571284031%2Cn%3A1983396031%2Cn%3A1983518031%2Cp_n_size_two_browse-vebin%3A2022299031&bbn=1983518031&ie=UTF8&qid=1402227933&rnid=2022042031'
    shoe_white = 'http://www.amazon.in/s/ref=lp_1983518031_nr_p_n_size_two_browse-_2?rh=n%3A1571283031%2Cn%3A%211571284031%2Cn%3A1983396031%2Cn%3A1983518031%2Cp_n_size_two_browse-vebin%3A2022301031&bbn=1983518031&ie=UTF8&qid=1402227972&rnid=2022042031'
    shoe_green = 'http://www.amazon.in/s/ref=lp_1983518031_nr_p_n_size_two_browse-_9?rh=n%3A1571283031%2Cn%3A%211571284031%2Cn%3A1983396031%2Cn%3A1983518031%2Cp_n_size_two_browse-vebin%3A2022309031&bbn=1983518031&ie=UTF8&qid=1402227997&rnid=2022042031'
    shoe_orange ='http://www.amazon.in/s/ref=lp_1983518031_nr_p_n_size_two_browse-_7?rh=n%3A1571283031%2Cn%3A%211571284031%2Cn%3A1983396031%2Cn%3A1983518031%2Cp_n_size_two_browse-vebin%3A2022306031&bbn=1983518031&ie=UTF8&qid=1402228030&rnid=2022042031'
    shoe_red =   'http://www.amazon.in/s/ref=lp_1983518031_nr_p_n_size_two_browse-_5?rh=n%3A1571283031%2Cn%3A%211571284031%2Cn%3A1983396031%2Cn%3A1983518031%2Cp_n_size_two_browse-vebin%3A2022304031&bbn=1983518031&ie=UTF8&qid=1402225500&rnid=2022042031'
    shoe_blue =  'http://www.amazon.in/s/ref=sr_nr_p_n_size_two_browse-_10?rh=n%3A1571283031%2Cn%3A%211571284031%2Cn%3A1983396031%2Cn%3A1983518031%2Cp_n_size_two_browse-vebin%3A2022304031&bbn=1983518031&ie=UTF8&qid=1402228075'
    shoe_grey =  'http://www.amazon.in/s/ref=sr_nr_p_n_size_two_browse-_5?rh=n%3A1571283031%2Cn%3A%211571284031%2Cn%3A1983396031%2Cn%3A1983518031%2Cp_n_size_two_browse-vebin%3A2022300031&bbn=1983518031&ie=UTF8&qid=1402228108'
    amazon(shoe_black,'black')
    amazon(shoe_white,'white')
    amazon(shoe_orange,'orange')
    amazon(shoe_red,'red')
    amazon(shoe_blue,'blue')
    amazon(shoe_green,'green') 
    amazon(shoe_grey,'grey')

def scrape_watch():
    jeans_blue = 'http://www.amazon.in/s/ref=lp_1968076031_nr_p_n_size_two_browse-_2?rh=n%3A1571271031%2Cn%3A%211571272031%2Cn%3A1968024031%2Cn%3A1968076031%2Cp_n_size_two_browse-vebin%3A1975318031&bbn=1968076031&ie=UTF8&qid=1402228973&rnid=1974754031'
    jeans_black ='http://www.amazon.in/s/ref=sr_nr_p_n_size_two_browse-_2?rh=n%3A1571271031%2Cn%3A%211571272031%2Cn%3A1968024031%2Cn%3A1968076031%2Cp_n_size_two_browse-vebin%3A1975317031&bbn=1968076031&ie=UTF8&qid=1402229021'
    jeans_green ='http://www.amazon.in/s/ref=sr_nr_p_n_size_two_browse-_1?rh=n%3A1571271031%2Cn%3A%211571272031%2Cn%3A1968024031%2Cn%3A1968076031%2Cp_n_size_two_browse-vebin%3A1975321031&bbn=1968076031&ie=UTF8&qid=1402229034'
    jeans_gray = 'http://www.amazon.in/s/ref=lp_1968076031_nr_p_n_size_two_browse-_5?rh=n%3A1571271031%2Cn%3A%211571272031%2Cn%3A1968024031%2Cn%3A1968076031%2Cp_n_size_two_browse-vebin%3A1975322031&bbn=1968076031&ie=UTF8&qid=1402229052&rnid=1974754031'
    amazon(jeans_gray,'grey')
    amazon(jeans_green,'green')
    amazon(jeans_black,'black')
    amazon(jeans_blue,'blue')

if __name__ == '__main__':
    watch_black = 'http://www.amazon.in/s/ref=lp_1350387031_nr_p_n_feature_two_brow_0?rh=n%3A1350387031%2Cp_n_feature_two_browse-bin%3A1480923031&bbn=1350387031&ie=UTF8&qid=1402229356&rnid=1480891031'
    watch_white = 'http://www.amazon.in/s/ref=lp_1350387031_nr_p_n_feature_two_brow_2?rh=n%3A1350387031%2Cp_n_feature_two_browse-bin%3A1480938031&bbn=1350387031&ie=UTF8&qid=1402229411&rnid=1480891031'
    watch_red = 'http://www.amazon.in/s/ref=lp_1350387031_nr_p_n_feature_two_brow_5?rh=n%3A1350387031%2Cp_n_feature_two_browse-bin%3A1480935031&bbn=1350387031&ie=UTF8&qid=1402229440&rnid=1480891031'
    watch_orange = 'http://www.amazon.in/s/ref=lp_1350387031_nr_p_n_feature_two_brow_7?rh=n%3A1350387031%2Cp_n_feature_two_browse-bin%3A1480932031&bbn=1350387031&ie=UTF8&qid=1402229466&rnid=1480891031'
    watch_green ='http://www.amazon.in/s/ref=lp_1350387031_nr_p_n_feature_two_brow_11?rh=n%3A1350387031%2Cp_n_feature_two_browse-bin%3A1480927031&bbn=1350387031&ie=UTF8&qid=1402229486&rnid=1480891031'
    watch_blue = 'http://www.amazon.in/s/ref=sr_nr_p_n_feature_two_brow_14?rh=n%3A1350387031%2Cp_n_feature_two_browse-bin%3A1480927031%7C1480934031&bbn=1350387031&ie=UTF8&qid=1402229490&rnid=1480891031'
    amazon(watch_blue,'blue')
    amazon(watch_green,'green')
    amazon(watch_orange,'orange')
    amazon(watch_red,'red')
    amazon(watch_white,'white')
    amazon(watch_black,'black')

    

