from src import dbhandler
from datetime import datetime
from src import placeontology
from src.jsonencoder import *
 
def unixtimestampToYMDHMS(timestamp):
    return datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d-%H-%M-%S')

def getWeekday (ymdhms):
    return datetime.strptime(ymdhms,'%Y-%m-%d-%H-%M-%S').strftime('%A')

def getIsWeekend(day):
    if day=="Saturday" or day=="Sunday":
        return "true"
    else:
        return "false"

def timeofday(hour):
    if hour>6 and hour<12:
        return "morning"
    elif hour>=12 and hour<18:
        return "afternoon"
    elif hour>=18:
        return "evening"
    else:
        return "dawn"
 
ont_db = dbhandler.firebase('https://placenessdb.firebaseio.com/ontology/starbucks/')
dat_db = dbhandler.firebase('https://placenessdb.firebaseio.com/data/starbucks/')

ont = placeontology.ontology()
places = dat_db.get_shallow("")

for place in places: 
    #place_instances = dat_db.get_shallow("/"+place+"/instagram/")
    place_instances = dat_db.get("/"+place+"/instagram/")
     
    for place_instance in place_instances: 
        try:
            #data = dat_db.get("/" + place + "/instagram/"+place_instance+"/time/")
            data = place_instances [place_instance]['time']
        except:
            data = place_instances [place_instance]['created_time']
     
            timestamp = data
            ymdhms = unixtimestampToYMDHMS(timestamp)
             
            year = int(ymdhms.split('-')[0])
            month = int(ymdhms.split('-')[1])
            day = int(ymdhms.split('-')[2])
            hour = int(ymdhms.split('-')[3])
            minute = int(ymdhms.split('-')[4])
            second = int(ymdhms.split('-')[5])
            weekday = getWeekday(ymdhms)
            isWeekend = getIsWeekend(weekday)
            tod = timeofday(hour)
            
            values_time = [timestamp, year, month, day, hour, minute, second, weekday, isWeekend, tod]
            json_time = encodeJson(ont.time,values_time)
            
            print place, place_instance, json_time
            dat_db.put("/"+place+"/instagram/"+place_instance+"/time", json_time)
            #ont_db.put("/"+place+"/instagram/"+place_instance+"/time", json_time)
    
