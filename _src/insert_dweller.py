from src import dbhandler
from src import cognitiveAPI
from src.jsonencoder import *
import time

ont_db = dbhandler.firebase('https://placenessdb.firebaseio.com/ontology/starbucks/')
dat_db = dbhandler.firebase('https://placenessdb.firebaseio.com/data/starbucks/')
 
places = dat_db.get_shallow("/")

   
for place in places:
    place_instances = dat_db.get_shallow("/"+place+"/instagram/")

    #print place_instances
 
    for place_instance in place_instances: 
        #instance = place_instances[place_instance]
        try:
            data = dat_db.get("/" + place + "/instagram/"+place_instance+"/")
        except:
            continue
        #print data
        
        try:
            prev_val = data['profile_analysis']
            ont_db.put("/" + place + "/instagram/"+place_instance+"/dweller", json.dumps(prev_val))

            print ("skip")
        except:
            
            profile_picture_url = ""
            
            try:       
                profile_picture_url =  data['user']['profile_pic_url']
            except:
                try:
                    profile_picture_url =  data['user']['profile_picture']
                except:
                    continue
            
            print time.ctime(), place, place_instance, profile_picture_url
             
            res = cognitiveAPI.requestAPI(profile_picture_url)
            try:
                dat_db.put("/" + place + "/instagram/"+place_instance+"/profile_analysis", json.dumps(res))
                ont_db.put("/" + place + "/instagram/"+place_instance+"/dweller", json.dumps(res))
            except:
                print "db insert error: ", res