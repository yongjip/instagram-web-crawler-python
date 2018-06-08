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

filename_prefix = "experiment_170107_2_"


#timedict = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0,'13':0,'14':0,'15':0,'16':0,'17':0,'18':0,'19':0,'20':0,'21':0,'22':0,'23':0}
timedict = {}

for place in places:
    print place
    
    if place=="coex":
        posts = dat_db.get('/experiment/'+ place)
        
        mintimestamp = 9999999999999999
        maxtimestamp = 0
        
        f = open (filename_prefix+place+".txt", "w")
        
        for post in posts:
            activities= []
            time = []
            
            imgtotal += 1
            try:
                time =  posts[post]['date']
                        
                
                time = (analyze_time.get_time_analysis_keywords(time))
                text_word_dict = read_csv.get_text_dict()
                
                
                for wordbag in text_word_dict:
                    for word in text_word_dict[wordbag]:
                        if (word.decode('utf-8') in posts[post]['caption']):
                            if not wordbag in activities:
                                activities.append(wordbag)

                 
                for activity in activities:
                    if str(str(time[0])+ ' ' + activity)  in timedict:
                        timedict[str(str(time[0])+ ' ' + activity)] +=1
                    else:
                        timedict[str(str(time[0])+ ' ' + activity)] =1
            except:
                print '/experiment/'+ place + '/' + post
                        
        f.close() 
             
        tot += len(posts)
        
print tot
for d in sorted(timedict):
    print d + " " + str(timedict[d]) 
    
    
    
    