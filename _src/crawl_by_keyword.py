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

dat_db = dbhandler.firebase('https://placenessdb.firebaseio.com/experiment2/')

def crawl_by_tag(tag, max_id=None, ret=[]):
    if (max_id==None or max_id==""):
        url = "https://www.instagram.com/explore/tags/"+tag+"/"
    else:
        url = "https://www.instagram.com/explore/tags/"+tag+"/" + "?max_id="+max_id
    try:
        html = urllib.urlopen(url).read()
    except:
        return ret
       
    print "url: ", url 
          
    soup = BeautifulSoup(html) 
    data = soup.findAll("script", { "type" : "text/javascript" }) 
    
    try:
        json_text =  '{'+(str(data[4]).split('"media": {')[1].split(', "content_advisory":')[0])
        json_data = json.loads(json_text)['nodes']
    except: 
        return ret

    print("json_data")
    print(json_data)
    print(len(json_data))


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
        res['display_src']= "json['display_src'] "
        
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
     
     
    if len(ret) >100:
        write_post(tag,ret)
        return crawl_by_tag(tag, str(res['id']), [])
    else:
        return crawl_by_tag(tag, str(res['id']), ret)


def write_post(tag,postlist):    
    uploaddata = {}
    
    for post in postlist:
        uploaddata[post['id']] = post
    
    #print uploaddata
    try:
        dat_db.patch("/"+tag.+"/", json.dumps(uploaddata))
        print("DB write successful")
    except:
        print("DB write error")

 
  
tag = "스타벅스";
postlist = crawl_by_tag(tag, "J0HWCiIaQAAAF0HWCiG3wAAAFjwA", [])
write_post(tag,postlist)