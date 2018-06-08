# -*- coding: utf-8 -*-

import urllib
from bs4 import BeautifulSoup
import json
import ast
from pprint import pprint
import dryscrape
from selenium import webdriver
import time
import os
from src import dbhandler
import sys

url = str(sys.argv[1]) 
print "url: ", url


html = urllib.urlopen(url)
print "html loaded..."
soup = BeautifulSoup(html, "lxml")
data = soup.findAll("script", { "type" : "text/javascript" })
json_text = (str(data[4]).split('"PostPage": [')[1]).split(']}, "qe":')[0]
json_data = json.loads(json_text)['media']        
print "media parsed..."

#caption
#comments
json_data['created_time'] = json_data['date']
#filter # NA
#id
json_data['images'] = json_data['display_src'] 
#likes
json_data['link'] = url
locationid = json_data['location']['id']
 
    
#fixme: tags
#embeded in 'caption'

#fixme: type
#either 'video' or 'image'. cannot be determined from source

json_data['user'] = json_data['owner']

#fixme: user_has_liked
#not available either
 
dat_db = dbhandler.firebase('https://placenessdb.firebaseio.com/data/demo/')
dat_db.put("timesquare"+"/" + "ontheborder" + "/" +json_data['id'] +"/", json.dumps(json_data))
print "done."