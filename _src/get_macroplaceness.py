# -*- coding: utf-8 -*-

import os
import json
from datetime import datetime
from src import dbhandler
from src import placeontology
from src import cognitiveAPI
from konlpy.tag import Hannanum


from src.jsonencoder import *
 
 
datapath = "./data/macro/coex160621/json/" 
respath = "./data/macro/coex160621/res/"

filenames = os.listdir(datapath)
hannanum = Hannanum()
wordvec = {}
  
for filename in filenames:
    filepath = datapath+filename
    
    f = open(filepath, "r")
    
    print filename
       
    for line in f:
        data = None
        try:
            data = json.loads(line)
        except: 
            print "json load fail"
        
        if data != None:
            try:
                caption = data['caption']
                caption = caption.replace('#', ' ')
            except:
                print "no caption"
         
            nouns = hannanum.nouns(caption)
            
            for noun in nouns:
                try:
                    wordvec[noun] += 1
                except:
                    wordvec[noun] = 1
        

wordvec = sorted(wordvec.items(), key=lambda x: x[1], reverse=True)
f = open(respath + "totalresult.txt", "w")
    
for elem in wordvec:
    try: 
        f.write(elem[0].encode('utf8') + "\t" + str(elem[1]) + "\n")
    except:
        print "file write fail"
        
f.close()
         