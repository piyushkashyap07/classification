from tensorflow import keras
import numpy as np
import tensorflow as tf
import PIL

# Load the model
model = keras.models.load_model(r'C:\Piyush\Scripts\jobs\classifier\gender_classification_model.h5')

# Preprocess the image
def preprocess_image(image_path):
    img = keras.preprocessing.image.load_img(image_path, target_size=(256, 256))
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch
    img_array = img_array / 255.0  # Normalize
    return img_array

# Path to the image you want to classify
image_path = r"C:\Piyush\Scripts\jobs\classifier\images\gender\valid\female\image_134.jpg"

# Preprocess the image
img_array = preprocess_image(image_path)

# Make a prediction
prediction = model.predict(img_array)

# Get the classification result
if prediction[0] > 0.5:
    print("Predicted: Male")
else:
    print("Predicted: Female")
