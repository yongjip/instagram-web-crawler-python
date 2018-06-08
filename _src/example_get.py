# -*- coding: utf-8 -*-


from src import dbhandler

db = dbhandler.firebase('https://placenessdb.firebaseio.com/ontology/times')


placenames = db.get_shallow("/")
 
_dweller = []
_with = []
_what = []
_activity = []

f = open("placedata_times.txt", "w")


for placename in placenames:
    posts = db.get("/"+placename)
     
    for post in posts:
        print post
        dat = posts[post]
        
        __dweller = "?"
        __with = "?"
        __what = "?"
        __activity = "?"
                                
        try:
            __dweller = dat['dweller']['modified_keywords']
            
            for keyword in __dweller:
                if not keyword in _dweller:
                    _dweller.append(keyword)
        except:
            pass
        try:
            __with = dat['with']['modified_keywords']
            for keyword in __with:
                if not keyword in _with:
                    _with.append(keyword)
        except:
            pass
        try:
            __what = dat['what']['modified_keywords']
            for keyword in __what:
                if not keyword in _what:
                    _what.append(keyword)
        except:
            pass
        try:            
            __activity = dat['activity']['keywords']
            for keyword in __activity:
                if not keyword in _activity:
                    _activity.append(keyword)
        except:
            pass
        
        for d in __dweller:
            for wh in __what:
                for wi in __with:
                    for ac in __activity:
                        b = d+ ","+wh+","+wi+","+ac
                        f.write (b.encode('utf-8') + "\n")
f.close()

g = open("placeattributes_times.txt","w") 
buf = ""    
for elem in _dweller:
    buf += elem + ", "
    #print elem
g.write(buf.encode('utf-8') +"\n")

buf = ""    
for elem in _with:
    buf += elem + ", "
    #print elem
g.write(buf.encode('utf-8') +"\n")

buf = ""    
for elem in _what:
    buf += elem + ", "
    #print elem
g.write(buf.encode('utf-8') +"\n")

buf = ""    
for elem in _activity:
    buf += elem + ", "
    #print elem
g.write(buf.encode('utf-8') +"\n")

g.close()


'''

############# 2. fetching place instance ids ############
for placeid in placeids:
    place_instances = db.get_shallow("/"+placeid+"/instagram/")
    #print place_instances

############# 3. fetching place instances ############
    for place_instance in place_instances:
        data = db.get("/"+placeid+"/instagram/"+place_instance+"/")

'''