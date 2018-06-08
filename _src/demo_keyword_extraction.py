# -*- coding: utf-8 -*-


def with_analysis(input) : 
    res =[]
     
    if u"엄마" in input:
        res.append(u"가족")
    if u"엄마" in input:
        res.append(u"엄마")
    if u"모녀" in input:
        res.append(u"가족")
    if u"모녀" in input:
        res.append(u"딸")
        
    return res
    
def space_analysis(input) : 
    res =[] 
        
    return res

def activity_analysis(input) : 
    res =[]
     
    if u"와구와구" in input:
        res.append(u"식사")
    
    if u"모녀" in input:
        res.append(u"육아")
    if u"모녀" in input:
        res.append(u"식사")
        
    return res

def when_analysis(input) : 
    res =[]
     
    if u"월요일" in input:
        res.append(u"평일")
    if u"현충일" in input:
        res.append(u"공휴일")
        
    return res 



def what_analysis(input) : 
    res =[]
     
    if u"멕시칸" in input:
        res.append(u"멕시칸음식")
    if u"다정" in input:
        res.append("Enchilada")
        
    return res 













