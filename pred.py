import tensorflow as tf
from tensorflow import keras
import os
from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.metrics import categorical_crossentropy
from keras.models import Sequential, Model
from keras.layers import Conv2D, MaxPooling2D,GlobalAveragePooling2D
from keras.layers import Activation, Dropout, BatchNormalization, Flatten, Dense, AvgPool2D,MaxPool2D
from keras.models import Sequential, Model
import cv2



def Cancerprediction(input):
    image = cv2.imread(input)

    model = tf.keras.models.load_model('C:\\Users\\Mahi\\Desktop\\Canpred\\model_m.h5')
    image_fromarray = Image.fromarray(image, 'RGB')
    resize_image = image_fromarray.resize((224, 224))
    expand_input = np.expand_dims(resize_image,axis=0)
    input_data = np.array(expand_input)
    input_data = input_data/255

    pred = model.predict(input_data)
    if pred >= 0.5:
        return "Yes"
    else:
        return "No"
