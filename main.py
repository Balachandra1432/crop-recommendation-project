import pickle
import streamlit as st

@st.cache_resource
def load_model():
    try:
        return pickle.load(open("Crop_recommendation_model.pkl", "rb"))
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_model()
#model=pickle.load(open("Crop_recommendation_model.pkl","rb"))
st.header("Crop Recommendation Project")


nitro=st.number_input("Enter Nitrogen content in the soil (in mg/kg)",min_value=10,max_value=140)
phosp=st.number_input("Enter Phosphorus content in the soil (in mg/kg)",min_value=5,max_value=145)
pota=st.number_input("Enter Potassium content in the soil (in mg/kg)",min_value=5,max_value=205)
temp=st.number_input("Enter Average temperature in °C",min_value=8,max_value=43)
humi=st.number_input("Enter Average relative humidity in %",min_value=15,max_value=100)
ph=st.number_input("Enter Soil pH value",min_value=3,max_value=10)
rain=st.number_input("Enter Rainfall in mm",min_value=20,max_value=300)
data=[[nitro,phosp,pota,temp,humi,ph,rain]]
if st.button("Predict Crop"):
    val=model.predict(data)[0]
    if val=="muskmelon":
        st.markdown(f"<h4> Recommended Crop: {val} </h4>",unsafe_allow_html=True)
        st.image("C:/Users/janag/Desktop/crop recommendation project/muskmelon.jpg",width=400)

    elif val=="apple":
        st.markdown(f"<h4> Recommended Crop: {val} </h4>",unsafe_allow_html=True)
        st.image("C:/Users/janag/Desktop/crop recommendation project/apple-image.jpg",width=400)

    elif val=="banana":
        st.markdown(f"<h4> Recommended Crop: {val} </h4>",unsafe_allow_html=True)
        st.image("C:/Users/janag/Desktop/crop recommendation project/banana-image.jpg",width=400)

    elif val=="blackgram":
        st.markdown(f"<h4> Recommended Crop: {val} </h4>",unsafe_allow_html=True)
        st.image("C:/Users/janag/Desktop/crop recommendation project/blackgram-image.jpg",width=400)

    elif val=="chickpea":
        st.markdown(f"<h4> Recommended Crop: {val} </h4>",unsafe_allow_html=True)
        st.image("C:/Users/janag/Desktop/crop recommendation project/chickpea-image.jpg",width=400)

    elif val=="coconut":
        st.markdown(f"<h4> Recommended Crop: {val} </h4>",unsafe_allow_html=True)
        st.image("C:/Users/janag/Desktop/crop recommendation project/coconut-iamge.jpg",width=400)

    elif val=="coffee":
        st.markdown(f"<h4> Recommended Crop: {val} </h4>",unsafe_allow_html=True)
        st.image("C:/Users/janag/Desktop/crop recommendation project/coffee-image.jpg",width=400)

    elif val=="cotton":
        st.markdown(f"<h4> Recommended Crop: {val} </h4>",unsafe_allow_html=True)
        st.image("C:/Users/janag/Desktop/crop recommendation project/cotton-image.jpg",width=400)

    elif val=="grapes":
        st.markdown(f"<h4> Recommended Crop: {val} </h4>",unsafe_allow_html=True)
        st.image("C:/Users/janag/Desktop/crop recommendation project/grapes-image.jpg",width=400)

    elif val=="kidneybeans":
        st.markdown(f"<h4> Recommended Crop: {val} </h4>",unsafe_allow_html=True)
        st.image("C:/Users/janag/Desktop/crop recommendation project/kidney-beans-image.jpg",width=400)

    elif val=="lentil":
        st.markdown(f"<h4> Recommended Crop: {val} </h4>",unsafe_allow_html=True)
        st.image("C:/Users/janag/Desktop/crop recommendation project/lentil-image.jpg",width=400)

    elif val=="maize":
        st.markdown(f"<h4> Recommended Crop: {val} </h4>",unsafe_allow_html=True)
        st.image("C:/Users/janag/Desktop/crop recommendation project/maize-image.jpg",width=400)

    elif val=="mango":
        st.markdown(f"<h4> Recommended Crop: {val} </h4>",unsafe_allow_html=True)
        st.image("C:/Users/janag/Desktop/crop recommendation project/mango-tree.jpg",width=400)
        
    elif val=="mungbean":
        st.markdown(f"<h4> Recommended Crop: {val} </h4>",unsafe_allow_html=True)
        st.image("C:/Users/janag/Desktop/crop recommendation project/moong-beans-image.jpg",width=400)

    elif val=="orange":
        st.markdown(f"<h4> Recommended Crop: {val} </h4>",unsafe_allow_html=True)
        st.image("C:/Users/janag/Desktop/crop recommendation project/orange-image.jpg",width=400)

    elif val=="papaya":
        st.markdown(f"<h4> Recommended Crop: {val} </h4>",unsafe_allow_html=True)
        st.image("C:/Users/janag/Desktop/crop recommendation project/papaya-image.jpg",width=400)

    elif val=="pigeonpeas":
        st.markdown(f"<h4> Recommended Crop: {val} </h4>",unsafe_allow_html=True)
        st.image("C:/Users/janag/Desktop/crop recommendation project/pigeonpeas-image.jpg",width=400)

    elif val=="pomegranate":
        st.markdown(f"<h4> Recommended Crop: {val} </h4>",unsafe_allow_html=True)
        st.image("C:/Users/janag/Desktop/crop recommendation project/pomegranate-iamge.jpg",width=400)

    elif val=="jute":
        st.markdown(f"<h4> Recommended Crop: {val} </h4>",unsafe_allow_html=True)
        st.image("C:/Users/janag/Desktop/crop recommendation project/jute-image.jpg",width=400)

    elif val=="watermealo":
        st.markdown(f"<h4> Recommended Crop: {val} </h4>",unsafe_allow_html=True)
        st.image("C:/Users/janag/Desktop/crop recommendation project/water-mealo-image.jpg",width=400)
    
    elif val=="rice":
        st.markdown(f"<h4> Recommended Crop: {val} </h4>",unsafe_allow_html=True)
        st.image("C:/Users/janag/Desktop/crop recommendation project/rice-image.jpg",width=400)

    elif val=="mothbeans":
        st.markdown(f"<h4> Recommended Crop: {val} </h4>",unsafe_allow_html=True)
        st.image("C:/Users/janag/Desktop/crop recommendation project/mothbeans-image.jpg",width=400)
    
        
