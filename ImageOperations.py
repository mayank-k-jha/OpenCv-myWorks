# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 00:02:14 2017
img=cv2.cvtColor(img,cv2.COLOR_BGR2HLS_FULL)

print([i for i in dir(cv2)  if 'COLOR_BGR' in i])
@author: mayank
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


img=cv2.imread('D:/pics/special/Goku_by_drozdoo.png')
img1=cv2.imread('D:/pics/special/fox-1366x768.jpg')
#img[420:540,800:900]=img[300:420,300:400]             #extracting part of image
#img[100:300,:,0]=152                 #changing all red colors in selected region with value 152
#r,g,b=cv2.split(img)       #slow
#img1[:640,:1024]=img+img1[:640,:1024]
                
"""
r,g,b=img[:,:,0],img[:,:,1],img[:,:,2]  #fast numpy indexing
print(r[:1],g[:1],b[:1])

plt.subplot(1,2,1),plt.imshow(img,'gray')
plt.subplot(1,2,2),plt.imshow(img1,'gray')
plt.xticks([]),plt.yticks([])
plt.show()
plt.show()
"""
cv2.resizeWindow('cam',640,360);
cv2.resizeWindow('cam1',640,360);
cv2.imshow('cam',img)

cv2.imshow('cam1',img1)

if cv2.waitKey(0)==ord('q'):
    cv2.destroyAllWindows()
