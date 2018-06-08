# -*- coding: utf-8 -*-

from src import dbhandler
from src import cognitiveAPI
from src.jsonencoder import *
import numpy as np
import subprocess
import cv2
import os  
import urllib
import json
from bs4 import BeautifulSoup
from flask import Flask
from flask import request
from src import dbhandler
import sys
import ast

import read_csv
import image_analysis
import analyze_time
import time

hotspots =0

dat_db = dbhandler.firebase('https://placenessdb.firebaseio.com/')
places = dat_db.get_shallow('/data/coex') 

for place in places: 
     
    hotspots+= len(place)
     
print hotspots
