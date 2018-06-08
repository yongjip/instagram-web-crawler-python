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
                        
                        if gender=="Male":
                            if str(hour) in male:
                                male[str(hour)] += 1
                            else:
                                male[str(hour)] = 1
                        if gender=="Female":
                            if str(hour) in female:
                                female[str(hour)] += 1
                            else:
                                female[str(hour)] = 1 

print profiletot
print maletot


for d in sorted(male):
    print str(d) + "," + str(male[d])
    
for d in sorted(female):
    print str(d) + "," + str(female[d])