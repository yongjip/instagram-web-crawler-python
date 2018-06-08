from src import dbhandler
from src import cognitiveAPI
from src.jsonencoder import *
import os
 
filenames = os.listdir("./data/hs_starbucks_revision/")
dat_db = dbhandler.firebase('https://placenessdb.firebaseio.com/data/starbucks/')

for filename in filenames:
    f = open ("./data/hs_starbucks_revision/"+filename, "r")
    data = json.load(f)
    campus = data['campus']
    
    place = filename.split(".")[0]
    
    for elem in campus:
        place_instance = elem['key']
        activity_dict = elem['activity']
        
        if any(activity_dict) :
            res = {}
            for key in activity_dict:
                for k in key:
                    res[k] = key[k]
            #print type (res)
            print "/" + place + "/instagram/"+place_instance+"/activity_tf_rev"
            #print type(activity_dict)
            try:
                dat_db.put("/" + place + "/instagram/"+place_instance+"/activity_tf_rev", json.dumps(res))
            except:
                pass
        else:
            print "\t no keywords found"
        
