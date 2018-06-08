#-*- coding: utf-8 -*-

from src import dbhandler
from src import cognitiveAPI
from src.jsonencoder import *
import numpy as np
import subprocess
import cv2
import os  
import urllib
import json

import read_csv
import analyze_time


db_src = dbhandler.firebase('https://placenessdb.firebaseio.com/')
db_dst = dbhandler.firebase('https://placenessdb2.firebaseio.com/')

print "1"

posts_src = db_src.get('/experiment/coex')

print "2"


text_word_dict = read_csv.get_text_dict()

found_last_location = True

for post in posts_src: 
    

    
    if found_last_location == False:
        if post == 1251287892337610234:
            continue
        else:
            found_last_location = True
        
    print post

    if 'date' in posts_src[post]:
        activity_node = {}
        visitor_node ={}
        time_node = {}
        
        if 'profile_image_analysis' in posts_src[post] and 'faces' in posts_src[post]['profile_image_analysis']:
            visitor_node = {'age':posts_src[post]['profile_image_analysis']['faces'][0]['age'], 'gender':posts_src[post]['profile_image_analysis']['faces'][0]['gender']}
             
 
        time_node = analyze_time.get_time_analysis_keywords_json(posts_src[post]['date'])
         
        
        for wordbag in text_word_dict:
            for word in text_word_dict[wordbag]:
                if (word.decode('utf-8') in posts_src[post]['caption']):
                    if not wordbag in activity_node:
                        activity_node[wordbag] = 1
                    else:
                        activity_node[wordbag] += 1
        
        print visitor_node
        print time_node     
        print activity_node  
        
        res_dict = {'visitor': visitor_node, 'time': time_node, 'activity': activity_node}
        
        
        print res_dict
        
        db_dst.put('/experiment3/ipark/' + post, json.dumps(res_dict))