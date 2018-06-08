#-*- coding: utf-8 -*-

import urllib
import json
from bs4 import BeautifulSoup
import sys
from src import dbhandler



def realtime_instagram(locationid, max_id):
    if (max_id==None):
        url = "https://www.instagram.com/explore/locations/"+locationid+"/" # + "?max_id="1362778012957782134"
    else:
        url = "https://www.instagram.com/explore/locations/"+locationid+"/" + "?max_id="+max_id
    
    try: 
        html = urllib.urlopen(url).read()
    except:
        return;
       
    print "url: ", url 
          
    soup = BeautifulSoup(html) 
    data = soup.findAll("script", { "type" : "text/javascript" })
 
    try:   
        json_text =  str(data[4]).split('window._sharedData =')[1].split(";</script>")[0]
    except: 
        return; 
    
    
    #print json_text
    try:
        json_data = json.loads(json_text)['entry_data']['LocationsPage'][0]['location']['media']['nodes']
    except: 
        return;
    
    res_tot={}
    

    for json_instance in json_data:
        res ={}
                 
        res['code']= ''
        res['owner']= ''
        res['comments']= ''
        res['caption']= ''
        res['likes']= ''
        res['date']= ''
        res['id']= ''
        res['display_src']= ''
        
        try:
            res['code']= json_instance['code']
            res['owner']= json_instance['owner']
            res['display_src']= json_instance['display_src']
            res['caption']= json_instance['caption']
            res['date']= json_instance['date']
            res['id']= json_instance['id']
            res['likes']= json_instance['likes']
            res['comments']= json_instance['comments']
        except:
            print "VALUE MISSING"  
             
        print res
        res_tot[res['id']] = res
    
    
    try:
        dat_db.put('experiment4/'+locationid +'/' , json.dumps(res_tot))
    except:
        print "upload error"

    
    #return next_url +'<br>\n' + str(json_data) + '\n' + table_txt;


def iter_locationid():
    locationids = dat_db.get('/experiment2/')
    
    found_last_id = False;
    last_id = '1033025300'
    
    for locationid in locationids:
        print locationid
        
        if found_last_id == False:
            if locationid == last_id:
                found_last_id = True
            else: 
                continue
        
        realtime_instagram(locationid, None)

dat_db = dbhandler.firebase('https://placenessdb2.firebaseio.com/')
iter_locationid()
         
        
        
        
