# -*- coding: utf-8 -*-




f = open ("./temp.txt")

keys = []

for line in f:
    if "Activity" in line:
        name = line.split("Activity")[1]
        #print name[:-3]
        keys.append(name[:-3])





f = open("./data/corpus/corpus.txt")
output = open("./data/corpus/res.txt", "w")
output2 = open("./data/corpus/res2.txt", "w")
output3 = open("./data/corpus/res3.txt", "w")
output4 = open("./data/corpus/res4.txt", "w")

for line in f:
    
    
    name = line.split(" ")[0]
    t = line.split(" ")[1].strip()
    
    if name == "root" or name == "acitvity" or name == "with" or name == "dweller" or name == "what" or name == "when" or name == "activity":
        continue
    
    if not (name in keys):    
        cl = ""
        
        cl += '{ \n "id": "' + name + '", \n "type": "owl:Thing"\n},\n'
        output3.write(cl)
        
        cl =""
        cl += '{ \n "id": "' + name + '", \n "label": {\n "undefined": "' + name + '" \n},\n\
        "comment": {\n "undefined": "' + name + '" \n},\n\
        "annotations": {\n "term_status": [{\n"identifier": "term_status",\n"language": "undefined",\n\
        "value": "stable",\n"type": "label"\n}]\n},\n"instances": 0 \n},\n'
    
        output4.write(cl)

    '''
    {
            "id": "상견례",
            "type": "owl:Thing"
    }
    '''
    '''
    {
        "id": "상견례",
        "label": {
             "undefined": "상견례"
        },
        "comment": {
            "undefined": "A place."
        },
        "annotations": {
            "term_status": [{
                "identifier": "term_status",
                "language": "undefined",
                "value": "stable",
                "type": "label"
            }]
        },
        "instances": 0
    }
    '''
    




    '''
    {
        "id": "Activity상견례",
        "type": "owl:objectProperty"
    }
    '''
    
    cl =""

    cl += '{ \n "id": "' + str(t.title())+str(name) + '", \n "type": "owl:objectProperty"\n},\n'

    output2.write(cl)


    '''
    {
        "id": "Place2Dweller",
        "label": {
             "undefined": "dwelledBy"
        },
         "comment": {
            "undefined": ""
        },
        "isDefinedBy": "http://xmlns.com/foaf/0.1/",
        "annotations": {
            "term_status": [{
                "identifier": "term_status",
                "language": "undefined",
                "value": "testing",
                "type": "label"
            }]
        },
        "domain": "Place",
        "range": "Dweller"
    }, 
    '''
 
    
    cl =""
    
    
    cl += '{ \n "id": "' + str(t.title())+str(name) + '", \n "label": {\n "undefined": "' + "fixme" + '" \n},\n\
    "comment": {\n "undefined": "' + "comment" + '" \n},\n\
    "isDefinedBy": "http://xmlns.com/foaf/0.1/",\n\
    "annotations": {\n "term_status": [{\n"identifier": "term_status",\n"language": "undefined",\n\
    "value": "stable",\n"type": "label"\n}]\n},\n \
    "domain": "' + t.title() + '", \n \
    "range": "' + name + '" \n \
     },\n'

    output.write(cl)

    
    
    #print name
    
    
    
    

    
output.close()
output2.close()
output3.close()
output4.close()

