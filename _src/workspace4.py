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
places = dat_db.get_shallow('/experiment/')
tot = 0

imgsuccess = 0
imgtotal = 0

filename_prefix = "experiment_170105_4_"

for place in places:
    print place
    
    posts = dat_db.get('/experiment/'+ place)
    
    mintimestamp = 9999999999999999
    maxtimestamp = 0
    
    f = open (filename_prefix+place+".txt", "w")
    
    for post in posts:
        activities= []
        time = []
        
        imgtotal += 1
        time =  posts[post]['date']
        imgurl = posts[post]['display_src']

        #urllib.urlretrieve (imgurl, "temp.jpg")
        #img = cv2.imread("./temp.jpg")

        #if not img is None:
        #    imgsuccess += 1
        
        if time < mintimestamp:
            mintimestamp = time
        elif time > maxtimestamp:
            maxtimestamp = time
        
        #print float(imgsuccess)/float(imgtotal)
        
        text_word_dict = read_csv.get_text_dict()
        
        for wordbag in text_word_dict:
            for word in text_word_dict[wordbag]:
                if (word.decode('utf-8') in posts[post]['caption']):
                    if not wordbag in activities:
                        activities.append(wordbag)
                     
        #print activities

        time = (analyze_time.get_time_analysis_keywords(time))
        
        #print time
         
        #cognitiveAPI.requestAPI(metadata['profile_img_url'])
        
        
         
        buf = ''

        for t in time:
            buf += str(t) + ","
        
        for activity in activities:            
            print buf + str(activity) 
            f.write(buf + str(activity) + "_" + imgurl + '\n')

        
        
    f.close() 
         
    tot += len(posts)
    
    print "\t min: " + str(mintimestamp)
    print "\t max: " + str(maxtimestamp)
    


fl = [filename_prefix+'coex.txt',
filename_prefix+'ifc.txt',
filename_prefix+'ipark.txt',
filename_prefix+'townsquare.txt']



for fn in fl:
    f = open(fn, "r")
    
    res = {}
    
    for line in f:
        
        st = line.strip().split('_')[0]
        imgurl = line.strip().split('_')[1]
        
        st = st.replace(',','-')
        
        if st=='weekday-evening-autumn-social':
            print imgurl
            
            
            


