import os
import json
from datetime import datetime
from src import dbhandler
from src import placeontology
from src import cognitiveAPI

node = dbhandler.firebase('https://placenessdb.firebaseio.com/data/yap')

data = {}

node.put("", json.dumps(data))
