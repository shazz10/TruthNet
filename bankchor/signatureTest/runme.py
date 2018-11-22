from __future__ import absolute_import
from __future__ import print_function
import numpy as np
np.random.seed(1337)  # for reproducibility
import os

#from keras.utils.visualize_util import plot

import tensorflow as tf
from keras.callbacks import ModelCheckpoint, TensorBoard
from keras.layers import Dense, Dropout, Input, Lambda, Flatten, Convolution2D, MaxPooling2D, ZeroPadding2D
from keras.preprocessing import image
from keras import backend as K
import sys
import glob
import logging
from keras.models import Sequential, Model
from keras.optimizers import SGD, RMSprop, Adadelta
from keras.layers.normalization import BatchNormalization
from keras.regularizers import l2
import random
import itertools
from keras.models import model_from_yaml
random.seed(1337)

# Create a session for running Ops on the Graph.
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.Session(config=config)
K.set_session(sess)

logging.basicConfig(level=logging.WARNING)
log = logging.getLogger()

def euclidean_distance(vects):
    x, y = vects
    return K.sqrt(K.sum(K.square(x - y), axis=1, keepdims=True))

def eucl_dist_output_shape(shapes):
    shape1, shape2 = shapes
    return (shape1[0], 1)

def contrastive_loss(y_true, y_pred):
    margin = 1
    return K.mean(y_true * K.square(y_pred) + (1 - y_true) * K.square(K.maximum(margin - y_pred, 0)))

def format_input(X):
    if not(type(X) is np.ndarray):   
        X = np.array(X)
        print ('Formatted input by converting to array')
    try:
        print ('Input shape before reshaping:   ', X.shape)
        # X = X.reshape(X.shape[0], X.shape[1], img_height, img_width, 1)
        X = X.reshape(X.shape[0], img_height, img_width, 1)
        X = X.astype('float32')
        X /= 255

        return X
    except Exception as e:
        print ('EXCEPTION while reshaping and formatting input data X:  \n', e)
        print (log.exception('ERROR MESSAGE'))

img_height = 155
img_width = 220
featurewise_std_normalization = True
input_shape=(img_height, img_width, 1)

yaml_file = open('model3.yaml', 'r')
loaded_model_yaml = yaml_file.read()
yaml_file.close()
loaded_model = model_from_yaml(loaded_model_yaml)
loaded_model.load_weights("model2.h5")
print("Loaded model from disk")
rms = RMSprop(lr=1e-4, rho=0.9, epsilon=1e-08)
adadelta = Adadelta()
loaded_model.compile(loss=contrastive_loss, optimizer=rms)

def predict():
    pred=loaded_model.predict([pair[:,0], pair[:,1]])
    if pred<9:
        return True
    return False