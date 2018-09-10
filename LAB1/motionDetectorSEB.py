# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 19:10:29 2018

@author: sebas
"""

import cv2
#OpenCV Documentation https://docs.opencv.org/3.3.1/de/de1/group__video__motion.html
cap = cv2.VideoCapture(0)
motion_detector = cv2.createBackgroundSubtractorMOG2(120, 100.0,False)

while True:
    ret,frame=cap.read()
    #applied a grayscale to reduce noise
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    detector = motion_detector.apply(gray)
    
    cv2.imshow('MotionDetector',detector)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()