# -*- coding: utf-8 -*-

from src import cognitiveAPI
import urllib
from bs4 import BeautifulSoup
import json
import ast
from pprint import pprint
import dryscrape
from selenium import webdriver
import time
import os
from src import dbhandler
import re
import demo_keyword_extraction as ke

dat_db = dbhandler.firebase('https://placenessdb.firebaseio.com/data/demo/')
ont_db = dbhandler.firebase('https://placenessdb.firebaseio.com/ontology/demo/')


places = dat_db.get("/")

for place in places:
    subplaces = places[place]
    for subplace in subplaces:
        posts = subplaces[subplace]
        for post in posts:
            _dweller = {}
            _with = {}
            _space = {}
            _activity = {}
            _what = {}
            _when = {}

            instance = posts[post]
            caption =  instance['caption']
            comments = instance['comments']
            created_time = instance['created_time']
            images = instance['images']
            
            img_res = cognitiveAPI.requestAPI(images)
            print "tags: " + str(img_res['tags'])
            
            ont_db.put("timesquare/ontheborder/"+post+"/activity/description", json.dumps(img_res['tags']))
            
            try:
                _dweller['gender'] = img_res['faces'][0]['gender']
                _dweller['age'] = img_res['faces'][0]['age']
                _activity['description'] = {"text": img_res['description']['captions'][0]['text']} 
            
            except:
                pass
            
            ont_db.put("timesquare/ontheborder/"+post+"/dweller/", json.dumps(_dweller))
            ont_db.put("timesquare/ontheborder/"+post+"/activity/description", json.dumps(_activity))

            temp = ke.with_analysis(caption)
            
            for elem in temp:
                ont_db.put_with("timesquare", "ontheborder", post, temp)
                
            temp = ke.space_analysis(caption)
            for elem in temp:
                ont_db.put_space("timesquare", "ontheborder", post, temp)

            temp = ke.activity_analysis(caption)
            for elem in temp:
                ont_db.put_activity("timesquare", "ontheborder", post, temp)

            temp = ke.when_analysis(caption)
            for elem in temp:
                ont_db.put_when("timesquare", "ontheborder", post, temp)


            
            
            
            
            
            
            
            
            
            
            
            