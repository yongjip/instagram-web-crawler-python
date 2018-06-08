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


key = "AIzaSyDHcwF80tRk72rL99Fqb7yc8TgGrF7Grpo"
cx = "002251192808668744489:obqpmibjnc4"
query = "%EC%8A%A4%ED%83%80%EB%B2%85%EC%8A%A4"

def get_locations(query, start, ret):
    if (start==1 or start==""):
        url = "https://www.googleapis.com/customsearch/v1?key=AIzaSyDHcwF80tRk72rL99Fqb7yc8TgGrF7Grpo&cx=002251192808668744489:obqpmibjnc4&q="+query+"&start=1"
    else:
        url = "https://www.googleapis.com/customsearch/v1?key=AIzaSyDHcwF80tRk72rL99Fqb7yc8TgGrF7Grpo&cx=002251192808668744489:obqpmibjnc4&q="+query+"&start=" + str(start)
    try:
        html = urllib.urlopen(url).read()
    except:
        return ret
    try:
        json_data = json.loads(html)
        nextPagestartIndex = json_data['queries']['nextPage'][0]['startIndex']
    except:
        return ret
    
    print nextPagestartIndex
    
    for item in json_data['items']:
        ret.append(item['link'])
        print item['link']
    
    get_locations(query, nextPagestartIndex, ret)

f= open("starbucks_links.txt","w")
buffer = get_locations(query, 1, [])
print buffer
f.write(str(buffer))
f.close()