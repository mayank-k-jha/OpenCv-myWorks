# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 01:45:16 2017

@author: mayank
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

kernel=np.ones((5,5))
img=cv2.imread('D:/pics/special/Goku_by_drozdoo.png',1)

#Canny edge detection
img1=img
img1=cv2.Canny(img1,100,200)
img1=cv2.GaussianBlur(img1,(5,5),0)


l = cv2.Laplacian(img,cv2.CV_64F)
l=cv2.GaussianBlur(l,(5,5),0)

sx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sx=cv2.GaussianBlur(sx,(5,5),0)

sy = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
sy=cv2.GaussianBlur(sy,(5,5),0)
#sy=cv2.morphologyEx(sy,cv2.MORPH_RECT,kernel)

cv2.namedWindow('Laplacian',cv2.WINDOW_NORMAL)
cv2.namedWindow('Sobelx',cv2.WINDOW_NORMAL)
cv2.namedWindow('Sobely',cv2.WINDOW_NORMAL)
cv2.namedWindow('img',cv2.WINDOW_NORMAL)

cv2.imshow('Laplacian',l)
cv2.imshow('Sobelx',sx)
cv2.imshow('Sobely',sy)
cv2.imshow('img',img1)

cv2.waitKey(0)
cv2.destroyAllWindows()