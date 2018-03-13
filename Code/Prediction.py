import keras
from keras.layers import Conv2D, Conv2DTranspose, UpSampling2D
from keras.layers import Activation, Dense, Dropout, Flatten, InputLayer
from keras.layers.normalization import BatchNormalization
from keras.callbacks import TensorBoard
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from skimage.color import rgb2lab, lab2rgb, rgb2gray
from skimage.io import imsave
import numpy as np
import os
import random
import tensorflow as tf
from keras.models import load_model

def predict(file):
    model = load_model('model.h5')
    global color_name
    color_me = []
    color_me.append(img_to_array(load_img(file)))
    color_me = np.array(color_me, dtype=float)
    color_me = rgb2lab(1.0/255*color_me)[:,:,:,0]
    color_me = color_me.reshape(color_me.shape+(1,))
    # Test model
    output = model.predict(color_me)
    output = output * 128
    # Output colorizations
    for i in range(len(output)):
            cur = np.zeros((256, 256, 3))
            cur[:,:,0] = color_me[i][:,:,0]
            cur[:,:,1:] = output[i]
            return lab2rgb(cur)
            #imsave("img"+str(i)+".png", lab2rgb(cur))
#predict('greyscale1.png')
