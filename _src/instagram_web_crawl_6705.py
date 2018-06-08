#-*- coding: utf-8 -*-

import urllib
import json
from bs4 import BeautifulSoup
import sys
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def main(): 
    return realtime_instagram(request.args.get('locationid'), request.args.get('max_id'))

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

 
def realtime_instagram(locationid, max_id):
    if (max_id==None):
        url = "https://www.instagram.com/explore/locations/"+locationid+"/" # + "?max_id="1362778012957782134"
    else:
        url = "https://www.instagram.com/explore/locations/"+locationid+"/" + "?max_id="+max_id
    html = urllib.urlopen(url).read()
       
    print "url: ", url 
          
    soup = BeautifulSoup(html) 
    data = soup.findAll("script", { "type" : "text/javascript" }) 
    json_text =  '{'+(str(data[4]).split('"media": {')[1].split(', "top_posts":')[0]) 
    
    json_data = json.loads(json_text)['nodes']
    
    table_txt = '<table border="1">'
    table_txt += '<tr>' 
    table_txt += '<td>picture</td>'
    table_txt += '<td>code</td>'
    table_txt += '<td>owner</td>'
    table_txt += '<td>comments</td>'
    table_txt += '<td>likes</td>'
    table_txt += '<td>date</td>'
    table_txt += '<td>id</td>'  
    table_txt += '<td>caption</td>'
    
    table_txt += '</tr>'
    
    res ={}

    for json_instance in json_data:
        res ={}
        table_txt += '<tr>' 
         
        res['code']= "json['code']"
        res['owner']= "json['owner']"
        res['comments']= "json['comments']"
        res['caption']= "json['caption']"
        res['likes']= "json['likes']"
        res['date']= "json['date']"
        res['id']= "json['id']"
        res['display_src']= "json['display_src'] "
        
        try:
            res['code']= json_instance['code']
            res['owner']= json_instance['owner']
            res['comments']= json_instance['comments']
            res['caption']= json_instance['caption']
            res['likes']= json_instance['likes']
            res['date']= json_instance['date']
            res['id']= json_instance['id']
            res['display_src']= json_instance['display_src']
        except:
            print "VALUE MISSING"  
             
        table_txt += '<td><img src="'+res['display_src']+'" style="width:320">' + '</td>' 
        table_txt += '<td>' + str(res['code'])+'</td>' 
        table_txt += '<td>' + str(res['owner'])+'</td>' 
        table_txt += '<td>' + str(res['comments'])+'</td>' 
        table_txt += '<td>' + str(res['likes'])+'</td>' 
        table_txt += '<td>' + str(res['date'])+'</td>' 
        table_txt += '<td>' + str(res['id'])+'</td>' 
        table_txt += '<td>' + res['caption'].encode('utf-8').decode('utf-8') +'</td>' 
        table_txt += '</tr>'
        
        print res
    
    table_txt += '</table>'
    f = open("/var/www/html/realtime_instagram/index.html", "w");
    f.write(table_txt.encode('utf-8'));
    
    next_url = "<a href='http://socialcomputing.kaist.ac.kr:6705/?locationid="+locationid+"&max_id="+str(res['id']+"'>"+"http://socialcomputing.kaist.ac.kr:6705/?locationid="+locationid+"&max_id="+str(res['id'])+"</a>")

    
    return next_url +'<br>\n' + str(json_data) + '\n' + table_txt;

'''
if (len(sys.argv) == 2):
    location_id = sys.argv[1]
    realtime_instagram(location_id)
'''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6705)


    