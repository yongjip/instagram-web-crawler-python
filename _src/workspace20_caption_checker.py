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
posts = dat_db.get('/experiment/ipark')
tot = 0
caption_cnt = 0
      
for post in posts:
    tot += 1
    
    caption = posts[post]['caption']
    if len(caption.split(" ")) < 2:
        caption_cnt += 1
                
            
                     
                    
print tot
printndler.firebase: 
print float(caption_cnt)/float(tot)        
