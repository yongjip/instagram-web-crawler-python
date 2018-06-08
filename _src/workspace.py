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

for place in places:
    print place
    
    posts = dat_db.get('/experiment/'+ place)
    
    mintimestamp = 9999999999999999
    maxtimestamp = 0
    
    for post in posts:
        imgtotal += 1
        time =  posts[post]['date']
        imgurl = posts[post]['display_src']

        urllib.urlretrieve (imgurl, "temp.jpg")
        img = cv2.imread("./temp.jpg")

        if not img is None:
            imgsuccess += 1
        
        if time < mintimestamp:
            mintimestamp = time
        elif time > maxtimestamp:
            maxtimestamp = time
        
        print float(imgsuccess)/float(imgtotal)
         
    tot += len(posts)
    
    print "\t min: " + str(mintimestamp)
    print "\t max: " + str(maxtimestamp)
    
print "imgsuccess: " + str(imgsuccess)





