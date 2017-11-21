# Author: mania@kaist.ac.kr
# Crawling instagram web from given location id
# todo (sskim): iteration, multi-threading

#-*- coding: utf-8 -*-

import urllib
import json
import sys
import sys
from src import dbhandler
from src import imagehandler
from bs4 import BeautifulSoup

prev_max_id = None;

def iter_webcrawl(locationid, max_id):
    global prev_max_id

    if (max_id==None or max==""):
        url = "https://www.instagram.com/explore/locations/"+locationid+"/" 
    else:
        url = "https://www.instagram.com/explore/locations/"+locationid+"/" + "?max_id="+max_id
    
    try: 
        html = urllib.urlopen(url).read()
    except:
        return;
       
    print "url: ", url

    try:
        soup = BeautifulSoup(html, "html.parser") 
        data = soup.find_all("script", { "type" : "text/javascript" })
    except:
        print "Error: page error"
        return;
    
    if data==None:
        print "Error: no data found"
        return;
    
    scripts = ""
    
    for _data in data:
        if "window._sharedData" in str(_data):
             scripts = str(_data)
        
    try:               
        json_text =  scripts.split('window._sharedData =')[1].split(";</script>")[0]
    except: 
        return;

    try:
        json_data = json.loads(json_text)['entry_data']['LocationsPage'][0]['location']['media']['nodes']
    except: 
        return;

    res_tot={}

    #print json_data

    if json_data == None or len(json_data) == 0:
        print "Crawler: No data found. Possibly end of data"
        return (None, None);

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
            res['id']= json_instance['id']
        except:
            print "id MISSING"

        try:
            res['date']= json_instance['date']
        except:
            print "date MISSING"

        try:
            res['code']= json_instance['code']
        except:
            print "code MISSING"

        try:
            res['owner']= json_instance['owner']
        except:
            print "owner MISSING"

        try:
            res['display_src']= json_instance['display_src']
        except:
            print "display_src MISSING"

        try:
            res['caption']= json_instance['caption']
        except:
            print "caption MISSING"

        try:
            res['comments']= json_instance['comments']
        except:
            print "comments MISSING"

        try:
            res['likes']= json_instance['likes']
        except:
            print "likes MISSING"


        res_tot[res['id']] = res
        last_id = res['id']

    if prev_max_id == res['id']:
        return (None, None)
    else:
        prev_max_id == res['id']
        
    return (res_tot, res['id']) #return json and max_id


def crawl_single_locationid(output, locationid, maxid):
    #print locationid
    print maxid
    
    result, maxid = iter_webcrawl(locationid, maxid)

    if (output=="print"):
        print result
        print maxid

    elif (output=="firebase"):
        #print "firebase"
        dat_db = dbhandler.firebase('https://placenessdb3.firebaseio.com/')
        try:
            if (locationid == ''):
                print "Error: location ID null!"
            else:
                dat_db.patch('locationdata/'+locationid +'/' , json.dumps(result))
        except:
            print "Error: DB write error"

        if result != None:
            for post in result:
                #print result[post]
                imagehandler.upload(result[post]["display_src"], str(locationid), result[post]["id"])
        else:
            return None

    return maxid
         
def main(argv):
    if (len(argv) < 2):
        if (len(argv) != 0):
            print "Error: not enough arguments \n"
        
        print "Usage:"
        print "\t python instagram_webcrawl_by_locationid.py <output_type> <location_id> <max_id>"
        print "\t python instagram_webcrawl_by_locationid.py print 254687352 1474635062204921374"
        
        sys.exit(2)

    max_id = None

    if (len(argv) == 3):
        max_id = argv[2]

    if (argv[0]=="print"):
        max_id = crawl_single_locationid("print", argv[1], max_id);

        while(max_id != none):
            max_id = crawl_single_locationid("print", argv[1], max_id);

        print "end of iteration"


    elif (argv[0]=="firebase"):
        print "qwer"
        
    elif (argv[0]=="aws"):
        print "asdf"

if __name__ == "__main__":
    main(sys.argv[1:])
    
    
         
        
        
        
