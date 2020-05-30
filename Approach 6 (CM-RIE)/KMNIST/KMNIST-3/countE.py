#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 21:08:21 2020

@author: 
"""

from utils.mnistutil import MNISTUitl
from utils.sliceutil import Slice
from keras.models import load_model
import numpy as np
#Module Load
def computeEdge(hidden):
    inputE=784*49
    hiddenE=0
    for i in range(0,hidden-1):
        hiddenE+=49*49
    outputE=49*10
    totalE=inputE+hiddenE+outputE
    return totalE

module0=load_model('module0.h5')
module1=load_model('module1.h5')
module2=load_model('module2.h5')
module3=load_model('module3.h5')
module4=load_model('module4.h5')
module5=load_model('module5.h5')
module6=load_model('module6.h5')
module7=load_model('module7.h5')
module8=load_model('module8.h5')
module9=load_model('module9.h5')
countM0=0
countM1=0
countM2=0
countM3=0
countM4=0
countM5=0
countM6=0
countM7=0
countM8=0
countM9=0
networkE=computeEdge(1)
slc = Slice()
W1, W2, b1, b2 = slc.getweights(module0)
countM0=(np.count_nonzero(W1)+np.count_nonzero(W2))/networkE

W1, W2, b1, b2 = slc.getweights(module1)
countM1=(np.count_nonzero(W1)+np.count_nonzero(W2))/networkE

W1, W2, b1, b2 = slc.getweights(module2)
countM2=(np.count_nonzero(W1)+np.count_nonzero(W2))/networkE

W1, W2, b1, b2 = slc.getweights(module3)
countM3=(np.count_nonzero(W1)+np.count_nonzero(W2))/networkE

W1, W2, b1, b2 = slc.getweights(module4)
countM4=(np.count_nonzero(W1)+np.count_nonzero(W2))/networkE

W1, W2, b1, b2 = slc.getweights(module5)
countM5=(np.count_nonzero(W1)+np.count_nonzero(W2))/networkE

W1, W2, b1, b2 = slc.getweights(module6)
countM6=(np.count_nonzero(W1)+np.count_nonzero(W2))/networkE

W1, W2, b1, b2 = slc.getweights(module7)
countM7=(np.count_nonzero(W1)+np.count_nonzero(W2))/networkE

W1, W2, b1, b2 = slc.getweights(module8)
countM8=(np.count_nonzero(W1)+np.count_nonzero(W2))/networkE

W1, W2, b1, b2 = slc.getweights(module9)
countM9=(np.count_nonzero(W1)+np.count_nonzero(W2))/networkE
print ("avg nonzero nodes:"+str((countM0+countM0+countM0+countM0+countM0+countM0+countM0+countM0+countM0)/10))