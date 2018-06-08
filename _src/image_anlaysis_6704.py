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
    filename = (request.args.get('filename'))
    print filename
    urllib.urlretrieve (filename, "temp.jpg")
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
    img = cv2.imread("./temp.jpg")
    
    if not img is None:
        
        ########## 1. FACE DECTECTION ############
        scale_factor = 1.1
        min_neighbors = 3
        min_size = (30, 30)
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE

        width = len(img)
        height = len(img[0])
        
        faces = face_cascade.detectMultiScale(img, scaleFactor = scale_factor, minNeighbors = min_neighbors,minSize = min_size, flags = flags)
        
        numfaces = len(faces);
        
        isSelfie = False;
        
        for (x,y,w,h) in faces:
            if w>width/3 or h>height/3:
                isSelfie = True  
                  
        ########## 2. COLOR ANALYSIS ############
        
        Z = img.reshape((-1,3))        
        Z = np.float32(Z)
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.1) # criteria = 10 iterations, epsilon < 1.0
        K = 8
         
        ret,label,center=cv2.kmeans(Z,K,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

        primary_hsv = []
        for color in center:
            b,g,r = color;   
            
            bgr = np.uint8([[[b,g,r ]]]) 
            hsv = cv2.cvtColor(bgr,cv2.COLOR_BGR2HSV)
             
            h,s,v = hsv[0][0][0]/180.0*360, hsv[0][0][1]/255.0*100, hsv[0][0][2]/255.0*100; 
            hsv_tuple = (h,s,v)
            primary_hsv.append(hsv_tuple)
    
        ########## 3. TAGS AND ACTIVITY ############ 
        captions=[]
        
        script = '/root/tensorflow/tensorflow/models/im2txt/bazel-bin/im2txt/run_inference   --checkpoint_path=${CHECKPOINT_DIR}   --vocab_file="/home/cdsn/workspace/placenessdb/word_counts.txt"   --input_files="/home/cdsn/workspace/placenessdb/temp.jpg"'
        output = subprocess.check_output(script, shell=True, env={'LD_LIBRARY_PATH':"$LD_LIBRARY_PATH:/usr/local/cuda/lib64", 'CUDA_HOME':'/usr/local/cuda', 'CHECKPOINT_DIR':"/root/im2txt/model/train"})
        lines= output.split("\n");
        
        for i in range(len(lines)-2):
            caption =(lines[i+1].split(") ")[1].split(" (")[0],float(lines[i+1].split(") ")[1].split("p=")[1].split(")")[0]))
            captions.append(caption);
            
    
        ######### WRITE RESULTS #################
        res = {'isSelfie':isSelfie, 'numface':numfaces, 'primary_hsv':primary_hsv, 'captions':captions}
        
    
        print (filename, res);
        image_tag = '<img src="' +filename + '" style="width:640">'
        return str(res) + '\n<br>' + image_tag;
    
        '''    
        try:
            dat_db.patch("/" + hotspotid + "/"+postid, json.dumps(res))
        except:
            print "firebase error has occured with " + "/" + hotspotid + "/"+postid
        '''
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6704)