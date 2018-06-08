from datetime import datetime

def unixtimestampToYMDHMS(timestamp):
    return datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d-%H-%M-%S')

def getWeekday (ymdhms):
    return datetime.strptime(ymdhms,'%Y-%m-%d-%H-%M-%S').strftime('%A')

def getIsWeekend(day):
    if day=="Saturday" or day=="Sunday":
        return "weekend"
    else:
        return "weekday"

def timeofday(hour):
    if hour>6 and hour<12:
        return "morning"
    elif hour>=12 and hour<18:
        return "afternoon"
    elif hour>=18:
        return "evening"
    else:
        return "dawn"
    
def getSeason(month):
    if month>11 or month <=2:
        return "winter"
    elif month > 2 and month <=5:
        return "spring"
    elif month > 5 and month <=8:
        return "summer"
    elif month > 8 and month <=11:
        return "autumn"

def monthString(month):
    if month ==1:
        return "January"
    elif month ==2:
        return "February"
    elif month ==3:
        return "March"
    elif month ==4:
        return "April"
    elif month ==5:
        return "May"
    elif month ==6:
        return "June"
    elif month ==7:
        return "July"
    elif month ==8:
        return "August"
    elif month ==9:
        return "September"
    elif month ==10:
        return "October"
    elif month ==11:
        return "November"
    elif month ==12:
        return "December"
    

def get_time_analysis_keywords(timestamp):
    res = []
     
    ymdhms = unixtimestampToYMDHMS(timestamp)
    
    year = int(ymdhms.split('-')[0])
    month = int(ymdhms.split('-')[1])
    day = int(ymdhms.split('-')[2])
    hour = int(ymdhms.split('-')[3])
    #minute = int(ymdhms.split('-')[4])
    #second = int(ymdhms.split('-')[5])
    tod = timeofday(hour)
    season = getSeason(month)
    weekday = getWeekday(ymdhms)
    isWeekend = getIsWeekend(weekday)

    #res.append(month)
    #res.append(year)

    res.append(weekday.lower())
    #res.append(weekday.lower())
    #res.append(isWeekend)
    #res.append(hour)
    #res.append(tod)
    #res.append(monthString(month).lower())
    #res.append(season.lower())

    return res 


def get_time_analysis_keywords_json(timestamp):
    res = {}
     
    ymdhms = unixtimestampToYMDHMS(timestamp)
    
    year = int(ymdhms.split('-')[0])
    month = int(ymdhms.split('-')[1])
    day = int(ymdhms.split('-')[2])
    hour = int(ymdhms.split('-')[3])
    #minute = int(ymdhms.split('-')[4])
    #second = int(ymdhms.split('-')[5])
    tod = timeofday(hour)
    season = getSeason(month)
    weekday = getWeekday(ymdhms)
    isWeekend = getIsWeekend(weekday)

    #res.append(month)
    #res.append(year)

    res['dayOfWeek'] = weekday.lower()
    res['timeOfDay'] = tod
    res['timeOfYear'] = season
    
    #res.append(weekday.lower())
    #res.append(isWeekend)
    #res.append(hour)
    #res.append(tod)
    #res.append(monthString(month).lower())
    #res.append(season.lower())

    return res 

def get_year(timestamp):     
    ymdhms = unixtimestampToYMDHMS(timestamp)
    
    year = int(ymdhms.split('-')[0])
    month = int(ymdhms.split('-')[1])
    day = int(ymdhms.split('-')[2])
    hour = int(ymdhms.split('-')[3])
    minute = int(ymdhms.split('-')[4])
    second = int(ymdhms.split('-')[5])
    tod = timeofday(hour)
    season = getSeason(month)
    weekday = getWeekday(ymdhms)
    isWeekend = getIsWeekend(weekday) 

    return year

def get_hour(timestamp):     
    ymdhms = unixtimestampToYMDHMS(timestamp)
    
    year = int(ymdhms.split('-')[0])
    month = int(ymdhms.split('-')[1])
    day = int(ymdhms.split('-')[2])
    hour = int(ymdhms.split('-')[3])
    minute = int(ymdhms.split('-')[4])
    second = int(ymdhms.split('-')[5])
    tod = timeofday(hour)
    season = getSeason(month)
    weekday = getWeekday(ymdhms)
    isWeekend = getIsWeekend(weekday) 

    return hour

def get_weekday(timestamp):     
    ymdhms = unixtimestampToYMDHMS(timestamp)
    
    year = int(ymdhms.split('-')[0])
    month = int(ymdhms.split('-')[1])
    day = int(ymdhms.split('-')[2])
    hour = int(ymdhms.split('-')[3])
    minute = int(ymdhms.split('-')[4])
    second = int(ymdhms.split('-')[5])
    tod = timeofday(hour)
    season = getSeason(month)
    weekday = getWeekday(ymdhms)
    isWeekend = getIsWeekend(weekday) 

    return weekday

def get_time_analysis_res(timestamp):
    res = {'weekday':"", "timeofday":"","season":"","isHoliday":False}
     
    ymdhms = unixtimestampToYMDHMS(timestamp)
    
    year = int(ymdhms.split('-')[0])
    day = int(ymdhms.split('-')[2])
    hour = int(ymdhms.split('-')[3])
    #minute = int(ymdhms.split('-')[4])
    #second = int(ymdhms.split('-')[5])
    tod = timeofday(hour)

    
    month = int(ymdhms.split('-')[1])
    
    weekday = getWeekday(ymdhms)
    isWeekend = getIsWeekend(weekday)

    season = getSeason(month)
    #print ymdhms
    
    res['weekday'] = weekday
    res['season'] = season
    res['isHoliday'] = "json['isHoliday']"
    res['timeofday'] = tod
    res['datetime'] = ymdhms

    return res 
    


    