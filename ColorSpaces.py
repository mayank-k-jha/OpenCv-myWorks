# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 00:43:20 2017

@author: mayank
"""

import cv2
import numpy as np

cv2.imwrite('D:/pics/tom_and_jerry_laying-1440x900_m.jpg',cv2.resize(cv2.imread(input("Enter image to resize")),(1440,900)))
