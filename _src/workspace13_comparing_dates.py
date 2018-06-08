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

total = 0
delta = 0
hours = {}

for place in places:    
    posts = dat_db.get('/data/coex/'+place)
    print place
    if place!="megabox":
        for post in posts:
            if 'date' in posts[post] and 'created_time' in posts[post]:
                total += 1
                
                
                hour = analyze_time.get_time_analysis_keywords(posts[post]['date'])
                
                if str(hour) in hours:
                    hours[str(hour)] +=1
                else:
                    hours[str(hour)] =1
    
                #print int(posts[post]['date'])-(posts[post]['created_time'])
                #delta += int(posts[post]['date'])-(posts[post]['created_time'])
            
#print total
#print delta

for h in sorted(hours):
    print h + "," +str(hours[h])