# -*- coding: utf-8 -*-

from src import dbhandler
from src import cognitiveAPI
from src.jsonencoder import *
from konlpy.tag import Hannanum
from krprint import krprint
import operator



dat_db = dbhandler.firebase('https://placenessdb.firebaseio.com/ontology/')
districts = dat_db.get_shallow("/")

for district in districts:
    if district != "youngsan":
        continue
    try:
        places = dat_db.get_shallow("/"+district+"/")
    except:
        print "error 1"
        
    
    activities = []
    dwellers = []
    whats = []
    whens = []
    withs = []    
    count = 0
    activity_list_str = "먹,만나,맛집,냠냠,구경,식사,쇼핑,만남,떠나,과제,기차,한잔,파티,먹방,안주,나들이,버스,데이트,레스토랑,모임,아이쇼핑,외출,여유,외식,드라이브,여행,음주,시험,투어,휴식,망년회,생파,수업,휴가,러닝,힐링,맛스타그램,먹스타그램,혼밥,송년회,공부,소풍,먹부림,지름,뷰티,득템,캠핑,회식,럽스타그램,travel,주말데이트,중간고사,고향,스터디,자소서,처묵처묵,가족여행,산책,취미,토크,독서,상봉,소설,여행스타그램,책스타그램,기말고사,시험기간"
    activity_list = activity_list_str.split(",")
    activity_freq = []
    
    f = open("./data/macro/160726/"+district+".txt", "w")
     
    for place in places:
        try:
            place_instances = dat_db.get("/"+district+"/" + place + "/")
        except:
            print "error 2"
            
        for place_instance in place_instances:
            count+=1
            #print district + ", " + place +", "+ place_instance
            
            instance = place_instances[place_instance]
            
            try:
                _activity = instance['activity']['keywords']
                for op in _activity:
                     if not op in activities:
                        activities.append(op)
            except:
                _activity = ["?"]
            
            try:
                _dweller = instance['dweller']['modified_keywords']
                for op in _dweller:
                     if not op in dwellers:
                        dwellers.append(op)

            except:
                _dweller = ["?"]
            
            try:
                _what = instance['what']['modified_keywords']
                for op in _what:
                     if not op in whats:
                        whats.append(op)

            except:
                _what = ["?"]
            
            try:
                _when = instance['when']['modified_keywords']
                for op in _when:
                     if not op in whens:
                        whens.append(op)

            except:
                _when = ["?"]
            
            try:
                _with = instance['with']['modified_keywords']
                for op in _with:
                     if not op in withs:
                        withs.append(op)

            except:
                _with = ["?"]
                
            
            for p1 in _activity:
                for p2 in _dweller:
                    for p3 in _what:
                        for p4 in _when:
                            for p5 in _with:
                                
                                f.write(p1.encode('utf8') + "," + p2.encode('utf8') + "," \
                                        + p3.encode('utf8') + "," + p4.encode('utf8') + "," \
                                        + p5.encode('utf8') + "\n")
                                
                                
                                #if u'' == p1 and u'여자' == p2 and u'파티' == p3 and u'아침' == p4 and u'가족' == p5:
                                #    print district + ", " + place +", "+ place_instance
                                
                                
    
    
    
    
    for p in activities:
        f.write(p.encode('utf8') + ",")
    f.write("\n")
    for p in dwellers:
        f.write(p.encode('utf8') + ",")
    f.write("\n")
    for p in whats:
        f.write(p.encode('utf8') + ",")
    f.write("\n")
    for p in whens:
        f.write(p.encode('utf8') + ",")
    f.write("\n")
    for p in withs:
        f.write(p.encode('utf8') + ",")
        
    f.close()
    
    #print count
    #asdf = input("asdfasd")
    