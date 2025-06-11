import pickle
import streamlit as st

# Load the model
model = pickle.load(open("Crop_recommendation_model.pkl", "rb"))

st.set_page_config(page_title="Crop Recommendation App", layout="centered")
st.header("🌾 Crop Recommendation Project")

# Input fields
nitro = st.number_input("Nitrogen (mg/kg)", min_value=10, max_value=140)
phosp = st.number_input("Phosphorus (mg/kg)", min_value=5, max_value=145)
pota = st.number_input("Potassium (mg/kg)", min_value=5, max_value=205)
temp = st.number_input("Temperature (°C)", min_value=8, max_value=43)
humi = st.number_input("Humidity (%)", min_value=15, max_value=100)
ph = st.number_input("Soil pH", min_value=3.0, max_value=10.0)
rain = st.number_input("Rainfall (mm)", min_value=20, max_value=300)

# Predict button
if st.button("Predict Crop"):
    data = [[nitro, phosp, pota, temp, humi, ph, rain]]
    val = model.predict(data)[0]

    st.success(f"🌱 Recommended Crop: **{val.capitalize()}**")

    # Crop-to-image mapping
    image_paths = {
        "muskmelon": "muskmelon.jpg",
        "apple": "apple-image.jpg",
        "banana": "banana-image.jpg",
        "blackgram": "blackgram-image.jpg",
        "chickpea": "chickpea-image.jpg",
        "coconut": "coconut-image.jpg",
        "coffee": "coffee-image.jpg",
        "cotton": "cotton-image.jpg",
        "grapes": "grapes-image.jpg",
        "kidneybeans": "kidney-beans-image.jpg",
        "lentil": "lentil-image.jpg",
        "maize": "maize-image.jpg",
        "mango": "mango-tree.jpg",
        "mungbean": "moong-beans-image.jpg",
        "orange": "orange-image.jpg",
        "papaya": "papaya-image.jpg",
        "pigeonpeas": "pigeonpeas-image.jpg",
        "pomegranate": "pomegranate-image.jpg",
        "jute": "jute-image.jpg",
        "watermelon": "watermelon-image.jpg",
        "rice": "rice-image.jpg",
        "mothbeans": "mothbeans-image.jpg"
    }

    # Image display
    image_file = image_paths.get(val, None)
    if image_file:
        st.image(f"images/{image_file}", width=400)
    else:
        st.warning("No image found for this crop.")
