from keras.models import load_model  # Or your ML library
from PIL import Image
import numpy as np
import tensorflow as tf

# # Load your model once when the module loads
# model = load_model('/static/final_model82.h5')
# print("Model loaded successfully.")

import os
from keras.models import load_model

# Define the absolute path
# model_path = os.path.join(os.path.dirname(__file__), 'static', 'final_model82.h5')
# model = load_model(model_path)
# print("Model loaded successfully.")
class_name = ['Apple___Black_rot', 'Apple___healthy', 'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy', 'Pepper,_bell___healthy', 'Potato___Late_blight', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___healthy']
class_mapping = {
    'Apple___Black_rot': 'Apple Black Rot',
    'Apple___healthy': 'Apple Healthy',
    'Blueberry___healthy': 'Blueberry Healthy',
    'Cherry_(including_sour)___Powdery_mildew': 'Cherry Powdery Mildew',
    'Cherry_(including_sour)___healthy': 'Cherry Healthy',
    'Corn_(maize)___Common_rust_': 'Corn Common Rust',
    'Corn_(maize)___Northern_Leaf_Blight': 'Corn Northern Leaf Blight',
    'Corn_(maize)___healthy': 'Corn Healthy',
    'Grape___Black_rot': 'Grape Black Rot',
    'Grape___Esca_(Black_Measles)': 'Grape Esca',
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': 'Grape Leaf Blight',
    'Grape___healthy': 'Grape Healthy',
    'Orange___Haunglongbing_(Citrus_greening)': 'Orange Huanglongbing',
    'Peach___Bacterial_spot': 'Peach Bacterial Spot',
    'Peach___healthy': 'Peach Healthy',
    'Pepper,_bell___healthy': 'Pepper Bell Healthy',
    'Potato___Late_blight': 'Potato Late Blight',
    'Raspberry___healthy': 'Raspberry Healthy',
    'Soybean___healthy': 'Soybean Healthy',
    'Squash___Powdery_mildew': 'Squash Powdery Mildew',
    'Strawberry___Leaf_scorch': 'Strawberry Leaf Scorch',
    'Strawberry___healthy': 'Strawberry Healthy',
    'Tomato___Leaf_Mold': 'Tomato Leaf Mold',
    'Tomato___Septoria_leaf_spot': 'Tomato Septoria Leaf Spot',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus': 'Tomato Yellow Leaf Curl Virus',
    'Tomato___healthy': 'Tomato Healthy'
}
def detect_disease(image_path):
    cnn = tf.keras.models.Sequential()
        
    cnn.add(tf.keras.layers.Conv2D(filters=32,kernel_size=3,padding='same',activation='relu',input_shape=[128,128,3]))
    cnn.add(tf.keras.layers.Conv2D(filters=32,kernel_size=3,activation='relu'))
    cnn.add(tf.keras.layers.MaxPool2D(pool_size=2,strides=2))
    cnn.add(tf.keras.layers.Conv2D(filters=64,kernel_size=3,padding='same',activation='relu'))
    cnn.add(tf.keras.layers.Conv2D(filters=64,kernel_size=3,activation='relu'))
    cnn.add(tf.keras.layers.MaxPool2D(pool_size=2,strides=2))
    cnn.add(tf.keras.layers.Conv2D(filters=128,kernel_size=3,padding='same',activation='relu'))
    cnn.add(tf.keras.layers.Conv2D(filters=128,kernel_size=3,activation='relu'))
    cnn.add(tf.keras.layers.MaxPool2D(pool_size=2,strides=2))
    cnn.add(tf.keras.layers.Conv2D(filters=256,kernel_size=3,padding='same',activation='relu'))
    cnn.add(tf.keras.layers.Conv2D(filters=256,kernel_size=3,activation='relu'))
    cnn.add(tf.keras.layers.MaxPool2D(pool_size=2,strides=2))
    cnn.add(tf.keras.layers.Conv2D(filters=512,kernel_size=3,padding='same',activation='relu'))
    cnn.add(tf.keras.layers.Conv2D(filters=512,kernel_size=3,activation='relu'))
    cnn.add(tf.keras.layers.MaxPool2D(pool_size=2,strides=2))
    cnn.add(tf.keras.layers.Flatten()) # Add flatten and dense layers after the convolutions.
    cnn.add(tf.keras.layers.Dense(units=26,activation='softmax'))
    cnn.compile(optimizer=tf.keras.optimizers.Adam( # Removed 'legacy'
    learning_rate=0.0001),loss='categorical_crossentropy',metrics=['accuracy'])

    cnn.load_weights('cropCure/static/final_model82.h5')
    print("Model weights loaded successfully.")
    import cv2
    import matplotlib.pyplot as plt
    # image_path = '/content/data/split_plant_village/test/Apple___Black_rot/079d0ba3-b207-4fc7-ace3-f2fe25c796b3___JR_FrgE.S 3038.JPG'
    # image_path = image_path
    # Reading an image in default mode
    print(image_path)
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #Converting BGR to RGB

    image = tf.keras.preprocessing.image.load_img(image_path,target_size=(128,128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])  # Convert single image to a batch.
    predictions = cnn.predict(input_arr)

    result_index = np.argmax(predictions) #Return index of max element
    print(result_index)

    # Displaying the disease prediction
    model_prediction = class_name[result_index]
    print(class_mapping[model_prediction])
    return class_mapping[model_prediction]


# detection = detect_disease("cropCure/static/inputted_images/apple_scrab3.jpg")
# print(detection)

