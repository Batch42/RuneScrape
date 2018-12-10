# Matthew Manoly, Steven Proctor, Harrison Ratcliffe, Zachary Taylor
# December 10th, 2018
# FinalModel.py
# A recurrent neural network used for forecasting prices in the RuneScape market

import numpy
import sys
import json
import tensorflow as tf
from keras.models import Sequential
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils

#read in the data and format it as sequences of 4 days at a time.
file = open("nowData").read()
file = json.loads(file)
x = []
y = []
for i in range(4,len(file)):
    oof = []
    oof.append(file[i-4])
    oof.append(file[i-3])
    oof.append(file[i-2])
    oof.append(file[i-1])
    x.append(oof)
    y.append(file[i])

model = Sequential()

#change arrays to numpy arrays
x = numpy.array(x)
y = numpy.array(y)

#adding 2 lstm layers. 3220 is the number of items in a day, return sequences will return the
#entire sequence rather than the final output.
model.add(LSTM(3220,return_sequences=True))
model.add(LSTM(3220))

#Custom accuracy metric. Approaches 0 as predictions are further off
def acc(x,y):
    return 1/(1+tf.reduce_sum(tf.abs(x-y)))

#compile and fit
model.compile(loss='mean_squared_error', optimizer='adam',metrics=[acc])
model.fit(x, y, epochs=350, batch_size=1, verbose=2)
