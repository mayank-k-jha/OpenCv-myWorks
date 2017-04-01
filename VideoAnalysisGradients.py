# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 14:51:10 2017

@author: mayank
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

cap=cv2.VideoCapture(0)
kernel=np.ones((5,5),np.uint8)

while(True):
    ret,fr=cap.read()
    #fr=cv2.Laplacian(fr,cv2.CV_64F)
    #fr=cv2.GaussianBlur(fr,(5,5),0)
    #fr=cv2.Sobel(fr,cv2.CV_64F,0,1,ksize=5)
    
    #Canny edge detection
    fr=cv2.Canny(fr,100,220)
    
    cv2.morphologyEx(fr,cv2.MORPH_RECT,kernel)
    fr=cv2.GaussianBlur(fr,(5,5),0)
    
    cv2.resizeWindow('cam',640,360)
    cv2.imshow('cam',fr)
    if cv2.waitKey(1)==32:
        break
    
cap.release()
cv2.destroyAllWindows()    