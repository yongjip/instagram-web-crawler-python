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
  
for filename in filenames:
    wordvec = {}
    filepath = datapath+filename
    
    if filepath.endswith(".json"):    
        print filename

        f = open(filepath, "r")
           
        for line in f:
            data = None
            try:
                data = json.loads(line)
            except: 
                pass
        
            if data != None:
                try:
                    caption = data['caption']
                    caption = caption.replace('#', ' ')
                except:
                    pass
             
                nouns = hannanum.nouns(caption)
                
                for noun in nouns:
                    try:
                        wordvec[noun] += 1
                    except:
                        wordvec[noun] = 1
                
        wordvec = sorted(wordvec.items(), key=lambda x: x[1], reverse=True)
        
        f = open(respath + filename.split(".")[0]+".txt", "w")
        
        for elem in wordvec:
            try: 
                f.write(elem[0].encode('utf8') + "\t" + str(elem[1]) + "\n")
            except:
                pass    
                
        f.close()
                 