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

total = 0
textsuccess = 0 
imgsuccess = 0
textimgsuccess = 0
profilesuccess = 0
 
for place in places:
    print place 
    
    if place=="coex":        
        posts = dat_db.get('/experiment/'+ place)

        for post in posts:
            activities= []
            time = []
            
            total += 1
            '''
            time =  posts[post]['date']
            imgurl = posts[post]['display_src']
            caption = posts[post]['caption']
            '''
            code = posts[post]['code']
            
            if code!=None:
                try:

                    url = "https://www.instagram.com/p/"+code+"/"
                    html = urllib.urlopen(url).read()
                    
                    soup = BeautifulSoup(html) 
                    data = soup.findAll("script", { "type" : "text/javascript" })
    
                    #print str(data[4])
                    #print type(data[4])
                    #json_text =  '{'+(str(data[4]).split('"PostPage": [{')[1].split(', "country_code":')[0])
                    
                    cs =  str(data[4]).split("{")
                    
                    for line in cs: 
                        #print line
                         
                        if "profile_pic_url" in line and "followed_by_viewer" in line:
                            #print line
                            profile_imgurl=  line.split('"profile_pic_url": "')[1].split('.jpg"')[0] + ".jpg"
                            
                            
                            ip_res = cognitiveAPI.pythonSample(profile_imgurl)
                            #print ip_res
                            #print type(ip_res)
                            
                            hashable = '{"profile_image_analysis": ' +ip_res + '}'
                            #print hashable
                            #print type(hashable)
                            
                            print '/experiment/'+place+'/'+post
                            
                            dat_db.patch('/experiment/'+place+'/'+post, hashable)
                except:
                    print 'error at /experiment/'+place+'/'+post
                    
             


print textsuccess
print imgsuccess
print textimgsuccess
print total
        
        
          