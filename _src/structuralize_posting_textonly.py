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


import read_csv
import image_analysis
import analyze_time

def write_post(district,res):
    try:
        dat_db = dbhandler.firebase('https://placenessdb2.firebaseio.com/'+ sys.argv[1])
        dat_db.patch("/" + district + "/"+ res['id'], json.dumps(res))
        print("DB write successful")
    except:
        print("DB write error")

text_word_dict = read_csv.get_text_dict(); 
#img_word_dict = read_csv.get_img_dict();

if len(sys.argv) ==2:
    dat_db = dbhandler.firebase('https://placenessdb.firebaseio.com/'+ sys.argv[1])

    districts = dat_db.get_shallow('/')
     
    for district in districts:
        hotspots = dat_db.get('/'+district+'/')
        
        print '\t' + district
        for hotspot in hotspots:
            print '\t' + hotspot
    
            res = {'text_keywords':[], 'img_keywords':[], 'time_keywords':[], 'id':hotspot}
            data = hotspots[hotspot]
             
            for wordbag in text_word_dict:
                 for word in text_word_dict[wordbag]:
                    if (word.decode('utf-8') in data['caption']):                
                        if not wordbag in res['text_keywords']:
                            res['text_keywords'].append(wordbag)

            '''
            img_res =image_analysis.get_image_analysis_res(data['display_src'])
     
            if img_res != False : 
                for wordbag in img_word_dict:
                     for word in img_word_dict[wordbag]:
                        if (word.decode('utf-8') in img_res['captions'][0][0]):                
                            if not wordbag in res['img_keywords']:
                                res['img_keywords'].append(wordbag) 
            
                res['img_analysis'] = img_res
            '''
            time_res = analyze_time.get_time_analysis_res(data['date'])
            
            res['time_keywords'] = time_res 
            write_post(district, res)
 
if len(sys.argv) ==3:
    dat_db = dbhandler.firebase('https://placenessdb.firebaseio.com/'+ sys.argv[1])
    district = sys.argv[2]
    hotspots = dat_db.get('/'+district+'/')
    
    print district
    for hotspot in hotspots:
        print '\t' + hotspot

        res = {'text_keywords':[], 'img_keywords':[], 'time_keywords':[], 'id':hotspot}
        data = hotspots[hotspot]
        
        for wordbag in text_word_dict:
             for word in text_word_dict[wordbag]:
                if (word.decode('utf-8') in data['caption']):                
                    if not wordbag in res['text_keywords']:
                        res['text_keywords'].append(wordbag)
        '''
        img_res =image_analysis.get_image_analysis_res(data['display_src'])
 
        if img_res != False : 
            for wordbag in img_word_dict:
                 for word in img_word_dict[wordbag]:
                    if (word.decode('utf-8') in img_res['captions'][0][0]):                
                        if not wordbag in res['img_keywords']:
                            res['img_keywords'].append(wordbag) 
        
            res['img_analysis'] = img_res
        '''
        time_res = analyze_time.get_time_analysis_res(data['date'])
        
        res['time_keywords'] = time_res 
        write_post(district, res) 