# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import cv2
import time

#input from user to get the amount of time before each frame is written to another file
#no excpetion handling implemented
#n = int(input("Please type a number from 1 to 10\n"))

cap = cv2.VideoCapture(0)
start = time.time()
count=0

#For part 5 of Lab1
#out = cv2.VideoWriter('outpy.mp4',cv2.VideoWriter_fourcc('M','J','P','G'), 24, (640,480)) 
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    count+=1

    cv2.imshow('frame0',frame)

      
      
      
    # Display the resulting frame
    
    #----------1. Display the gray level version of the image-----------------#
    #this modifies the frame capture to grayscale 
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow(“frame”, gray)
    
    
    #----------2. Display the negative gray level version of the image--------#
    #color range in frames is [255], inverse is [1 – range] 
    #From statistics, set A contains all the colors, then set A' contains the not-colors or negative of colors 
    #cv2.imshow(“frame”, 1 - gray) #current range is gray, thus [1 - gray]
    
    
    #-------3. Display the mirrored version of the original color image.-----#
    #mirror = cv2.flip(frame, 1) # passing argument [1] flips the image given the #Y - axis
    #cv2.imshow(“frame”, mirror)

    #------4. Display the original color image upside down.-------------------#
    #upside_down = cv2.flip(frame, 0) # passing argument [0] flips the image #given the X - axis
    #cv2.imshow(“frame”, upside_down)
    
    #---5. Write to a file one frame every n second, where n is a user-supplied parameter.
    #open VideoWriter
    #out = cv2.VideoWriter(‘myVideo.avi’, #cv2.VideoWriter_fourcc(‘M’,’J’,’P’,’G’),24, Size(frame_width, frame_height))
    


  
   
    #IMPORTANT: typecast time to int to make the condition true given time % n
   # if int(time.time() - start) % n == 0:
   #     out.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if count%30==0:
        print(np.max(frame),np.min(frame))
    
elapsed_time = time.time()-start


    
print('Capture speed: {0:.2f} frames per second'.format(count/elapsed_time))   

# When everything done, release the capture
cap.release()
#to release VideoWriter
#out = release()
cv2.destroyAllWindows()