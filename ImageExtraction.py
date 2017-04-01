# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 12:38:19 2017
plt.subplot(1,3,1),plt.imshow(blue_mask,'gray'),plt.xticks([]),plt.yticks([])
    plt.subplot(1,3,2),plt.imshow(green_mask,'gray'),plt.xticks([]),plt.yticks([])
    plt.subplot(1,3,3),plt.imshow(red_mask,'gray'),plt.xticks([]),plt.yticks([])
    plt.show()
@author: mayank
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

cap=cv2.VideoCapture(0)
blue_lb=np.array([110,50,50])
blue_ub=np.array([130,255,255])
green_lb=np.array([40,100,100])
green_ub=np.array([60,255,255])
red_lb=np.array([0, 70, 50])
red_ub=np.array([10,255,255])
red_lb1=np.array([170, 70, 50])
red_ub1=np.array([180,255,255])
skin_min_YCrCb = np.array([0,133,77],np.uint8)
skin_max_YCrCb = np.array([255,173,127],np.uint8)


while(True):
    r,fr=cap.read()
    f=cv2.cvtColor(fr,cv2.COLOR_BGR2HSV)
    ycr=cv2.cvtColor(fr,cv2.COLOR_BGR2YCR_CB)
    blue_mask=cv2.inRange(f,blue_lb,blue_ub)
    green_mask=cv2.inRange(f,green_lb,green_ub)
    red_mask=cv2.inRange(f,red_lb|red_lb1,red_ub|red_ub1)
    skin_mask=cv2.inRange(ycr,skin_min_YCrCb,skin_max_YCrCb)
    cv2.resizeWindow('cam',640,380)
    cv2.resizeWindow('cam1',640,380)
    cv2.resizeWindow('cam2',640,380)
    
    #cv2.imshow('cam',cv2.bitwise_and(f,f,mask=blue_mask))
    #cv2.imshow('cam1',cv2.bitwise_and(f,f,mask=green_mask))
    cv2.imshow('cam2',cv2.bitwise_and(f,f,mask=skin_mask))
    if cv2.waitKey(1)==ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()    