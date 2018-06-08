# -*- coding: utf-8 -*-

import urllib2
import json

class firebase:
    def __init__(self, url) :
        self.root = url 

    def push(self, node, data):
        request = urllib2.Request(self.root+node+".json", data, {'Content-Type': 'application/json'})
        urlop = urllib2.urlopen(request)
        res = json.load(urlop)['name']
        return res
    
    def put(self, node, data):
        request = urllib2.Request(self.root+node+".json", data, {'Content-Type': 'application/json'})
        request.get_method = lambda: 'PUT'
        urlop = urllib2.urlopen(request)
    
    def patch(self, node, data):
        request = urllib2.Request(self.root+node+".json", data, {'Content-Type': 'application/json'})
        request.get_method = lambda: 'PATCH'
        urlop = urllib2.urlopen(request)
        
    def get(self, node):
        request = urllib2.Request(self.root+node+".json")
        urlop = urllib2.urlopen(request)
        res = json.load(urlop)
        return res

    def get_shallow(self, node):
        request = urllib2.Request(self.root+node+".json?shallow=true")
        urlop = urllib2.urlopen(request)
        res = json.load(urlop)
        return res
    
    def put_list(self,node, list):
        data = {}
        
        for i in range(len(list)):
            data[str(i)] = list[i]
            
        request = urllib2.Request(self.root+node+".json", json.dumps(data), {'Content-Type': 'application/json'})
        request.get_method = lambda: 'PUT'
        urlop = urllib2.urlopen(request)
            
            
    #####insert lists of keywords
    def put_dweller(self, districtname, placename, postid, keywords):
        self.put_list(districtname+"/"+placename+"/"+postid+"/dweller/keywords/", keywords)
    def put_with(self, districtname, placename, postid, keywords):
        self.put_list(districtname+"/"+placename+"/"+postid+"/with/keywords/", keywords)
    def put_when(self, districtname, placename, postid, keywords):
        self.put_list(districtname+"/"+placename+"/"+postid+"/when/keywords/", keywords)
    def put_what(self, districtname, placename, postid, keywords):
        self.put_list(districtname+"/"+placename+"/"+postid+"/what/keywords/", keywords)
    def put_activity(self, districtname, placename, postid, keywords):
        self.put_list(districtname+"/"+placename+"/"+postid+"/activity/keywords/", keywords)
    def put_opinion(self, districtname, placename, postid, keywords):
        self.put_list(districtname+"/"+placename+"/"+postid+"/opinion/keywords/", keywords)
        
         
    ####insert json 
    def put_when_timestamp(self, districtname, placename, postid, data):
        self.put(districtname+"/"+placename+"/"+postid+"/when/timestamp/", data)
    def put_imageAnalysis(self, districtname, placename, postid, data):
        self.put(districtname+"/"+placename+"/"+postid+"/image_analysis/", data)
    def put_profileAnalysis(self, districtname, placename, postid, data):
        self.put(districtname+"/"+placename+"/"+postid+"/profile_analysis/", data)
    def put_metadata(self, districtname, placename, postid, data):
        self.put(districtname+"/"+placename+"/"+postid+"/metadata/", data)