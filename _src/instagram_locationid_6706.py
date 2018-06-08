from src import dbhandler
from src import cognitiveAPI
from src.jsonencoder import *
import numpy as np
import subprocess
import cv2
import os  
import urllib
from flask import Flask
from flask import request


app = Flask(__name__)
@app.route("/")
def main():
    lat = (request.args.get('lat'))
    lng = (request.args.get('lng'))
    distance = (request.args.get('distance'))

    if (distance==None):
        distance = '750'
    
    token = '2102054277.a8877cd.4e351957bbcd458db4b40fb6424d69df'

    url = 'https://api.instagram.com/v1/locations/search?lat='+lat+'&lng='+lng+'&access_token='+token+'&distance='+distance
    print url
    
    html = urllib.urlopen(url).read() 
    
    return html 

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6706)

'''
coex = (37,30,42.24,127,3,32.59)
lat = str(coex[0]+float(coex[1])/60.0+float(coex[2])/60.0/60.0)
lng = str(coex[3]+float(coex[4])/60.0+float(coex[5])/60.0/60.0)
 
token = '2102054277.a8877cd.4e351957bbcd458db4b40fb6424d69df'
 
print url

html = urllib.urlopen(url).read() 

print html
'''