from src import dbhandler


db = dbhandler.firebase('https://placenessdb.firebaseio.com/ontology/')

opinions = []

places = db.get("/")

f = open("opinion_corpus.txt","w")

for place in places:
    place_instance = places[place]
    
    for posts in place_instance:
        ps = place_instance[posts]
        
        for p in ps:
            inst = ps[p]
            
            #print inst
            #print inst['metadata']
        
            try:
                ops = inst['opinion']['modified_keywords']
                
                #print ops
                
                for op in ops:
                    #print op
                    if not op in opinions:
                        opinions.append(op)
                        f.write(op.encode('utf8') + "\n")
                        
            except:
                pass
                


#f.write(str(opinions))
f.close()