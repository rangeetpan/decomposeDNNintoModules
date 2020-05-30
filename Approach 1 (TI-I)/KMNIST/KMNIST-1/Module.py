#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 12:47:48 2020

@author: 
"""
# In[]: Library
from utils.mnistutil import MNISTUitl
from utils.sliceutil import Slice
from keras.models import load_model
from datetime import datetime
import numpy as np
sx = 28
sy = 28
accuracyCheck=[]
# In[]: Data Acquisition and Model Training
# mn = MNISTUitl()
# X, Y, x, y = mn.getdata2(0,0,sx,sy)
# nm , xt, yt = mn.train2(X, Y, x,y,sx,sy,10,50)
# #X, Y, x, y = mn.getdata2(0,0,sx,sy)
# model , xt1, yt1 = mn.train2(X, Y, x,y,sx,sy,10,50)
labs = [0,1,2,3,4,5,6,7,8,9]
mn = MNISTUitl()
X, Y, x, y = mn.getdata2(0,0,sx,sy)
#nm , xt, yt = mn.train2(X, Y, x,y,sx,sy,10,20)
xt, yt = mn.trainData(X, Y, x,y,sx,sy,10,50)
# In[]: Module 0
test=[]
accuracyCheck=[]
nonDigit=[]
labs = [0,1,2,3,4,5,6,7,8,9]
labs1 = [0,1,2,3,4,5,6,7,8,9]
print("Start Time:"+datetime.now().strftime("%H:%M:%S"))
#nm.save('kmnist.h5')
for j in labs:
    print("#Module "+str(j)+" in progress....")
    #test=[]
    slicingModel=load_model('kmnist.h5')
    #X, Y, x, y = mn.getdata2(0,0,sx,sy)
    model=load_model('kmnist.h5')
    digit  = []
    slc = Slice()
    W1, W2, b1, b2 = slc.getweights(slicingModel)
    for i in range(0,len(yt)):
        if yt[i] == j and model.predict(xt[i:i+1])[0][j] >.9:
            digit.append(xt[i])
    #print(len(zero),len(Y))
    #np.random.shuffle(digit)
    digit = digit[0:1000]
    mc = 0
    for x in digit:
        W1, W2,b1,b2 = slc.modifyThroughInterSection(slicingModel,x,sx,sy)
        mc=mc+1
        if np.count_nonzero(slc.D2) < 45:
            #print("Breaking at mc ", mc,np.count_nonzero(slc.D2))
            slc.first = True
    digit=[]
    for k in labs1:
        if(k!=j):
            temp=xt[yt==k]
            temp=temp[0:1]
            for u in temp:
                digit.append(u)
    #digit = digit[0:200]
    np.random.shuffle(digit)
    mc = 0
    for x in digit:
        W1, W2,b1,b2 = slc.dynamicmodify(slicingModel,x,sx,sy)
        mc=mc+1
        if np.count_nonzero(slc.D2) < 45:
            #print("Breaking at mc ", mc,np.count_nonzero(slc.D2))
            slc.first = True
    #In[]: Verifiy
    #slc.backtrack(j)
    model.layers[1].set_weights([slc.D1,slc.d1])
    model.layers[2].set_weights([slc.D2,slc.d2])
    model.save('module'+str(j)+'.h5')
    #In[]:
    # from sklearn.metrics import accuracy_score
    # zeros = []
    # pred = []
    # tr = []
    # #labs = [0,1,2,3,4,5,6,7,8,9]
    # acc = []
    # count = 0
    # #for l in labs:
    # pred = []
    # tr = []
    # for i in range(0,len(yt)):
    # #for i in range(0,len(yt[0:500])):
    #     count += 1
    #     #if yt[i] == j:
    #     p = model.predict(xt[i:i+1])
    #     m = p.argmax()
    #     test.append(p)
    #     if(yt[i]!=j):
    #         tr.append(1)
    #         if(m!=j):
    #             pred.append(1)
    #         else:
    #             pred.append(0)
    #     else:
    #         if(m==j):
    #             pred.append(0)
    #         else:
    #             pred.append(1)
    #         tr.append(0)
    # score = accuracy_score(pred,tr)
    # acc.append(score)
    # accuracyCheck.append(score)

# # In[]:Module 1:
# mn = MNISTUitl()
# X, Y, x, y = mn.getdata2(0,0,sx,sy)
# nm , xt, yt = mn.train2(X, Y, x,y,sx,sy,10,50)
# #X, Y, x, y = mn.getdata2(0,0,sx,sy)
# model , xt1, yt1 = mn.train2(X, Y, x,y,sx,sy,10,50)
# zero  = []
# slc = Slice()
# W1, W2, b1, b2 = slc.getweights(nm)
# for i in range(0,len(Y)):
#     if Y[i] == 1:
#         zero.append(X[i])
# print(len(zero),len(Y))
# for x in zero:
#     W1, W2,b1,b2 = slc.dynamicmodify(nm,x,sx,sy)
# #In[]: Verifiy
# model.layers[1].set_weights([slc.D1,slc.d1])
# model.layers[2].set_weights([slc.D2,slc.d2])
# #In[]:
# from sklearn.metrics import accuracy_score
# zeros = []
# pred = []
# tr = []
# labs = [0,1,2,3,4,5,6,7,8,9]
# acc = []
# count = 0
# #for l in labs:
# pred = []
# tr = []
# for i in range(0,len(yt)):
#     count += 1
#     #if yt[i] == l:
#     p = model.predict(xt[i:i+1])
#     m = p.argmax()
#     if(yt[i]!=0):
#         tr.append(1)
#         if(pred!=0):
#             pred.append(1)
#         else:
#             pred.append(0)
#     else:
#         pred.append(m)
#         tr.append(0)
# score = accuracy_score(pred,tr)
# acc.append(score)
# accuracyCheck.append(score)
