import io
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow import keras
from tensorflow.keras import layers
from keras.layers import Dense, Activation
from keras.models import Sequential

model = Sequential()
model.add(Dense(32, input_shape=(500,)))

# model = Sequential([
#     Dense(5, input_shape(3,), activation='relu'),
#     Dense(2, activation='softmax')
# ])
