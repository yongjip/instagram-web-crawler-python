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


dat_db = dbhandler.firebase('https://placenessdb2.firebaseio.com/')
places = dat_db.get('/experiment2/')

places_cnt = 0

tot = 0
caption_cnt = 0



for place in places:
        
    posts = places[place]
    
    
    places_cnt += 1
    
    
    '''
    for post in posts:
        tot += 1
        
        caption = places[place][post]['caption']
        if len(caption.split(" ")) < 2:
            caption_cnt += 1
    '''
                
            
                     
print places_cnt
                    
#print tot
#rint caption_cnt
#rint float(caption_cnt)/float(tot)        