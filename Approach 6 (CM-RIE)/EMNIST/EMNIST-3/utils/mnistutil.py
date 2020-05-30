'''
Created on Feb 8, 2019

@author:  
'''

from keras.datasets import mnist
from skimage.transform import resize
import numpy as np
from keras import backend as K
import keras
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D




class MNISTUitl:
    
    
    def __init__(self):
        self.name = None
    def load(self,f):
        return np.load(f)['arr_0']      
    def getdata(self,a,b,img_rows = 28, img_cols = 28):
    # the data, split between train and test sets
        (x_train, y_train), (x_test, y_test) = mnist.load_data()
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
    def getdata2(self,a,b,img_rows = 28, img_cols = 28):
    # the data, split between train and test sets
        x_train = self.load('emnist-train-imgs.npz')
        x_test = self.load('emnist-test-imgs.npz')
        y_train = self.load('emnist-train-labels.npz')
        for i in range(0,len(y_train)):
            y_train[i]=y_train[i]-1
        y_test = self.load('emnist-test-labels.npz')
        for i in range(0,len(y_test)):
            y_test[i]=y_test[i]-1
        x_zo = []
        y_zo = []
        for i in range(len(y_train)):
            if y_train[i] in [0,1,2,3,4,5,6,7,8,9]:
                A = resize(x_train[i], (img_rows,  img_cols),mode='constant')
                Ay = y_train[i]#resize(y_train[i], (img_rows, img_cols))
                x_zo.append(A)
                y_zo.append(Ay)
        xt_zo = []
        yt_zo = []
    
        for i in range(len(y_test)):
            if y_test[i] in [0,1,2,3,4,5,6,7,8,9]:
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
    def trainDense2(self,x_zo,y_zo,xt_zo,yt_zo,img_rows = 28, img_cols = 28,numclass = 10,ep = 20):
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
    def trainDense4(self,x_zo,y_zo,xt_zo,yt_zo,img_rows = 28, img_cols = 28,numclass = 10,ep = 20):
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
    def trainDense3(self,x_zo,y_zo,xt_zo,yt_zo,img_rows = 28, img_cols = 28,numclass = 10,ep = 20):
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
            keras.layers.Dense(numclass, activation=tf.nn.softmax, name = "output")
        ])
    
        nm.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        print(nm.summary())
        nm.fit(x_train, y_train, epochs=ep)
        return nm, x_test, y_test
    def trainDense6(self,x_zo,y_zo,xt_zo,yt_zo,img_rows = 28, img_cols = 28,numclass = 10,ep = 20):
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
    def trainData(self,x_zo,y_zo,xt_zo,yt_zo,img_rows = 28, img_cols = 28,numclass = 10,ep = 20):
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
        return x_test, y_test,x_train, y_train
    def train3(self,x_zo,y_zo,xt_zo,yt_zo,img_rows = 28, img_cols = 28,numclass = 10,ep = 20):
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