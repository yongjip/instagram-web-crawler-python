from src import dbhandler

############# 0. initialization ############
db = dbhandler.firebase('https://placenessdb.firebaseio.com/corpus/')

############# 1. fetching place ids ############
corpus = db.get("/")
edges = corpus['edges']
nodes = corpus['nodes']

############# 2. fetching place instance ids ############
for node in nodes:
    print node, nodes[node]['type'][0]