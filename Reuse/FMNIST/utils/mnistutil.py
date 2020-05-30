'''
Created on Feb 8, 2019

@author:  
'''

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




class MNISTUitl:
    
    
    def __init__(self):
        self.name = None
        
    def getdata(self,a,b,img_rows = 28, img_cols = 28):
    # the data, split between train and test sets
        (x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
        x_zo = []
        y_zo = []
        for i in range(len(y_train)):
            if y_train[i] == a or y_train[i] == b:
                A = resize(x_train[i], (img_rows,  img_cols),mode='constant')
                Ay = y_train[i]#resize(y_train[i], (img_rows, img_cols))
                x_zo.append(A)
                y_zo.append(Ay)
        xt_zo = []
        yt_zo = []
    
        for i in range(len(y_test)):
            if y_test[i] == a or y_test[i] == b:
                A = resize(x_test[i], (img_rows,  img_cols),mode='constant')
                Ay = y_test[i]#resize(y_train[i], (img_rows, img_cols))
                xt_zo.append(A)
                yt_zo.append(Ay)
        x_zo = np.array(x_zo)
        y_zo = np.array(y_zo)
        xt_zo = np.array(xt_zo)
        yt_zo = np.array(yt_zo)
        return x_zo, y_zo, xt_zo, yt_zo
    def getdata2(self,a,b,class1,class2,img_rows = 28, img_cols = 28):
    # the data, split between train and test sets
        (x_train1, y_train1), (x_test1, y_test1) = fashion_mnist.load_data()
        (x_train2, y_train2), (x_test2, y_test2) = fashion_mnist.load_data()
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
        y_test=[]
        for x in y_test1[y_test1==class1]:
            y_test.append(0)
        y_test=np.array(y_test)
        temp=[]
        for x in y_test2[y_test2==class2]:
            temp.append(1)
        temp=np.array(temp)
        y_test=np.append(y_test,temp)
        x_test, y_test = shuffle(x_test, y_test, random_state=0)
        
        x_zo = []
        y_zo = []
        for i in range(len(y_train)):
            if y_train[i] in [0, 1]:
                A = resize(x_train[i], (img_rows,  img_cols),mode='constant')
                Ay = y_train[i]#resize(y_train[i], (img_rows, img_cols))
                x_zo.append(A)
                y_zo.append(Ay)
        xt_zo = []
        yt_zo = []
        
        for i in range(len(y_test)):
            if y_test[i] in [0, 1]:
                A = resize(x_test[i], (img_rows,  img_cols),mode='constant')
                Ay = y_test[i]#resize(y_train[i], (img_rows, img_cols))
                xt_zo.append(A)
                yt_zo.append(Ay)
        x_zo = np.array(x_zo)
        y_zo = np.array(y_zo)
        xt_zo = np.array(xt_zo)
        yt_zo = np.array(yt_zo)
        return x_zo, y_zo, xt_zo, yt_zo    
    def getdataTrain(self,a,b,class1,class2,img_rows = 28, img_cols = 28):
    # the data, split between train and test sets
        (x_train1, y_train1), (x_test1, y_test1) = fashion_mnist.load_data()
        (x_train2, y_train2), (x_test2, y_test2) = fashion_mnist.load_data()
        #train data change
        x_train=x_train1[y_train1==class1]
        x_train=np.append(x_train,x_train2[y_train2==class2], axis=0)
        y_train=[]
        for x in y_train1[y_train1==class1]:
            y_train.append(x)
        y_train=np.array(y_train)
        #y_train=np.append(y_train,temp)
        temp=[]
        for x in y_train2[y_train2==class2]:
            temp.append(x)
        temp=np.array(temp)
        y_train=np.append(y_train,temp)
        x_train, y_train = shuffle(x_train, y_train, random_state=0)
        
        x_test=x_test1[y_test1==class1] #test Data change
        x_test=np.append(x_test,x_test2[y_test2==class2], axis=0)
        y_test=[]
        for x in y_test1[y_test1==class1]:
            y_test.append(x)
        y_test=np.array(y_test)
        temp=[]
        for x in y_test2[y_test2==class2]:
            temp.append(x)
        temp=np.array(temp)
        y_test=np.append(y_test,temp)
        x_test, y_test = shuffle(x_test, y_test, random_state=0)
        
        x_zo = []
        y_zo = []
        for i in range(len(y_train)):
            if y_train[i] in [class1, class2]:
                A = resize(x_train[i], (img_rows,  img_cols),mode='constant')
                Ay = y_train[i]#resize(y_train[i], (img_rows, img_cols))
                x_zo.append(A)
                y_zo.append(Ay)
        xt_zo = []
        yt_zo = []
        
        for i in range(len(y_test)):
            if y_test[i] in [class1, class2]:
                A = resize(x_test[i], (img_rows,  img_cols),mode='constant')
                Ay = y_test[i]#resize(y_train[i], (img_rows, img_cols))
                xt_zo.append(A)
                yt_zo.append(Ay)
        x_zo = np.array(x_zo)
        y_zo = np.array(y_zo)
        xt_zo = np.array(xt_zo)
        yt_zo = np.array(yt_zo)
        return x_zo, y_zo, xt_zo, yt_zo    
    def train(self,x_zo,y_zo,xt_zo,yt_zo,img_rows = 28, img_cols = 28,numclass = 2):
        if K.image_data_format() == 'channels_first':
            x_zo = x_zo.reshape(x_zo.shape[0], 1, img_rows, img_cols)
            xt_zo = xt_zo.reshape(xt_zo.shape[0], 1, img_rows, img_cols)
            input_shape = (1, img_rows, img_cols)
        else:
            x_zo = x_zo.reshape(x_zo.shape[0], img_rows, img_cols, 1)
            xt_zo = xt_zo.reshape(xt_zo.shape[0], img_rows, img_cols, 1)
            input_shape = (img_rows, img_cols, 1)
    
        x_train = x_zo.astype('float32')
        x_test = xt_zo.astype('float32')
        x_train /= 255
        x_test /= 255
        print('x_train shape:', x_train.shape)
        print(x_zo.shape,x_train.shape[0], 'train samples', y_zo.shape)
        print(x_test.shape[0], 'test samples')
    
        y_train = y_zo#keras.utils.to_categorical(y_zo, numclass )
        y_test =  yt_zo#keras.utils.to_categorical(yt_zo, numclass)
    
        print(y_zo.shape,y_train.shape)
        nm = keras.Sequential([
            keras.layers.Flatten(input_shape=(img_rows, img_cols,1), name = "Input"),
            keras.layers.Dense(7, activation=tf.nn.relu ,name = "H"),
            keras.layers.Dense(numclass, activation=tf.nn.softmax, name = "output")
        ])
    
        nm.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
    
        nm.fit(x_train, y_train, epochs=10)
        return nm, x_test, y_test
    def train2(self,x_zo,y_zo,xt_zo,yt_zo,img_rows = 28, img_cols = 28,numclass = 10,ep = 20):
        if K.image_data_format() == 'channels_first':
            x_zo = x_zo.reshape(x_zo.shape[0], 1, img_rows, img_cols)
            xt_zo = xt_zo.reshape(xt_zo.shape[0], 1, img_rows, img_cols)
            input_shape = (1, img_rows, img_cols)
        else:
            x_zo = x_zo.reshape(x_zo.shape[0], img_rows, img_cols, 1)
            xt_zo = xt_zo.reshape(xt_zo.shape[0], img_rows, img_cols, 1)
            input_shape = (img_rows, img_cols, 1)
    
        x_train = x_zo.astype('float32')
        x_test = xt_zo.astype('float32')
        x_train /= 255
        x_test /= 255
        print('x_train shape:', x_train.shape)
        print(x_zo.shape,x_train.shape[0], 'train samples', y_zo.shape)
        print(x_test.shape[0], 'test samples')
    
        y_train = y_zo #keras.utils.to_categorical(y_zo, numclass )
        y_test =  yt_zo #keras.utils.to_categorical(yt_zo, numclass)
    
        print(y_zo.shape,y_train.shape)
        nm = keras.Sequential([
            keras.layers.Flatten(input_shape=(img_rows, img_cols,1), name = "Input"),
            keras.layers.Dense(49, activation=tf.nn.relu ,name = "H"),
            keras.layers.Dense(numclass, activation=tf.nn.softmax, name = "output")
        ])
    
        nm.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        print(nm.summary())
        nm.fit(x_train, y_train, epochs=ep)
        return nm, x_test, y_test
    def trainData(self,x_zo,y_zo,xt_zo,yt_zo,img_rows = 28, img_cols = 28,numclass = 2,ep = 20):
        if K.image_data_format() == 'channels_first':
            x_zo = x_zo.reshape(x_zo.shape[0], 1, img_rows, img_cols)
            xt_zo = xt_zo.reshape(xt_zo.shape[0], 1, img_rows, img_cols)
            input_shape = (1, img_rows, img_cols)
        else:
            x_zo = x_zo.reshape(x_zo.shape[0], img_rows, img_cols, 1)
            xt_zo = xt_zo.reshape(xt_zo.shape[0], img_rows, img_cols, 1)
            input_shape = (img_rows, img_cols, 1)
    
        x_train = x_zo.astype('float32')
        x_test = xt_zo.astype('float32')
        x_train /= 255
        x_test /= 255
        print('x_train shape:', x_train.shape)
        print(x_zo.shape,x_train.shape[0], 'train samples', y_zo.shape)
        print(x_test.shape[0], 'test samples')
    
        y_train = y_zo #keras.utils.to_categorical(y_zo, numclass )
        y_test =  yt_zo #keras.utils.to_categorical(yt_zo, numclass)
    
        print(y_zo.shape,y_train.shape)
        # nm = keras.Sequential([
        #     keras.layers.Flatten(input_shape=(img_rows, img_cols,1), name = "Input"),
        #     keras.layers.Dense(49, activation=tf.nn.relu ,name = "H"),
        #     keras.layers.Dense(numclass, activation=tf.nn.softmax, name = "output")
        # ])
    
        # nm.compile(optimizer='adam',
        #               loss='sparse_categorical_crossentropy',
        #               metrics=['accuracy'])
        # print(nm.summary())
        # nm.fit(x_train, y_train, epochs=ep)
        return x_test, y_test
    def train3(self,x_zo,y_zo,xt_zo,yt_zo,img_rows = 28, img_cols = 28,numclass = 2,ep = 20):
        input_shape = (img_rows,img_cols,1)
        x_zo = x_zo.reshape(x_zo.shape[0], img_rows, img_cols, 1)
        xt_zo = xt_zo.reshape(xt_zo.shape[0], img_rows, img_cols, 1)
        x_train = x_zo.astype('float32')
        x_test = xt_zo.astype('float32')
        x_train /= 255
        x_test /= 255
        y_train = keras.utils.to_categorical(y_zo, numclass )
        y_test =  keras.utils.to_categorical(yt_zo, numclass)
        num_classes = 10
        model = Sequential()
        model.add(Conv2D(32, kernel_size=(3, 3),
                         activation='relu',
                         input_shape=input_shape))
        model.add(Conv2D(64, (3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        #model.add(Dropout(0.25))
        model.add(Flatten())
        model.add(Dense(128, activation='relu'))
        #model.add(Dropout(0.5))
        model.add(Dense(num_classes, activation='softmax'))
        model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])
        model.fit(x_train, y_train, epochs=ep)
        return model, x_test, y_test
    def trainDense2(self,x_zo,y_zo,xt_zo,yt_zo,img_rows = 28, img_cols = 28,numclass = 2,ep = 20):
        if K.image_data_format() == 'channels_first':
            x_zo = x_zo.reshape(x_zo.shape[0], 1, img_rows, img_cols)
            xt_zo = xt_zo.reshape(xt_zo.shape[0], 1, img_rows, img_cols)
            input_shape = (1, img_rows, img_cols)
        else:
            x_zo = x_zo.reshape(x_zo.shape[0], img_rows, img_cols, 1)
            xt_zo = xt_zo.reshape(xt_zo.shape[0], img_rows, img_cols, 1)
            input_shape = (img_rows, img_cols, 1)
    
        x_train = x_zo.astype('float32')
        x_test = xt_zo.astype('float32')
        x_train /= 255
        x_test /= 255
        print('x_train shape:', x_train.shape)
        print(x_zo.shape,x_train.shape[0], 'train samples', y_zo.shape)
        print(x_test.shape[0], 'test samples')
    
        y_train = y_zo #keras.utils.to_categorical(y_zo, numclass )
        y_test =  yt_zo #keras.utils.to_categorical(yt_zo, numclass)
    
        print(y_zo.shape,y_train.shape)
        nm = keras.Sequential([
            keras.layers.Flatten(input_shape=(img_rows, img_cols,1), name = "Input"),
            keras.layers.Dense(49, activation=tf.nn.relu ,name = "H1"),
            keras.layers.Dense(49, activation=tf.nn.relu ,name = "H2"),
            keras.layers.Dense(numclass, activation=tf.nn.softmax, name = "output")
        ])
    
        nm.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        print(nm.summary())
        nm.fit(x_train, y_train, epochs=ep)
        return nm, x_test, y_test
    def trainDense4(self,x_zo,y_zo,xt_zo,yt_zo,img_rows = 28, img_cols = 28,numclass = 2,ep = 10):
        if K.image_data_format() == 'channels_first':
            x_zo = x_zo.reshape(x_zo.shape[0], 1, img_rows, img_cols)
            xt_zo = xt_zo.reshape(xt_zo.shape[0], 1, img_rows, img_cols)
            input_shape = (1, img_rows, img_cols)
        else:
            x_zo = x_zo.reshape(x_zo.shape[0], img_rows, img_cols, 1)
            xt_zo = xt_zo.reshape(xt_zo.shape[0], img_rows, img_cols, 1)
            input_shape = (img_rows, img_cols, 1)
    
        x_train = x_zo.astype('float32')
        x_test = xt_zo.astype('float32')
        x_train /= 255
        x_test /= 255
        print('x_train shape:', x_train.shape)
        print(x_zo.shape,x_train.shape[0], 'train samples', y_zo.shape)
        print(x_test.shape[0], 'test samples')
    
        y_train = y_zo #keras.utils.to_categorical(y_zo, numclass )
        y_test =  yt_zo #keras.utils.to_categorical(yt_zo, numclass)
    
        print(y_zo.shape,y_train.shape)
        nm = keras.Sequential([
            keras.layers.Flatten(input_shape=(img_rows, img_cols,1), name = "Input"),
            keras.layers.Dense(49, activation=tf.nn.relu ,name = "H1"),
            keras.layers.Dense(49, activation=tf.nn.relu ,name = "H2"),
            keras.layers.Dense(49, activation=tf.nn.relu ,name = "H3"),
            keras.layers.Dense(49, activation=tf.nn.relu ,name = "H4"),
            keras.layers.Dense(numclass, activation=tf.nn.softmax, name = "output")
        ])
    
        nm.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        print(nm.summary())
        nm.fit(x_train, y_train, epochs=ep)
        return nm, x_test, y_test
    def trainDense6(self,x_zo,y_zo,xt_zo,yt_zo,img_rows = 28, img_cols = 28,numclass = 2,ep = 10):
        if K.image_data_format() == 'channels_first':
            x_zo = x_zo.reshape(x_zo.shape[0], 1, img_rows, img_cols)
            xt_zo = xt_zo.reshape(xt_zo.shape[0], 1, img_rows, img_cols)
            input_shape = (1, img_rows, img_cols)
        else:
            x_zo = x_zo.reshape(x_zo.shape[0], img_rows, img_cols, 1)
            xt_zo = xt_zo.reshape(xt_zo.shape[0], img_rows, img_cols, 1)
            input_shape = (img_rows, img_cols, 1)
    
        x_train = x_zo.astype('float32')
        x_test = xt_zo.astype('float32')
        x_train /= 255
        x_test /= 255
        print('x_train shape:', x_train.shape)
        print(x_zo.shape,x_train.shape[0], 'train samples', y_zo.shape)
        print(x_test.shape[0], 'test samples')
    
        y_train = y_zo #keras.utils.to_categorical(y_zo, numclass )
        y_test =  yt_zo #keras.utils.to_categorical(yt_zo, numclass)
    
        print(y_zo.shape,y_train.shape)
        nm = keras.Sequential([
            keras.layers.Flatten(input_shape=(img_rows, img_cols,1), name = "Input"),
            keras.layers.Dense(49, activation=tf.nn.relu ,name = "H1"),
            keras.layers.Dense(49, activation=tf.nn.relu ,name = "H2"),
            keras.layers.Dense(49, activation=tf.nn.relu ,name = "H3"),
            keras.layers.Dense(49, activation=tf.nn.relu ,name = "H4"),
            keras.layers.Dense(49, activation=tf.nn.relu ,name = "H5"),
            keras.layers.Dense(49, activation=tf.nn.relu ,name = "H6"),
            keras.layers.Dense(numclass, activation=tf.nn.softmax, name = "output")
        ])
    
        nm.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        print(nm.summary())
        nm.fit(x_train, y_train, epochs=ep)
        return nm, x_test, y_test