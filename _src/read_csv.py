'''
Created on 2016. 11. 14.

@author: ozma
'''



def get_text_dict():
    f = open("word_hierachy.csv", "r")
    
    text_dict = {'business':[], 'education':[], 'legal':[], 'housing':[], 'relaxation':[], 'religion':[],
            'chores':[], 'dining':[], 'childcare':[], 'health':[], 'fashion&beauty':[], 'outdoor':[],
            'traveling':[], 'social':[], 'entertainment':[], 'art&culture':[]}
    
    for line in f:
        s = line.strip().split(',')
        text_dict[s[1]].append(s[0])
    '''    
    for word in text_dict:
        print word
        for w in text_dict[word]:
            print '\t' + w
    '''
    
    f.close()
    return text_dict 

def get_text_dict_feature_vector():
    f = open("word_hierachy.csv", "r")
    res = []
     
    for line in f:
        s = line.strip().split(',')
        res.append(s[0])
    
    return res 
    



def get_img_dict():
    img_dict = {
        'business': ["tie", "laptop", "computer", "keyboard", "desk", "chair", "suit"],
        'education': ["book", "paper"],
        'legal': [],
        'housing': ["flower", "candle", "room", "vase", "furniture", ],
        'relaxation': ["couch", "sitting", "bathtub", "tv", "television", "bed", "book", "blanket", "fireplace"],
        'religion': [],
        'chores': ["bathroom", "sink", "kitchen", "toilet", "trash", "refrigerator", "stove", "shelf", "oven"],
        'dining': ["coffee", "plate", "cake", "food", "donut", "fork", "sandwich", "bowls", "chocolate", "bottle", "fries", "cup", "glass", "salad", "vegetables", "juice", "carrots", "dining", "spoon", "chips", "lettuce", "fruit", "pizza", "eating", "meat", "chopstick"],
        'childcare': ["boy", "girl", "child", "baby"],
        'health': [],
        'fashion&beauty': ["dress", "shirt", "tie", "hat", "ribbon"],
        'outdoor': ["sky", "kites", "view", "street", "bench", "tower", "city", "park", "sidewalk", "tree", "bird", "grass", "snow", "field", "building", "ramp", "statue", "sidewalk", "boat", "sunglass", "bird", "forest", "bridge", "river", ],
        'traveling': ["luggage", "flying", "station", "train", "suitcase", "truck", "car", "traffic", "parked", "motorcycle", "subway", "platform", "bike", "helmet"],
        'social': ["people", "wine", "smiling", "birthday", "christmas", "beer", "crowd", "bride", "wedding", "couple"],
        'entertainment': ["nintendo", "stuffed animals", "playing", "game", "wii", "controller", "frisbee", "baseball", "carousel", "skateboard", "horse", "racquet", "tennis", "snowboard", "basketball"],
        'art&culture': ["parade"]
    }
    return img_dic
