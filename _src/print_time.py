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
 
timestamp = "1418108760"
ymdhms = unixtimestampToYMDHMS(timestamp)
hour = int(ymdhms.split('-')[3])
weekday = getWeekday(ymdhms)


isWeekend = getIsWeekend(weekday)

tod = timeofday(hour)

if (isWeekend):
    print "weekend, " + tod
else:
    print "weekday, " + tod
 
 

