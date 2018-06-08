# -*- coding: utf-8 -*-

from src import dbhandler
from src import cognitiveAPI
from src.jsonencoder import *
import numpy as np
import subprocess
import cv2
import os  
import urllib
import json
from bs4 import BeautifulSoup
from flask import Flask
from flask import request
from src import dbhandler
import sys
import ast

import read_csv
import image_analysis
import analyze_time
import time


dat_db = dbhandler.firebase('https://placenessdb.firebaseio.com/')
places = dat_db.get_shallow('/data/coex')
tot = 0


activityname = ["childcare", "education", "social", "fashion&beauty", "traveling", "business", "art&culture"]


coex_c = {}
coex_e = {}
coex_s = {}

ipark_c = {}
ipark_e = {}
ipark_s = {}

for place in places:
    print place
     
    posts = dat_db.get('/data/coex/'+ place)
     
    for post in posts:
        activities= []
        
        
        if 'date' in posts[post] and 'caption' in posts[post]:
            time =  posts[post]['date']

            #print posts[post]

             
            #urllib.urlretrieve (imgurl, "temp.jpg")
            #img = cv2.imread("./temp.jpg")
    
            #if not img is None:
            #    imgsuccess += 1
             
            
            hour = analyze_time.get_time_analysis_keywords(time)
            
            text_word_dict = read_csv.get_text_dict()
            
            for wordbag in text_word_dict:
                for word in text_word_dict[wordbag]:
                    if (word.decode('utf-8') in posts[post]['caption']):
                        if not wordbag in activities:
                            activities.append(wordbag)
            #print activities
    
            #asdf = raw_input("Asdfsadf")

            for activity in activities:
                if activity in activityname:
                    if activity=="childcare":
                        if str(hour) in coex_c:
                            coex_c[str(hour)] +=1
                        else:
                            coex_c[str(hour)] =1
                    elif activity=="education":
                        if str(hour) in coex_e:
                            coex_e[str(hour)] +=1
                        else:
                            coex_e[str(hour)] =1
                    elif activity=="social":
                        if str(hour) in coex_s:
                            coex_s[str(hour)] +=1
                        else:
                            coex_s[str(hour)] =1
                 
                     
                    
for h in sorted(coex_c):
    print h + "," +str(coex_c[h])
print ""
for h in sorted(coex_e):
    print h + "," +str(coex_e[h])
print ""
for h in sorted(coex_s):
    print h + "," +str(coex_s[h])
print "" 