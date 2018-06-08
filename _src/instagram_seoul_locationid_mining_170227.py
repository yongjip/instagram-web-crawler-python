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
 
 
def web_request(lat, lng):  
    token = '2102054277.a8877cd.4e351957bbcd458db4b40fb6424d69df'
    distance = 100
    url = 'https://api.instagram.com/v1/locations/search?lat='+str(lat)+'&lng='+str(lng)+'&access_token='+token+'&distance='+str(distance)
    #print url
    
    html = urllib.urlopen(url).read()  
    json_obj = json.loads(html)
    
    #print (json.dumps(json_obj)); 
    write_to_db(json_obj['data'])  

def write_to_db(json_obj): 
    dat_db = dbhandler.firebase('https://placenessdb2.firebaseio.com/') 
    
    for elem in json_obj:
        #print elem
        #print "experiment2/"+elem['id']
        try:
            dat_db.put("experiment2/"+elem['id'], json.dumps(elem))
        except:
            print "upload error"

        
  

def iter_latlng():
    #start_pos = (37.706, 126.759)
    #start_pos = (37.6885, 127.0315)
    #start_pos = (37.6635, 127.1115)
    #start_pos = (37.501, 127.144)
    #start_pos = (37.6217, 126.8236)
    start_pos = (37.6177, 126.9606)

    end_pos = (37.4895, 127.1281)
    
    cnt = 0
    cnt_tot = 19323

    cur_pos_lat = start_pos[0] 
    
    while cur_pos_lat > end_pos[0]:
        cur_pos_lon = start_pos[1]

        while cur_pos_lon < end_pos[1]:
            cur_pos_lon += 0.001
            cnt += 1
            
            print str(cur_pos_lat) + ", " + str(cur_pos_lon)
            
            
            print "Iter " + str(cnt) + " of " + str(cnt_tot) + " (" + str(cnt/cnt_tot) + "%)"
            
            web_request(cur_pos_lat, cur_pos_lon)
            
            
        cur_pos_lat -= 0.001
        
    print cnt
iter_latlng();