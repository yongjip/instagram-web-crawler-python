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
posts = dat_db.get('/experiment/ipark')
tot = 0


#activityname = ["traveling", "social", "art&culture"]
activityname = ["childcare", "social", "art&culture"]

for aa in activityname:
    res ={}
     
          
    for post in posts:
        activities= []
        
        time =  posts[post]['date']
    
        #print posts[post]
    
         
        #urllib.urlretrieve (imgurl, "temp.jpg")
        #img = cv2.imread("./temp.jpg")
    
        #if not img is None:
        #    imgsuccess += 1
         
        
        year = analyze_time.get_year(time)
        hour = analyze_time.get_hour(time)
        weekday  = analyze_time.get_weekday(time)
        
        text_word_dict = read_csv.get_text_dict()
        
        if year==2016:
        
            for wordbag in text_word_dict:
                for word in text_word_dict[wordbag]:
                    if (word.decode('utf-8') in posts[post]['caption']):
                        if not wordbag in activities:
                            activities.append(wordbag)
            #print activities
        
            #asdf = raw_input("Asdfsadf")
        
            for activity in activities:
                if activity == aa:    
                    if str(hour) in res:
                        res[str(hour)] += 1
                    else:
                        res[str(hour)] = 1
                    
                    
                
                         
                        
    for h in sorted(res):
        print h + "," +aa+','+str(res[h])