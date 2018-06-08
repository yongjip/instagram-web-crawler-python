import os
import json
from datetime import datetime
from src import dbhandler
from src import placeontology
from src import cognitiveAPI

from src.jsonencoder import *
 

def unixtimestampToYMDHMS(timestamp):
    return datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d-%H-%M-%S')

def getWeekday (ymdhms):
    return datetime.strptime(ymdhms,'%Y-%m-%d-%H-%M-%S').strftime('%A')

datapath = "./data/Seoul mall/res/" 
filenames = os.listdir(datapath)
 
ont = placeontology.ontology()
 
ont_db = dbhandler.firebase('https://placenessdb.firebaseio.com/ontology/')
dat_db = dbhandler.firebase('https://placenessdb.firebaseio.com/data/')

for filename in filenames:
    filepath = datapath+filename
    
    f = open(filepath, "r")
    
    district_name = filename.split("_")[0]
     
    for line in f:
        data = json.loads(line)
  
        #place name
        place_name = filename.split("_")[1].split(".")[0]
        #post id
        post_id = data['id']

        #raw data
        try:        
            dat_db.put(district_name+"/" + place_name + "/" +post_id +"/", json.dumps(data))
            print district_name, place_name, post_id
        except:
            pass

'''
        #meta data        
        metadata = {"source":"instagram",\
            "url":data['link'], \
            "img_url": data['images'], \
            "profile_img_url": data['user']['profile_pic_url']} 
 
        #time
        timestamp = data['created_time']
        ymdhms = unixtimestampToYMDHMS(timestamp)
        year = int(ymdhms.split('-')[0])
        month = int(ymdhms.split('-')[1])
        day = int(ymdhms.split('-')[2])
        hour = int(ymdhms.split('-')[3])
        minute = int(ymdhms.split('-')[4])
        second = int(ymdhms.split('-')[5])
        weekday = getWeekday(ymdhms)
  
        values_time = [timestamp, year, month, day, hour, minute, second, weekday]
        json_time = encodeJson(ont.time,values_time)
        
        #print district_name, place_name, post_id
        ont_db.put_when_timestamp(district_name, place_name, post_id, json_time)
        ont_db.put_metadata(district_name, place_name, post_id, json.dumps(metadata))
        
        img_res = json.dumps(cognitiveAPI.requestAPI(metadata['profile_img_url']))
        
        profile_img_res = json.dumps(cognitiveAPI.requestAPI(metadata['img_url']))
        
        ont_db.put_imageAnalysis(district_name, place_name, post_id, img_res)
        ont_db.put_profileAnalysis(district_name, place_name, post_id, profile_img_res)
'''