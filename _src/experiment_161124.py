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


####### 161124 (a) 
if (1==1122):
    text_word_dict = read_csv.get_text_dict() 
    
    dat_db = dbhandler.firebase('https://placenessdb.firebaseio.com/')
    posts = dat_db.get('/experiment/ipark')
    
    f = open("experiment_161128_a.txt","w")
    
    for post in posts:
        res = []
        
        data = posts[post] 
        
        for wordbag in text_word_dict:
            for word in text_word_dict[wordbag]:
                if (word.decode('utf-8') in data['caption']):                
                    if not word in res:
                        res.append(word)
            
        f.write(str(res) + '\n')
        print(str(res))
        
    f.close();

####### 161124 (b) 
if (1==1234):
    text_word_dict = read_csv.get_text_dict() 
    
    dat_db = dbhandler.firebase('https://placenessdb.firebaseio.com/')
    posts = dat_db.get('/experiment/coex')
    
    f = open("experiment_161124_b.txt","w")
    
    for post in posts:
        res = {}
        
        data = posts[post] 
        
        for wordbag in text_word_dict:
            for word in text_word_dict[wordbag]:
                if (word.decode('utf-8') in data['caption']):                
                    if not wordbag in res:
                        res[wordbag] = 1
                    else:
                        res[wordbag] += 1
            
        f.write(str(res) + '\n')
        print(str(res))
        
    f.close();
    
     
    
####### 161124 (c) 
if (1==111):
    text_word_dict = read_csv.get_text_dict() 
    
    dat_db = dbhandler.firebase('https://placenessdb.firebaseio.com/')
    posts = dat_db.get('/experiment/ipark')
    
    f = open("experiment_161128_c.txt","w")
    
    mapping = []
    for wordbag in text_word_dict:
        mapping.append(wordbag); 
    
    for post in posts:
        res = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
        data = posts[post] 
        
        for wordbag in text_word_dict:
            for word in text_word_dict[wordbag]:
                if (word.decode('utf-8') in data['caption']):                
                     res[mapping.index(wordbag)] = 1
             
        f.write(str(res) + '\n')
        print(str(res))
        
    f.close();
    
     
####### 161124 (d) same as (b), counts in vector form 
if (1==11212):
    text_word_dict = read_csv.get_text_dict() 
    
    dat_db = dbhandler.firebase('https://placenessdb.firebaseio.com/')
    posts = dat_db.get('/experiment/ipark')
    
    f = open("experiment_161128_d.txt","w")
    
    mapping = []
    for wordbag in text_word_dict:
        mapping.append(wordbag); 
    
    for post in posts:
        res = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
        data = posts[post] 
        
        for wordbag in text_word_dict:
            for word in text_word_dict[wordbag]:
                if (word.decode('utf-8') in data['caption']):          
                     res[mapping.index(wordbag)] += 1
                      
        f.write(str(res) + '\n')
        print(str(res))
        
    f.close();

    
if (1==12312):
    text_word_dict = read_csv.get_text_dict()
    a = ''
    for elem in text_word_dict:
        a+=elem + '\n'
    print a[:-1]


if (1==112312):
    f = open("experiment_161124_a.txt","r")
    for line in f:
        b = ast.literal_eval(line)
        c = ''
        for word in b:
            c += word
        print c 

if (1==112):
    out_c = open("output_c.txt","r")
    res_c = open("experiment_161124_c.txt","r")
    
    act_str = 'chores,fashion&beauty,outdoor,business,dining,housing,social,entertainment,legal,religion,childcare,traveling,relaxation,health,education,art&culture'
    act_list = act_str.split(',')
    
    index_array = []
    output_array = []
    
    for line in out_c:
        index_array.append(int(line.strip()))
    for line in res_c:
        output_array.append(line.strip().split(','))
         
        
    for i in range (len(index_array)):
        if (index_array[i] == 2):
            print output_array[i]


if (1==1212):
    out_c = open("output_c.txt","r")
    res_c = open("experiment_161124_c.txt","r")

    index_array = []
    output_array = []
    
    for line in out_c:
        index_array.append(int(line.strip()))
    for line in res_c:
        output_array.append(line.strip().split(','))

    act_str = 'chores,fashion&beauty,outdoor,business,dining,housing,social,entertainment,legal,religion,childcare,traveling,relaxation,health,education,art&culture'
    act_list = act_str.split(',')
    
    for k in range (16):
        print ("k=" + str(k))
        counts = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  

        for i in range (len(output_array)):
            if index_array[i] == k+1:       
                for j in range (len(output_array[i])):
                    counts[j] += int(output_array[i][j])
            
        for i in range (len(act_list)):
            print '\t' + act_list[i] + ": "  + str(counts[i])
   
if (1==1):
    out_c = open("output_c.txt","r")
    res_c = open("experiment_161124_c.txt","r")
   
    index_array = []
    output_array = []
    
    for line in out_c:
        index_array.append(int(line.strip()))
    for line in res_c:
        output_array.append(line.strip().split(','))

    act_str = 'chores,fashion&beauty,outdoor,business,dining,housing,social,entertainment,legal,religion,childcare,traveling,relaxation,health,education,art&culture'
    act_list = act_str.split(',')
    
    for k in range (16):
        print ("k=" + str(k+1))
        counts = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  

        for i in range (len(output_array)):
            if index_array[i] == k+1:       
                for j in range (len(output_array[i])):
                    counts[j] += int(output_array[i][j])
            
        total = 0;
        for c in counts:
            total+= c;
        
        normal_count = []
        
        for c in counts:
            normal_count.append(float(c)/total)
        
        for i in range (len(act_list)):
            if normal_count[i] > 0.10:
                print '\t' + act_list[i] + ": "  + str(normal_count[i])

            
if (1==1121):
    text_feature_vector = read_csv.get_text_dict_feature_vector() 
    len_text_feature_vector = len(text_feature_vector)
    out_c = open("output_161128_d.txt","r")
    keyword_file = open("experiment_161128_a.txt","r")

    f = open("dat_train_161128_d.txt","w")
 
    print len_text_feature_vector 

    for line in keyword_file:
        label = out_c.readline().strip()
        
        zero_vector = [0] * len_text_feature_vector

        b = ast.literal_eval(line)
        for word in b:
            temp_idx = text_feature_vector.index(word)
            zero_vector[temp_idx] += 1
            
        f.write(label + "," + str(zero_vector)[1:-1] + '\n')
    
    f.close()

            

        
    
    
           






    