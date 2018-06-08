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

dat_db = dbhandler.firebase('https://placenessdb.firebaseio.com/experiment2/')

def crawl_by_locatinid(locationid, max_id=None, ret=[]):
    if (max_id==None or max_id==""):
        url = "https://www.instagram.com/explore/locations/"+locationid+"/"
    else:
        url = "https://www.instagram.com/explore/locations/"+locationid+"/" + "?max_id="+max_id
    try:
        html = urllib.urlopen(url).read()
    except:
        return ret
       
    print "url: ", url 
          
    soup = BeautifulSoup(html) 
    data = soup.findAll("script", { "type" : "text/javascript" }) 
    
    try:
        json_text =  '{'+(str(data[4]).split('"media": {')[1].split(', "top_posts":')[0])
        json_data = json.loads(json_text)['nodes']
    except: 
        return ret 
     

    res ={}
    for json_instance in json_data:
        res ={}
          
        res['code']= "json['code']"
        res['owner']= "json['owner']"
        res['comments']= "json['comments']"
        res['caption']= "json['caption']"
        res['likes']= "json['likes']"
        res['date']= "json['date']"
        res['id']= ""
        res['display_src']= "json['display_src']"
        
        try:
            res['code']= json_instance['code']
            res['owner']= json_instance['owner']
            res['date']= json_instance['date']
            res['id']= json_instance['id']
            if 'display_src' in res.keys():
                res['display_src']= json_instance['display_src']
            if 'caption' in res.keys():
                res['caption']= json_instance['caption']
            if 'comments' in res.keys():
                res['comments']= json_instance['comments']
            if 'likes' in res.keys():
                res['likes']= json_instance['likes']
        
        except:
            print "Missing value"  
        
        ret.append(res);
 

    if not 'id' in res.keys():
        return ret
     
    
    next_url = "<a href='http://socialcomputing.kaist.ac.kr:6705/?locationid="+locationid+"&max_id="+str(res['id']+"'>"+"http://socialcomputing.kaist.ac.kr:6705/?locationid="+locationid+"&max_id="+str(res['id'])+"</a>")
    
    if len(ret) >100:
        write_post(locationid, ret)
        return crawl_by_locatinid(locationid, str(res['id']), [])
    else:
        return crawl_by_locatinid(locationid, str(res['id']), ret)


def write_post(locationid, postlist):    
    uploaddata = {}
    
    for post in postlist:
        uploaddata[post['id']] = post
    
    #print uploaddata
    try:
        dat_db.patch("/" + locationid+ "/", json.dumps(uploaddata))
        print("DB write successful")
    except:
        print("DB write error")

f  = open("starbucks_links.txt","r")
location_list = []

for line in f:
    id = line.split("/")[5]
    location_list.append(id)


distance = "750"
token = '2102054277.a8877cd.4e351957bbcd458db4b40fb6424d69df'

location_list = ['249569478']

for lid in location_list:
    print lid
    postlist = crawl_by_locatinid(lid) 
    write_post(lid, postlist)

    
            
        


    
    
    
    