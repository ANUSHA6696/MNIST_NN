# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 13:19:58 2021

@author: anusha Uni
"""

#Image classification using MNIST dataset
from tensorflow.keras.datasets import mnist
from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras.utils import to_categorical 


(train_images,train_labels),(test_images, test_labels) = mnist.load_data()
train_images = train_images.reshape(60000,28*28) #converting the images to float32 between 0 and 1
train_images = train_images.astype('float32')/255

test_images = test_images.reshape(10000,28*28) #converting the images to float32 between 0 and 1
test_images = test_images.astype('float32')/255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

network = models.Sequential()
network.add(layers.Dense(512, activation='relu' , input_shape = (28*28,)))
network.add(layers.Dense(10, activation='softmax'))

            
network.compile(optimizer='rmsprop', loss='categorical_crossentropy',metrics=['accuracy'])

network.fit(train_images,train_labels,epochs=5, batch_size= 128)
test_loss, test_acc = network.evaluate(test_images, test_labels)
print("test accuracy", test_acc)
