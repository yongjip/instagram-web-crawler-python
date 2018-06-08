#-*- coding: utf-8 -*-

# Author: mania@kaist.ac.kr
# Requesting Instagram API for available locationid of given GPS location
# todo (sskim): multi-threading  

from src import dbhandler
import urllib
import json
import sys
import getopt

api_key = ""; #instagram api key with public access (non-sandbox)

def web_request(token, lat, lng, distance):    
    url = 'https://api.instagram.com/v1/locations/search?lat='+str(lat)+'&lng='+str(lng)+'&access_token='+token+'&distance='+str(distance) 
    
    html = urllib.urlopen(url).read()  
    json_obj = json.loads(html)
    
    return json_obj['data'] 
        
def iter_latlng(output, start_lat, start_lng, end_lat, end_lng, distance):
    start_pos = (float(start_lat), float(start_lng))
    end_pos = (float(end_lat), float(end_lng))
    
    cnt = 0 
    cur_pos_lat = start_pos[0] 
    
    while cur_pos_lat > end_pos[0]: 
        cur_pos_lon = start_pos[1]
        while cur_pos_lon < end_pos[1]: 
            cur_pos_lon += 0.001
            cnt += 1
            print "#### Iter " + str(cnt) + ": (" + str(cur_pos_lat) + ", " + str(cur_pos_lon) + ") ####"
            res = web_request(api_key, cur_pos_lat, cur_pos_lon, distance)
            
            if (output == "print"):
                print res

            ########################################################################
            # store location id here: ex) db.patch(locationid, json.dumps(result)) #
            ########################################################################
                        
        cur_pos_lat -= 0.001
    
    print "End of iteration."
 
def main(argv):
    if (len(argv) < 6):
        if (len(argv) !=0):
            print "Error: not enough arguments \n"
            
        print "Usage:"
        print "\t python instagram_locationid_request.py <output_type> <start_lat> <start_lng> <end_lat> <end_lng> <distance>"
        print '\t python instagram_locationid_request.py print 37.614061 126.793019 37.479233 127.126362 100'
        print '\t python instagram_locationid_request.py firebase placenessdb2 experiment2 37.614061 126.793019 37.479233 127.126362 100'

        sys.exit(2)
        
    if (argv[0]=="print"):
        print "Printing results on terminal."
        iter_latlng("print", argv[1], argv[2], argv[3], argv[4], argv[5]) 
        print "Done."
     
    else:
        print "Error: output type not specified \n"
        print "Usage:"
        print "\t python instagram_locationid_request.py <output_type> <start_lat> <start_lng> <end_lat> <end_lng> <distance>"
        print '\t python instagram_locationid_request.py print 37.614061 126.793019 37.479233 127.126362 100'
        print '\t python instagram_locationid_request.py firebase placenessdb2 experiment2 37.614061 126.793019 37.479233 127.126362 100'


if __name__ == "__main__":
   main(sys.argv[1:]) 
    