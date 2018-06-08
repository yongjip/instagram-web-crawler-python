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

agetot = 0
profiletot = 0
maletot = 0

#age= {'teen':0, '20s':0,'30s':0,'40s':0,'50s':0, 'above60':0}

activitylist = {}

for place in places:
    print place
    
    if place =="ipark" :
        posts = dat_db.get('/experiment/'+ place)
         
        for post in posts:
            activities= []
            time =  posts[post]['date']

            if 'profile_image_analysis' in posts[post]: 
                if 'faces' in posts[post]['profile_image_analysis']:
                    faces = posts[post]['profile_image_analysis']['faces']
                    for face in faces:
                        
                        aaa = face['age']
                        gender = face['gender']
                        
                        hour = analyze_time.get_time_analysis_keywords(time)
                          
                        text_word_dict = read_csv.get_text_dict()
                        
                        for wordbag in text_word_dict:
                            for word in text_word_dict[wordbag]:
                                if (word.decode('utf-8') in posts[post]['caption']):
                                    if not wordbag in activities:
                                        activities.append(wordbag)
                        if aaa >=50 and aaa <60:
                            profiletot += 1

                            for activity in activities:
                                if activity in activitylist:
                                    activitylist[activity] += 1
                                else:
                                    activitylist[activity] = 1
                                                                 

print profiletot
print maletot
 
for d in sorted(activitylist):
    print d + " " + str(activitylist[d])
    activitylist[d] = float(activitylist[d])/float(profiletot)

buf =''
     
for d in sorted(activitylist):
    buf += str(activitylist[d]) + " "

print buf
