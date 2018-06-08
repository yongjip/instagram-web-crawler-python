import cv2
import numpy as np

filename = 'megabox_1152389346192391028.jpg'

scale_factor = 1.1
min_neighbors = 3
min_size = (30, 30)
flags = cv2.cv.CV_HAAR_SCALE_IMAGE

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
img = cv2.imread('data/image161010/'+ filename)

width = len(img)
height = len(img[0])

faces = face_cascade.detectMultiScale(img, scaleFactor = scale_factor, minNeighbors = min_neighbors,minSize = min_size, flags = flags)

numfaces = len(faces);

isSelfie = False;


for (x,y,w,h) in faces:
    if w>width/2 or h>height/2:
        isSelfie = True
        
