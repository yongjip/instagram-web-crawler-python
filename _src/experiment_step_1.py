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
import math
import operator
from konlpy.tag import Hannanum


hannanum = Hannanum()

dat_db = dbhandler.firebase('https://placenessdb.firebaseio.com/data/coex/')

hotspots = dat_db.get_shallow("/")


skiplist = ['addbing', 'agra', 'aquarium', 'artisee', 'bbodomoro', 'bbongsin', 
            'bboorigetta', 'bborigetta', 'cafemamas', 'chogeikooksu', 'dequeens', 
            'dongkyung', 'eightseconds', 'eskimos', 'gogoongsura', 'gongsugan', 
            'gundam', 'hadonggwan', 'hongdaedonburi', 'jayeoneun', 'jayeonun', 
            'kerban', 'kervan', 'kfc', 'lagrillia', 'lottleria', 'menmusha', 
            'ontheboarder', 'pica', 'resaigon', 'sariwon', 'sevensprings', 
            'shayibana', 'sideshow', 'sopreso', 'suisihanpan', 'susihanpan','sweetspace', 
            'tablestar', 'tastingroom', 'terarosa', 'youngpoong']
 
col_names = "hotspotname,num_post,face_total, face_mean,face_std,face_exists_num,face_exists_prob,selfie_num,selfie_prob,h_mean,s_mean,v_mean,h_std,s_std,v_std\n"

f = open("output_step_1.txt","w")
f.write(col_names)

for hotspot in hotspots:
    if not hotspot in skiplist: 
        print hotspot
        posts = dat_db.get("/" + hotspot)
        num_post = float(len(posts))
        num_post_pic_available = 0;
        
        
        face_total = 0
        face_mean = 0;
        face_num = []
        face_std = 0;
        
        face_exists_num = 0;
        face_exists_prob = 0;
        
        selfie_num = 0;
        selfie_prob = 0;
        
        h_total=0;
        s_total=0;
        v_total=0;
        
        h_val=[]
        s_val=[]
        v_val=[]
        
        h_mean=0
        s_mean=0
        v_mean=0
        
        h_std=0
        s_std=0
        v_std=0
        
        word_counts = {}
        noun_counts = {}
        
        for post in posts:
            instance = posts[post]
            
            numface = 0
            if 'numface' in instance:
                numface = instance['numface']
                face_total += numface
                face_num.append(numface)
                
                if (numface>0):
                    face_exists_num+=1
                
            
            if 'isSelfie' in instance:
                if (instance['isSelfie']==True):
                    selfie_num+=1
            
            if 'primary_hsv' in instance:
                num_post_pic_available += 1
                h_total += instance['primary_hsv'][0][0]
                s_total += instance['primary_hsv'][0][1]
                v_total += instance['primary_hsv'][0][2]
                
                h_val.append(instance['primary_hsv'][0][0])
                s_val.append(instance['primary_hsv'][0][1])
                v_val.append(instance['primary_hsv'][0][2]) 
                
            if 'captions' in instance:
                caption = instance['captions'][0][0]
                caption_split = caption.split(' ')
                for word in caption_split:
                    if word in word_counts:
                        word_counts[word]+=1
                    else:
                        word_counts[word]=1
                        
            if 'caption' in instance:
                nouns = hannanum.nouns(instance['caption'])
                for noun in nouns:
                    if noun in noun_counts:
                        noun_counts[noun]+=1
                    else:
                        noun_counts[noun]=1

 
        face_mean = float(face_total)/float(num_post_pic_available);
        
        for numface in face_num:
            face_std+=(numface-face_mean)**2
             
        face_std = math.sqrt(face_std/float(num_post_pic_available))
        
        face_exists_prob = float(face_exists_num)/float(num_post_pic_available)
        selfie_prob = float(selfie_num)/float(num_post_pic_available)
        
         
        h_mean=float(h_total)/float(num_post_pic_available);
        s_mean=float(s_total)/float(num_post_pic_available);
        v_mean=float(v_total)/float(num_post_pic_available);
        
        for i in range (len(h_val)):
            h_std+=(h_val[i]-h_mean)**2
            s_std+=(s_val[i]-s_mean)**2
            v_std+=(v_val[i]-v_mean)**2

        h_std = math.sqrt(h_std/float(num_post_pic_available))
        s_std = math.sqrt(s_std/float(num_post_pic_available))
        v_std = math.sqrt(v_std/float(num_post_pic_available))  
 
 
        "hotspotname,num_post,face_total,face_num, face_mean,face_std,face_exists_num,face_exists_prob,selfie_num,selfie_prob,h_mean,s_mean,v_mean,h_std,s_std,v_std"

        buffer = hotspot+','+str(num_post)+','+str(face_total)+','+ str(face_mean)+','+str(face_std)+','+str(face_exists_num)+','+str(face_exists_prob)+','+str(selfie_num)+','+str(selfie_prob)+','+str(h_mean)+','+str(s_mean)+','+str(v_mean)+','+str(h_std)+','+str(s_std)+','+str(v_std)+'\n'
        f.write(buffer)

 
        buffer = ''
        word_counts_sorted = sorted(word_counts.items(), key=operator.itemgetter(1), reverse =True)
        for word in word_counts_sorted:
            buffer += word[0] + "," + str(word[1])+'\n'
        #print buffer;
        g = open('word_count_'+hotspot+'.txt','w');
        g.write(buffer)
        g.close()
        
        buffer = ''
        noun_counts_sorted = sorted(noun_counts.items(), key=operator.itemgetter(1), reverse =True)
        print noun_counts_sorted
        for noun in noun_counts_sorted:
            buffer += noun[0] + "," + str(noun[1])+'\n'
        print buffer;
        h = open('noun_count_'+hotspot+'.txt','w');
        h.write(buffer.encode('utf-8'))
        h.close()

        
f.close()
    # print hotspot + "," +str(len(posts)) + ","
    
    
