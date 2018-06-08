from src import dbhandler
import urllib

 
db = dbhandler.firebase('https://placenessdb.firebaseio.com/data/coex')
 
hotspots = db.get_shallow("/") 
 
for hotspot in hotspots:
    print hotspot
    hotspots_instances = db.get("/"+hotspot)
     
    for hotspots_instance in hotspots_instances:
        print "\t" + hotspots_instance 
        hotspots_instance_data = hotspots_instances[hotspots_instance] 
        if "images" in hotspots_instance_data:
            print hotspots_instance_data["images"]
            urllib.urlretrieve (hotspots_instance_data["images"], "/home/cdsn/workspace/placenessdb/data/image161010/"+hotspot+"_"+hotspots_instance+".jpg")
  


'''
############# 0. initialization ############
db = dbhandler.firebase('https://placenessdb.firebaseio.com/data/')

############# 1. fetching place ids ############
macroplaces = db.get_shallow("/") 

############# 2. fetching place instance ids ############
for macroplace in macroplaces:
    #print macroplace
    hotspots = db.get_shallow("/"+macroplace)
    
    for hotspot in hotspots:
        #print "\t" + hotspot
        hotspot_data = db.get("/"+macroplace+"/"+hotspot)
        if "images" in hotspot_data:
            print(hotspot_data["images"])
            a = raw_input("asdfasdfAS");
 '''