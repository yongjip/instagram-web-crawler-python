from src import dbhandler


db = dbhandler.firebase('https://placenessdb.firebaseio.com/data/starbucks/')

placeids = db.get_shallow("/")
for placeid in placeids:
   place_instances = db.get_shallow("/"+placeid+"/instagram/")

   for place_instance in place_instances:
       data = db.get("/"+placeid+"/instagram/"+place_instance+"/location/name")
       print placeid, data
       break
   
        
        
        