from src import dbhandler
from src import cognitiveAPI
from src.jsonencoder import *
import time



image_url = "https://scontent.cdninstagram.com/t51.2885-15/e35/14566623_766840470085502_1354374527559139328_n.jpg?ig_cache_key=MTM1MzAwNDQxMDI1MDM5NDMxNw%3D%3D.2";
image_res = json.dumps(cognitiveAPI.requestAPI(image_url));

print image_res

 

'''
dat_db = dbhandler.firebase('https://placenessdb.firebaseio.com/data/')
districts = dat_db.get_shallow("/")

for district in districts:
    places = dat_db.get_shallow("/"+district+"/")
    
    for place in places:
        place_instances =  dat_db.get("/"+district+"/"+place)

        for place_instance in place_instances:
            instance = place_instances[place_instance]
            images = instance['images']
            img_res = json.dumps(cognitiveAPI.requestAPI(images))
            
            print district, place, place_instance
 
            try:
               	print("hello"); 
                #dat_db.put_imageAnalysis(district, place, place_instance, img_res)
            except:
                print("error at:", district, place, place_instance)

             
'''