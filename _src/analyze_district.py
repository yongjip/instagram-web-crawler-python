# Author: mania@kaist.ac.kr

# -*- coding: utf-8 -*-

from src import dbhandler
from src import cognitiveAPI
from src.jsonencoder import *
from konlpy.tag import Hannanum
from krprint import krprint
import operator


dat_db = dbhandler.firebase('https://placenessdb.firebaseio.com/data/')
districts = dat_db.get_shallow("/")
hannanum = Hannanum()
wordvec = {}

for district in districts:
    try:
        places = dat_db.get_shallow("/"+district+"/")
    except:
        print "error 1"

    wordvec[district] = {}
     
    for place in places:
        
        try:
            place_instances = dat_db.get("/"+district+"/" + place + "/")
        except:
            print "error 2"
            
        for place_instance in place_instances:
            print district + ", " + place +", "+ place_instance
            
            instance = place_instances[place_instance]
            try:
                caption = instance['caption']
                caption = caption.replace('#', ' ')
            except:
                pass #print "no caption"
            
            nouns = hannanum.nouns(caption)
            
            for noun in nouns:
                try:
                    wordvec[district][noun] += 1
                except:
                    wordvec[district][noun] = 1
            
            tags = None
            try:
                tags = instance['image_analysis']['tags']
            except:
                pass #print "no image_analysis/tags at " + district + ", " + place +", "+ place_instance
                
            if tags != None:
                for tag in tags:
                    try:
                        wordvec[district][tag['name']] += 1
                    except:
                        wordvec[district][tag['name']] = 1 
            
            '''
            desc_tags = None
            
            try:
                desc_tags = instance['image_analysis']['description']['tags']
            except:
                print "no image_analysis/description/tags at " + district + ", " + place +", "+ place_instance
            
            if desc_tags != None:       
                for tag in desc_tags:
                    try:
                        wordvec[district][tag] += 1
                    except:
                        wordvec[district][tag] = 1 
            '''
            
    wordvec[district] = sorted(wordvec[district].items(), key=lambda x: x[1], reverse=True)
    
    f = open("./data/macro/res/"+district+".txt", "w")
    
    for elem in wordvec[district]:
        #print elem[0].encode('utf8') + "\t" + str(elem[1])
        f.write(elem[0].encode('utf8') + "\t" + str(elem[1]) + "\n")    
        #print krprint().pformat(wordvec[district][place])
        
    f.close()
         