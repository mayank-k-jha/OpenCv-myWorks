# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 23:02:22 2017

@author: mayank
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img =cv2.imread('D:/pics/Pictures/20151206_164453.jpg')
img1=img
#img=cv2.GaussianBlur(img,(5,5),0)
#cv2.medianBlur(img,5)
kernel=np.ones((5,5),np.uint8)
#img=cv2.bilateralFilter(img,9,75,75)
"""Noise removal by erroding follwed by dilation  or directly by Laplacian"""
#img=cv2.erode(img,kernel,iterations=1)
#img=cv2.dilate(img,kernel,iterations=1)
#img=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
#img=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
img=cv2.morphologyEx(img,cv2.MORPH_RECT,kernel)
l=[i for i in dir(cv2) if 'MORPH_'in i]
print(l)
cv2.namedWindow('cam',cv2.WINDOW_NORMAL)
cv2.imshow('cam',img)
cv2.namedWindow('cam1',cv2.WINDOW_NORMAL)
cv2.imshow('cam1',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()