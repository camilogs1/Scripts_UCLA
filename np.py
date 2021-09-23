# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 18:10:07 2021

@author: bryan
"""

import numpy as np

arreglo1 = np.array([1,2,3,4,5])

vector1 = np.zeros(2)

vector2 = np.arange()

#------------------------------------

import matplotlib.pyplot as plt

puntos = 10

f=10

t = np.linspace(0,10,puntos)

t= np.arange(0,10,0.1111)
w = 2*np.pi*f
y=5*np.sin(w*t)

plt.plot(t,y)

vector = [1,2]

vector = arreglo1

#-----------------------------------

img = np.random.rand(50,50)

img[:5]=0
img[0:50,0:5]=0
img[0:50,45:50]=0
img[45:50,0:50]=0
img[10:20,30:40]=0
img[10:20,10:20]=0
img[32:40,15:35]=0
img[28:38,35:40]=0
img[28:38,10:15]=0
plt.imshow(img, cmap=plt.cm.hot)
plt.show()




