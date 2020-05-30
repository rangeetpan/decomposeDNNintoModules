#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 21:38:03 2020

@author: 
"""
from utils.mnistutil import MNISTUitl
#from utils.sliceutil import Slice
from keras.models import load_model
#import numpy as np
#Module Load
labs = [0,1,2,3,4,5,6,7,8,9]
labs1 = [0,1,2,3,4,5,6,7,8,9]
module=[]
accuracy=[]
class1=0
class2=0
for k in range(0,10):
    for j in range(0,10):
        #print("class1a: "+str(class1))
        class1=k
        class2=j
        #print("class1: "+str(class1))
        if(class2==0):
            Mmodule0=load_model('Mmodule0.h5')
        if(class2==1):
            Mmodule0=load_model('Mmodule1.h5')
        if(class2==2):
            Mmodule0=load_model('Mmodule2.h5')
        if(class2==3):
            Mmodule0=load_model('Mmodule3.h5')
        if(class2==4):
            Mmodule0=load_model('Mmodule4.h5')
        if(class2==5):
            Mmodule0=load_model('Mmodule5.h5')
        if(class2==6):
            Mmodule0=load_model('Mmodule6.h5')
        if(class2==7):
            Mmodule0=load_model('Mmodule7.h5')
        if(class2==8):
            Mmodule0=load_model('Mmodule8.h5')
        if(class2==9):
            Mmodule0=load_model('Mmodule9.h5')

        if(class1==0):
            Fmodule0=load_model('Emodule0.h5')
        if(class1==1):
            Fmodule0=load_model('Emodule1.h5')
        if(class1==2):
            Fmodule0=load_model('Emodule2.h5')
        if(class1==3):
            Fmodule0=load_model('Emodule3.h5')
        if(class1==4):
            Fmodule0=load_model('Emodule4.h5')
        if(class1==5):
            Fmodule0=load_model('Emodule5.h5')
        if(class1==6):
            Fmodule0=load_model('Emodule6.h5')
        if(class1==7):
            Fmodule0=load_model('Emodule7.h5')
        if(class1==8):
            Fmodule0=load_model('Emodule8.h5')
        if(class1==9):
            Fmodule0=load_model('Emodule9.h5')
        sx = 28
        sy = 28
        # class1=0
        # class2=0
        mn = MNISTUitl()
        X, Y, x, y = mn.getdata2(0,0,class1,class2,sx,sy)
        #nm , xt, yt = mn.train2(X, Y, x,y,sx,sy,10,50)
        xt, yt = mn.trainData(X, Y, x,y,sx,sy,10,50)
        #In[]: Parallel execution of modules
        finalPred=[]
        for i in range(0,len(yt)):
            #M0 prediction
            Fpred = Fmodule0.predict(xt[i:i+1])
            maxPredF= Fpred.argmax()
            if(maxPredF!=class1):
                maxPredF=11
            #M1 prediction
            Mpred = Mmodule0.predict(xt[i:i+1])
            maxPredM= Mpred.argmax()
            if(maxPredM!=class2):
                maxPredM=11
            # #M2 prediction
            # pred2 = module2.predict(xt[i:i+1])
            # maxPred2= pred2.argmax()
            # if(maxPred2!=2):
            #     maxPred2=10
            # #M3 prediction
            # pred3 = module3.predict(xt[i:i+1])
            # maxPred3= pred3.argmax()
            # if(maxPred3!=3):
            #     maxPred3=10
            # #M4 prediction
            # pred4 = module4.predict(xt[i:i+1])
            # maxPred4= pred4.argmax()
            # if(maxPred4!=4):
            #     maxPred4=10
            # #M5 prediction
            # pred5 = module5.predict(xt[i:i+1])
            # maxPred5= pred5.argmax()
            # if(maxPred5!=5):
            #     maxPred5=10
            # #M6 prediction
            # pred6 = module6.predict(xt[i:i+1])
            # maxPred6= pred6.argmax()
            # if(maxPred6!=6):
            #     maxPred6=10
            # #M7 prediction
            # pred7 = module7.predict(xt[i:i+1])
            # maxPred7= pred7.argmax()
            # if(maxPred7!=7):
            #     maxPred7=10
            # #M8 prediction
            # pred8 = module8.predict(xt[i:i+1])
            # maxPred8= pred8.argmax()
            # if(maxPred8!=8):
            #     maxPred8=10
            # #M9 prediction
            # pred9 = module9.predict(xt[i:i+1])
            # maxPred9= pred9.argmax()
            # if(maxPred9!=9):
            #     maxPred9=10
        #In[]: compute accuracy
            pred=[]
            pred.append(maxPredF)
            pred.append(maxPredM)
            # pred.append(maxPred2)
            # pred.append(maxPred3)
            # pred.append(maxPred4)
            # pred.append(maxPred5)
            # pred.append(maxPred6)
            # pred.append(maxPred7)
            # pred.append(maxPred8)
            # pred.append(maxPred9)
        #In[]:
        #pred=np.array(pred)
        #Case 1: if all of them are negative
            if(pred.count(11)==2):
                maxPrediction=[]
                maxPrediction.append(Mpred[0][class1])
                maxPrediction.append(Fpred[0][class2])
                # maxPrediction.append(pred2[0][2])
                # maxPrediction.append(pred3[0][3])
                # maxPrediction.append(pred4[0][4])
                # maxPrediction.append(pred5[0][5])
                # maxPrediction.append(pred6[0][6])
                # maxPrediction.append(pred7[0][7])
                # maxPrediction.append(pred8[0][8])
                # maxPrediction.append(pred9[0][9])
                finalPred.append(maxPrediction.index(max(maxPrediction)))
             # More than one vote
            elif (pred.count(11)==0):
                maxPrediction=[]
                maxPrediction.append(Mpred[0][class1])
                maxPrediction.append(Fpred[0][class2])
                # maxPrediction.append(pred2[0][2])
                # maxPrediction.append(pred3[0][3])
                # maxPrediction.append(pred4[0][4])
                # maxPrediction.append(pred5[0][5])
                # maxPrediction.append(pred6[0][6])
                # maxPrediction.append(pred7[0][7])
                # maxPrediction.append(pred8[0][8])
                # maxPrediction.append(pred9[0][9])
                argPred=[]
                valPred=[]
                #if(pred[0]!=11):
                valPred.append(maxPrediction[0])
                #if(pred[1]!=11):
                valPred.append(maxPrediction[1])
                # for i in pred:
                #     if(i!=11):
                #         valPred.append(maxPrediction[i])
                        #argPred.append(i)
                finalPred.append(maxPrediction.index(max(valPred)) )
            #Case 3: One vote
            elif(pred.count(11)==1):
                # for i in pred:
                #     if(i!=10):
                #        finalPred.append(i)
                if(pred[0]==class1):
                    finalPred.append(0)
                if(pred[1]==class2):
                    finalPred.append(1)
        #In[]
        from sklearn.metrics import accuracy_score
        score = accuracy_score(finalPred,yt)
        print("Modularized Accuracy: "+str(score))
        #acc.append(score)
        module.append([class1,class2])
        #print("class1: "+str(class1))
        accuracy.append(score)
with open("outputSequence.txt", "w") as txt_file:
    for line in module:
        txt_file.write(" ".join(str(line)) + "\n")
with open("outputAcc.txt", "w") as txt_file:
    for line in accuracy:
        txt_file.write(str(line) + "\n")
