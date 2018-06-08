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

dat_db = dbhandler.firebase('https://placenessdb.firebaseio.com/experiment/')

def realtime_instagram(locationid, max_id=None, ret=[]):
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
     
    
    next_url = "<a href='http://socialcomputing.kaist.ac.kr:6705/?locationid="+locationid+"&max_id="+str(res['id']+"'>"+"http://socialcomputing.kaist.ac.kr:6705/?locationid="+locationid+"&max_id="+str(res['id'])+"</a>")
    
    if len(ret) >100:
        write_post(ret)
        return realtime_instagram(locationid, str(res['id']), [])
    else:
        return realtime_instagram(locationid, str(res['id']), ret)


def write_post(postlist):    
    uploaddata = {}
    
    for post in postlist:
        uploaddata[post['id']] = post
    
    #print uploaddata
    try:
        dat_db.patch("/" + latlng[2], json.dumps(uploaddata))
        print("DB write successful")
    except:
        print("DB write error")


#frisbee = '237818231'
#postlist = realtime_instagram(frisbee)
#print postlist
#print len(postlist)

latlng_0 = (37.5254622,126.9254538, 'ifc')
latlng_1 = (37.5171639,126.9009871, 'townsquare')
latlng_2 = (37.5288539,126.961856, 'ipark')
latlng_3 = (37.5130828,127.0555708, 'coex') 

location_list = [latlng_0]
distance = "750"
token = '2102054277.a8877cd.4e351957bbcd458db4b40fb6424d69df'

for location_ in location_list:
    latlng = location_

    url = 'https://api.instagram.com/v1/locations/search?lat='+str(latlng[0])+'&lng='+str(latlng[1])+'&access_token='+token+'&distance='+distance
       
    print url
    
    res = urllib.urlopen(url).read() 
    locations = json.loads(res) 
    
    print locations['data']
     
    
    for loc in locations['data']:
        print loc['id'] + ", " + loc['name']
          
    
        buffer = {}
        locationid = loc['id']
        postlist = realtime_instagram(locationid)
        
        write_post(postlist)

    
            
        


    
    
    
    