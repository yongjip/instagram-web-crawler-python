

def applyRules(rule, placeness):
    
    pass

def generateRules(placeness):
    
    pass
    


def ruleBasedInference(placeness):
    ret = [] 
    
    rulelist = open("placeness_knowledgebase_rules.txt",'r')
    
    for rule in rulelist:
        res = applyRules(rule, placeness)
        
        if res!= False:
            ret.append(res)     
    
    return ret