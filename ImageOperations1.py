# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 04:00:37 2017

@author: mayank
"""

import cv2
import matplotlib.pyplot as plt
import numpy

print(cv2.useOptimized())

"""print([i for i in dir(cv2) if 'THRESH_' in i])
print([i for i in dir(cv2) if 'WINDOW_' in i])
img=cv2.imread('D:/pics/opencv-logo2.png',0)

ret,th=cv2.threshold(img,10,255,cv2.THRESH_BINARY)
ret1,th1=cv2.threshold(img,10,255,cv2.THRESH_BINARY_INV)
ret2,th2=cv2.threshold(img,10,255,cv2.THRESH_MASK)
ret3,th3=cv2.threshold(img,10,255,cv2.THRESH_OTSU)
ret4,th4=cv2.threshold(img,10,255,cv2.THRESH_TOZERO)
ret5,th5=cv2.threshold(img,10,255,cv2.THRESH_TOZERO_INV)
ret6,th6=cv2.threshold(img,10,255,cv2.THRESH_TRIANGLE)
ret7,th7=cv2.threshold(img,10,255,cv2.THRESH_TRUNC)
th8=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th9=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

c=[img,th,th1,th2,th3,th4,th5,th6,th7,th8,th9]
b=["image","THRESH_BINARY","THRESH_BINARY_INV","THRESH_MASK","THRESH_OTSU","THRESH_TOZERO","THRESH_TOZERO_INV","THRESH_TRIANGLE","THRESH_TRUNC","ADAPTIVE_THRESH_MEAN_C","ADAPTIVE_THRESH_GAUSSIAN_C"]
for i in range(0,11):
    plt.subplot(6,2,i+1)
    plt.imshow(c[i],'gray'),plt.xticks([]),plt.yticks([])
    plt.title(b[i])
figure=plt.gcf()    
figure.set_size_inches(5,16)
plt.savefig('D:/pics/myimg6.jpg',dpi=400)    
"""
"""if cv2.waitKey(0)==ord('q'):
    cv2.destroyAllWindows()
    """
    