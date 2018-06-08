from src import dbhandler

import read_csv
import activity_classifier 
import analyze_time
from src import reasoner
from src import placeness

fileprefix = 'experiment_140105_ipark'


#1. read database, generate keywordlist file
if (True):
    f = open(fileprefix+".txt","w")
    g = open(fileprefix+"_timestamp.txt","w")

    text_word_dict = read_csv.get_text_dict() 
    dat_db = dbhandler.firebase('https://placenessdb.firebaseio.com/')
    posts = dat_db.get('/experiment/ipark')
    
    mapping = []
    for wordbag in text_word_dict:
        mapping.append(wordbag); 
    
    for post in posts:
        res = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
        data = posts[post] 
        
        g.write(str(data['date']) + '\n')
        
        for wordbag in text_word_dict:
            for word in text_word_dict[wordbag]:
                if (word.decode('utf-8') in data['caption']):                
                     res[mapping.index(wordbag)] = 1    #checks occurence
             
        f.write(str(res) + '\n')
        print(str(res))
        
    f.close() 
    g.close() 
 

#2. generate feature vector
if (True): 
    text_feature_vector = read_csv.get_text_dict_feature_vector() 
    len_text_feature_vector = len(text_feature_vector)
    out_c = open(fileprefix+'.txt','r')
    keyword_file = open(fileprefix + '_keyword.txt','r')
    
    f = open(fileprefix + '_featurevec.txt',"w")
    
    print len_text_feature_vector 
    
    for line in keyword_file:
        label = out_c.readline().strip()
        
        zero_vector = [0] * len_text_feature_vector
    
        b = ast.literal_eval(line)
        for word in b:
            temp_idx = text_feature_vector.index(word)
            zero_vector[temp_idx] += 1
            
        f.write(label + "," + str(zero_vector)[1:-1] + '\n')
    
    f.close()
 
#3-1. activity classification
activity_cluster_keyword = []
if(True):
    trainingdata = fileprefix + '_featurevec.txt'
    #trainingdata = 'dat_train_d.txt'
    
    activity_cluster_labels = activity_classifier.test(trainingdata, 'svm_model_161212.ml')    
    activity_classification = ['childcare', 'social', 'fashion&beauty', 'social/traveling', 'dining',
                'traveling', 'outdoor', 'art&culture', 'religion', 'entertainment', 'education',
                'housing', 'health', 'entertainment/art&culture', 'social', 'business']
    
    for label in activity_cluster_labels:
        activity_cluster_keyword.append(activity_classification[int(label) -1])


#3-2. time classification
time_analysis_keyword = []
if (True):
    f = open(fileprefix+"_timestamp.txt","r")
    
    for line in f:
        time_analysis_keyword.append(analyze_time.get_time_analysis_keywords(line.strip()))
 

#3-3. visitor classification
#visitor_analysis

 
#4. form ontology vector
ontology_vector = []
if (True): 
     #['laptop', 'female', '20s', 'monday', 'autumn', 'evening', 'social/traveling']
    for i in range(len(time_analysis_keyword)):
        temp =[]
        temp.append(activity_cluster_keyword[i])
        for k in time_analysis_keyword[i]:
            temp.append(k)
        ontology_vector.append(temp)
    
    f = open(fileprefix+"_ontologyvector.txt","w")
    for vector in ontology_vector:
        f.write(str(vector) + '\n');
    f.close()
 
#4. ontology mapping  
 



'''

#4-1 rule generation
f = open (fileprefix+"_ontologyvector.txt","r")
ont_v = []
for line in f:
    ont_v.append(line.strip());

placeness_repr_list = {}

for ont_v_child in ont_v:
    #print ont_v_child
    p = placeness.placeness(keywordlist=ont_v_child)
    if str(p) in placeness_repr_list:
        placeness_repr_list[str(p)] +=1
    else:
        placeness_repr_list[str(p)] =1
    
    #asdf = raw_input("asdfasd")
    
f f = open (fileprefix+"_observedplaceness2.txt","w")

for key in placeness_repr_list:
    #print key + ": " + str(placeness_repr_list[key])
    if ((placeness_repr_list[key])>100):
        f.write(key + "\t" + str(placeness_repr_list[key]) + "\n")
f.close()

#5. generate rules

'''










