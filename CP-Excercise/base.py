num_of_coordinates = 84
img_size = 112
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import PIL
import cv2
import os
from pathlib import Path
from tensorflow.train import latest_checkpoint

from tensorflow import keras
from tensorflow.keras.applications import VGG16
from tensorflow.keras.layers import Dropout, Conv2D, Input
from tensorflow.keras.models import Model
from keras.callbacks import EarlyStopping, ModelCheckpoint, Callback
from tensorflow.keras.optimizers import Adam,SGD,RMSprop
#import visualkeras
from tensorflow.keras.utils import plot_model
from keras.applications.vgg16 import preprocess_input
from sklearn.metrics import accuracy_score

basemodel = VGG16(input_shape=(img_size, img_size, 3), weights='imagenet', include_top=False)

basemodel.trainable = True

inputs = Input(shape=(img_size, img_size, 3), name="InputLayer")
inputs = preprocess_input(inputs)
var = basemodel(inputs)

var = Conv2D(84, kernel_size=3, activation='relu', name="Conv")(var)
outputs = Conv2D(84, kernel_size=1, activation='sigmoid', name="OutputLayer")(var)

model_vgg = Model(inputs, outputs)