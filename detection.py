#import libraries of python opencv
import cv2
import numpy as np
import dlib
import time
import cv2
import threading
import math

#create VideoCapture object and read from video file
cap = cv2.VideoCapture('cars.mp4')
#use trained file XML classifiers
car_cascade = cv2.CascadeClassifier('file.xml')
#claculation for speed
def estimateSpeed(location1,location2):
    d_pixels=math.sqrt(math.pow(loacation2[0]-location1[0],2)+math.pow(location2[1]-location1[1],2))
    	# ppm = location2[2] / carWidht

    ppm=8.8
    d_meters=d_pixel/ppm
    	#print("d_pixels=" + str(d_pixels), "d_meters=" + str(d_meters))

    fps=18
    speed=d_meters*fps*3.6
    return speed
#read until video is completed
while True:
    #capture frame by frame
    ret, frame = cap.read()
    #convert video into gray scale of each frames
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #detect cars in the video
    cars = car_cascade.detectMultiScale(gray, 1.1, 3)

    #to draw arectangle in each cars 
    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)      

    #display the resulting frame
    cv2.imshow('video', frame)
    #press Q on keyboard to exit
    if cv2.waitKey(25) & 0xFF == ord('e'):
        break
#release the videocapture object
cap.release()
#close all the frames
cv2.destroyAllWindows()
