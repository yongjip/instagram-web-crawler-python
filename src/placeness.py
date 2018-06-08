import numpy as np
import cv2

from enum import Enum

import reasoner
import ast


class placeness:
    ''' placeness class for ontological reasoning '''

    relations = []

    def __repr__(self):
        ret = ''
        ret += str(self.age)
        ret += str(self.gender)
        ret += str(self.companion)
        ret += str(self.dayOfWeek)
        ret += str(self.timeOfDay)
        ret += str(self.timeOfYear)
        ret += str(self.activityType) 
        return ret


    def __init__(self, keywordlist=[]):
        self.keywordlist =         ast.literal_eval(keywordlist)

        self.age = []
        self.gender = []
        self.companion = []
        
        self.dayOfWeek = []
        self.timeOfDay = []
        self.timeOfYear = []
        
        self.activityType = [] 
        
        self.mapKeywords()

    def mapKeywords(self):
        for keyword in self.keywordlist:
            self.keywordToOntologyProperty(keyword)
   
    def keywordToOntologyProperty(self, keyword):
        wordbag_age = ['teen','20s', '30s', '40s', '50s', '60s and above']
        wordbag_gender = ['male', 'female']
        wordbag_companion = ['alone', 'date', 'family', 'friends'] #family includes children, friends includes colleagues

        wordbag_dayOfWeek = ['weekend', 'weekday']
        wordbag_timeOfDay = ['morning', 'afternoon', 'evening', 'dawn']
        wordbag_timeOfYear = ['spring', 'summer', 'autumn', 'winter']
        
        wordbag_activityType = ['business', 'education', 'legal', 'housing', 'relaxation', 'religion',
            'chores', 'dining', 'childcare', 'health', 'fashion&beauty', 'outdoor',
            'traveling', 'social', 'entertainment', 'art&culture']
        
        wordbag_list = [wordbag_age,wordbag_gender,wordbag_companion,wordbag_dayOfWeek,wordbag_timeOfDay,wordbag_timeOfYear,wordbag_activityType]
                 

        for i in range (len(wordbag_list)):        
            for list in wordbag_list[i]: 
                keyword_split = keyword.split('/')
                for ks in keyword_split:
                    if ks in list:
                        self.setOntologyAttribute(i, ks)
                  
    def setOntologyAttribute(self, i, keyword):
        if i==0:
            self.age.append(keyword)
        elif i==1:
            self.gender.append(keyword)
        elif i==2:
            self.companion.append(keyword)
        elif i==3:
            self.dayOfWeek.append(keyword)
        elif i==4:
            self.timeOfDay.append(keyword)
        elif i==5:
            self.timeOfYear.append(keyword)
        elif i==6:
            self.activityType.append(keyword)
            
    def setOntologyRelations(self):
        self.relations.append(('pmo:Placeness','describedAs','pmo:Visitor'))
        self.relations.append(('pmo:Placeness','describedAs','pmo:Time'))
        self.relations.append(('pmo:Placeness','describedAs','pmo:Activity'))
        
        self.relations.append(('pmo:Visitor','hasAge','pmo:age'))
        self.relations.append(('pmo:Visitor','hasGender','pmo:gender'))
        self.relations.append(('pmo:Visitor','visitsWith','pmo:companion'))
        self.relations.append(('pmo:Visitor','visitedAt','pmo:Time'))
        
        self.relations.append(('pmo:Time','dayOfWeekIs','pmo:dayOfWeek'))
        self.relations.append(('pmo:Time','timeOfDayIs','pmo:timeOfDay'))
        self.relations.append(('pmo:Time','timeOfYearIs','pmo:timeOfYear')) 
        self.relations.append(('pmo:Time','isHoliday','pmo:holiday')) 

        self.relations.append(('pmo:Activity','hasType','pmo:ActivityType'))
        
        self.relations.append(('pmo:work','subClassof','pmo:ActivityType'))
        self.relations.append(('pmo:living','subClassof','pmo:ActivityType'))
        self.relations.append(('pmo:leisure','subClassof','pmo:ActivityType')) 
    
'''
p = placeness(['laptop', '20s', 'monday', 'autumn/summer', 'evening']) 
print p.keywordlist
print p.age
print p.gender

print p.timeOfDay
print p.timeOfYear
print p.dayOfWeek
print p.activityType
'''
 
