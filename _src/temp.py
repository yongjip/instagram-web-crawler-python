
# -*- coding: utf-8 -*-

from src import dbhandler
from src import cognitiveAPI
from src.jsonencoder import *
from konlpy.tag import Hannanum
from krprint import krprint
import operator


dat_db = dbhandler.firebase('https://placenessdb.firebaseio.com/data/')
districts = dat_db.get_shallow("/")

res = []

for district in districts:
    try:
        places = dat_db.get_shallow("/"+district+"/")
    
    
        print(district)
            
     
        for place in places:
            print (place)
            
            place_instances = dat_db.get("/"+district+"/" + place + "/")
            
            for place_instance in place_instances:
                try:
                    a = place_instances[place_instance]['owner']['username']
                    if not a in res:
                        res.append(a)
                    #print a
                except: 
                    b = "no username"
    except:
        c = "something wrong"

print (res)
print (len(res))

f = open('usernames.txt','w')
f.write(str(res))
f.close()




'''
import read_csv


text_word_dict = read_csv.get_text_dict(); 

for cat in text_word_dict:
    buf = ''
    for word in text_word_dict[cat]:
        buf += '"' + word + '", '
    print cat + ": " + buf
'''