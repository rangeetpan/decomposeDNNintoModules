#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 09:49:54 2020

@author: 
"""
from keras.datasets import fashion_mnist
from keras.datasets import mnist
from skimage.transform import resize
import numpy as np
from keras import backend as K
import keras
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from sklearn.utils import shuffle

class1=1
class2=9
img_rows = 28
img_cols = 28
(x_train1, y_train1), (x_test1, y_test1) = fashion_mnist.load_data()
(x_train2, y_train2), (x_test2, y_test2) = mnist.load_data()
#train data change
x_train=x_train1[y_train1==class1]
x_train=np.append(x_train,x_train2[y_train2==class2], axis=0)
y_train=[]
for x in y_train1[y_train1==class1]:
    y_train.append(0)
y_train=np.array(y_train)
#y_train=np.append(y_train,temp)
temp=[]
for x in y_train2[y_train2==class2]:
    temp.append(1)
temp=np.array(temp)
y_train=np.append(y_train,temp)
x_train, y_train = shuffle(x_train, y_train, random_state=0)

x_test=x_test1[y_test1==class1] #test Data change
x_test=np.append(x_test,x_test2[y_test2==class2], axis=0)
y_test=y_test1[y_test1==class1]
temp=[]
for x in y_test2[y_test2==class2]:
    temp.append(class1+1)
temp=np.array(temp)
y_test=np.append(y_test,temp)
x_test, y_test = shuffle(x_test, y_test, random_state=0)

x_zo = []
y_zo = []
for i in range(len(y_train)):
    if y_train[i] in [class1, class1+1]:
        A = resize(x_train[i], (img_rows,  img_cols),mode='constant')
        Ay = y_train[i]#resize(y_train[i], (img_rows, img_cols))
        x_zo.append(A)
        y_zo.append(Ay)
xt_zo = []
yt_zo = []

for i in range(len(y_test)):
    if y_train[i] in [class1, class1+1]:
        A = resize(x_test[i], (img_rows,  img_cols),mode='constant')
        Ay = y_test[i]#resize(y_train[i], (img_rows, img_cols))
        xt_zo.append(A)
        yt_zo.append(Ay)
x_zo = np.array(x_zo)
y_zo = np.array(y_zo)
xt_zo = np.array(xt_zo)
yt_zo = np.array(yt_zo)