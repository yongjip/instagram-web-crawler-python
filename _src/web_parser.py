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

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""
 
datapath = "./data/macro/coex160927/"
filenames = os.listdir(datapath)
#dat_db = dbhandler.firebase('https://placenessdb.firebaseio.com/data/starbucks/')

'''
for foldername in foldernames:
    folderpath =datapath + foldername + "/" 
    filenames = os.listdir(folderpath)
'''

for filename in filenames:
    filepath = datapath + filename
    
    print filepath
            
    file = open(filepath, 'r')
    lat = ""
    lon = ""
    getLocation = False
      
    outputfilepath = datapath + filename.split(".")[0] + ".json" 
     
    print outputfilepath
    
    for line in file:
        urlid = find_between(line, "/p/", "/?taken")
           
        if urlid != "": 
            try:
                url = "https://www.instagram.com/p/"+urlid+"/"
                print "url: ", url
                
                
                html = urllib.urlopen(url)
                 
                soup = BeautifulSoup(html)
                
                data = soup.findAll("script", { "type" : "text/javascript" })
                 
                
                json_text = (str(data[4]).split('"PostPage": [')[1]).split(']}, "qe":')[0]
                json_data = json.loads(json_text)['media']        
                 
                #caption
                #comments
                json_data['created_time'] = json_data['date']
                #filter # NA
                #id
                json_data['images'] = json_data['display_src'] 
                #likes
                json_data['link'] = url
                
                locationid = json_data['location']['id']
                
                #fixme: location
                if lat == "" and getLocation: 
                    dryscrape.start_xvfb()
                    session = dryscrape.Session()
                    session.visit(url)
        
                    locationurl = "https://www.instagram.com/explore/locations/" + locationid + "/"
                    print "location: ", locationurl
                    dryscrape.start_xvfb()
                    session = dryscrape.Session()
                    session.visit(url)
                    response = session.body()
                    response = session.body()
                     
                    soup = BeautifulSoup(response)
         
                    data = soup.findAll(attrs={"property": "place:location:latitude"})
                    print data
                    
                #fixme: tags
                #embeded in 'caption'
                
                #fixme: type
                #either 'video' or 'image'. cannot be determined from source
        
                json_data['user'] = json_data['owner']
                
                #fixme: user_has_liked
                #not available either
                 
                #pprint (json_data)
                 
                outputfile = open(outputfilepath, 'a+')
                outputfile.write(json.dumps(json_data) + "\n")
                outputfile.close()
                
                
            except:
                print "error line: ", line
