# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 20:33:30 2017

@author: mayank
"""

import cv2
import numpy as np

img=cv2.imread('D:/pics/special/the_pooh_team.jpg')
b,g,r=img[:,:,0],img[:,:,1],img[:,:,2]

img1=cv2.merge([r,b,g])
cv2.namedWindow('rbg',cv2.WINDOW_NORMAL)
cv2.imshow('rbg',img1)
cv2.waitKey(1)

img2=cv2.merge([r,g,b])
cv2.namedWindow('rbg',cv2.WINDOW_NORMAL)
cv2.imshow('rbg',img2)  
cv2.waitKey(0)

img3=cv2.merge([b,r,g])
cv2.namedWindow('rbg',cv2.WINDOW_NORMAL)
cv2.imshow('rbg',img3)
cv2.waitKey(0)

img4=cv2.merge([g,r,b])
cv2.namedWindow('rbg',cv2.WINDOW_NORMAL)
cv2.imshow('rbg',img4)
cv2.waitKey(0)

img5=cv2.merge([g,b,r])
cv2.namedWindow('rbg',cv2.WINDOW_NORMAL)
cv2.imshow('rbg',img5)
cv2.waitKey(0)

cv2.namedWindow('rbg',cv2.WINDOW_NORMAL)
cv2.imshow('rbg',img)
cv2.waitKey(0)

cv2.destroyAllWindows()
