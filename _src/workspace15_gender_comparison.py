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

male= {}
female={}

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
                        
                        
                        age = face['age']
                        gender = face['gender']
                        
                        hour = analyze_time.get_time_analysis_keywords(time)
                          
                        text_word_dict = read_csv.get_text_dict()
                        
                        for wordbag in text_word_dict:
                            for word in text_word_dict[wordbag]:
                                if (word.decode('utf-8') in posts[post]['caption']):
                                    if not wordbag in activities:
                                        activities.append(wordbag)
                        
                
                        for activity in activities:
                            if activity =="business" or activity =="education" or activity =="legal":
                                a = "work"
                            elif activity =="housing" or activity =="relaxation" or activity =="religion" or activity =="chores" or activity =="dining" or activity =="childcare" or activity=="health":
                                a = "living"
                            elif activity =="fashion&beauty" or activity =="outdoor" or activity =="traveling" or activity =="social" or activity =="entertainment" or activity =="art&culture":
                                a = "leisure"
                            
                            profiletot+=1

                            if gender=='Male':
                                maletot+=1

                                if a in male:
                                    male[a] +=1
                                else:
                                    male[a] =1
                            else:
                                if a in female:
                                    female[a] +=1
                                else:
                                    female[a] =1


print profiletot
print maletot


'''
for d in male:
    male[d] = float(male[d])/float(maletot)

for d in female:
    female[d] = float(female[d])/float(profiletot-maletot)
    
buf = "Gender Work Living Leisure \n"
buf += "Male "
for d in sorted(male):
    buf += str(male[d]) + " "
buf += '\n'

buf += "Female "
for d in sorted(female):
    buf +=  str(female[d]) + " "
buf += '\n'

print buf
'''