# -*- coding: utf-8 -*-

from src import dbhandler
from src import placeontology
from src.jsonencoder import *
import json


ont_db = dbhandler.firebase('https://placenessdb.firebaseio.com/ontology/')

district_name = "IFC_Mall"
place_name = "Starbucks"
post_id = "1004038919362882936"
metadata = {"source":"instagram",\
            "url":"https://www.instagram.com/p/3vyl_hqkMn/", \
            "profile_img_url": "https://scontent.cdninstagram.com/t51.2885-19/s150x150/12317957_143603502668427_1089213051_a.jpg"} 

ont_db.put_dweller(district_name, place_name, post_id, ["맛집", "IFC Mall", "스타벅"])
ont_db.put_with(district_name, place_name, post_id, ["여자친구", "장모님"])
ont_db.put_when(district_name, place_name, post_id, ["오늘", "휴일", "아침"])
ont_db.put_what(district_name, place_name, post_id, ["커피","케이크", "홍차"])
ont_db.put_activity(district_name, place_name, post_id, ["상견례"])
ont_db.put_opinion(district_name, place_name, post_id, ["정갈하다", "고급스럽다"])
 
ont_db.put_when_timestamp(district_name, place_name, post_id, json.dumps({"timestampjson":"timejson"}))
ont_db.put_imageAnalysis(district_name, place_name, post_id, json.dumps({"imagekeyword":"imageeimad"}))
ont_db.put_profileAnalysis(district_name, place_name, post_id, json.dumps({"profilejson":"profilejson"}))
ont_db.put_metadata(district_name, place_name, post_id, json.dumps(metadata))
 
