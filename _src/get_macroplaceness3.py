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
filenames = os.listdir(datapath)
hannanum = Hannanum()
wordvec = {}
  
for filename in filenames:
    filepath = datapath+filename
    
    if filepath.endswith(".json"):    
        f = open(filepath, "r")
        print filename
        
        linenum = 0;

        for line in f:
            print linenum
            
            data = None
            
            try:
                data = json.loads(line)
            except: 
                pass

            if data != None:
                try:
                    caption = data['caption']
                    caption = caption.replace('#', ' ')
                    #print caption
                except:
                    print "no caption"
             
                nouns = hannanum.nouns(caption)
                
                for noun in nouns:
                    try:
                        wordvec[noun] += 1
                    except:
                        wordvec[noun] = 1
                linenum += 1
            
        #wordvec = sorted(wordvec.items(), key=lambda x: x[1], reverse=True)
    
f = open(datapath+"result3.txt", "w")

print len(wordvec)
for elem in wordvec:
    try: 
        f.write(elem[0].encode('utf8') + "\t" + str(elem[1]) + "\n")
    except:
        pass         
f.close()
             