import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# TensorFlow Model Prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model("trained_model.h5")
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(64, 64, 3))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])  # Add batch dimension
    predictions = model.predict(input_arr)
    return np.argmax(predictions)

# Calorie Database
calorie_dict = {
    "watermelon": 52,
    "banana": 96,
    "mango": 41,
    "spinach": 18,
    "cauliflower": 55,
    "apple":44,
    "potato":88,
    "paprika":44,
}

# Function to get calorie information
def get_calories(label):
    return calorie_dict.get(label, "Unknown")

# Sidebar
st.sidebar.title("Dash bar")
app_mode = st.sidebar.selectbox("Select Page", ["Home", "About Project", "Prediction"])

# Main Page
if app_mode == "Home":
    st.header("FRUITS & VEGETABLES RECOGNITION SYSTEM")
    image_path = "foodie.jpg"
    st.image(image_path)

# About Project
elif app_mode == "About Project":
    st.header("About Project")
    st.subheader("About Dataset")
    st.text("This dataset contains the images of the following food items:")
    st.text("Fruits and vegetables")

# Prediction Page
elif app_mode == "Prediction":
    st.header("Model Prediction")
    test_image = st.file_uploader("Choose an Image:")

    if st.button("Show Image"):
        st.image(test_image, width=4, use_column_width=True)
        
    if st.button("Predict"):
        st.write("Our Prediction")
        st.snow()
        st.balloons()
        result_index = model_prediction(test_image)

        # Reading labels
        with open("labels.txt") as f:
            content = f.readlines()
        labels = [i.strip() for i in content]

        predicted_label = labels[result_index]
        st.success(f"Model is predicting it's a {predicted_label}")

        # Get calorie information
        calories = get_calories(predicted_label)
        st.info(f"Estimated calories for {predicted_label}: {calories} kcal")
