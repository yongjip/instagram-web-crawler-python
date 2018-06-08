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

activity_cnt={}

filename_prefix = "experiment_170107_3_"

for place in places:
    print place
    
    if place =="ifc":
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
     
            
            text_word_dict = read_csv.get_text_dict()
            
            for wordbag in text_word_dict:
                for word in text_word_dict[wordbag]:
                    if (word.decode('utf-8') in posts[post]['caption']):
                        if not wordbag in activities:
                            activities.append(wordbag)


            for activity in activities:
                if activity in activity_cnt:
                    activity_cnt[activity] += 1
                else:
                    activity_cnt[activity] = 1

for activity in activity_cnt:
    print activity + " " + str(activity_cnt[activity])