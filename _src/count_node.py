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

dat_db = dbhandler.firebase('https://placenessdb.firebaseio.com/experiment/')

shallows = dat_db.get_shallow('/')
sum = 0;
for shallow in shallows:
    hotspot_shallow = dat_db.get_shallow('/'+shallow+'/')
    a = len(hotspot_shallow)
    sum += a
    print (shallow + ": " + str(a))
print sum

 