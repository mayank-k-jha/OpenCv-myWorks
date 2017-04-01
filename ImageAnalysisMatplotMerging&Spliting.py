# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 23:29:18 2017

@author: mayank
"""

import cv2
import matplotlib.pyplot as plt
img=cv2.imread('D:/pics/special/bell_boeing_v_22_osprey-wide.jpg')
b,g,r=cv2.split(img)
img=cv2.merge([r,g,b])
plt.imshow(img,cmap='autumn',interpolation='bicubic')
#plt.xticks([]),plt.yticks([])
plt.show()