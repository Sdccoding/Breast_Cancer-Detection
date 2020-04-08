# -*- coding: utf-8 -*-
"""Breast_Cancer_CNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GDtHkapkYYQ_GM7mNikb4BTb4O0X5TlI
"""

pip install tensorflow-gpu==2.0.0-rc0

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Flatten,Dense,Dropout,BatchNormalization
from tensorflow.keras.layers import Conv1D,MaxPool1D
from tensorflow.keras.optimizers import Adam
print(tf.__version__)

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets,metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = datasets.load_breast_cancer()
print(df.DESCR)

x=pd.DataFrame(data=df.data,columns=df.feature_names)
x.head()

y=df.target
y

df.target_names

x.shape

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0,stratify=y)
x_train.shape

#Standardization
scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.transform(x_test)

x_test.shape

#Reshaping
x_train=x_train.reshape(455,30,1)
x_test=x_test.reshape(114,30,1)

x_train.shape

#Convolutional layers.
epochs= 50
model=Sequential()
model.add(Conv1D(filters=32,kernel_size=2,activation='relu',input_shape=(30,1)))
model.add(BatchNormalization())
model.add(Dropout(0.2))


model.add(Conv1D(filters=64,kernel_size=2,activation='relu',input_shape=(30,1)))
model.add(BatchNormalization())
model.add(Dropout(0.5))
#Flattening and then hideen
model.add(Flatten())
model.add(Dense(64,activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(1,activation='sigmoid'))

x_train.shape

model.summary()

model.compile(optimizer=Adam(lr=0.00005),loss='binary_crossentropy',metrics=['accuracy'])

history=model.fit(x_train,y_train,epochs=epochs, validation_data=(x_test,y_test),verbose=1)

val_loss,val_acc=model.evaluate(x_test,y_test)
print(val_loss,val_acc)

model.save('Mymodel.h5')

model.save_weights('weights.h5')