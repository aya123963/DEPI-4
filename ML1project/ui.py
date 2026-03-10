import streamlit as st
import pickle
import numpy as np


with open("house_price_model.pkl", "rb") as f:
    model = pickle.load(f)


st.title(" House Price Prediction")

st.write("Please enter the house data to make a prediction:")


rooms = st.number_input("Room Number:", min_value=1, max_value=20, value=5)
poverty = st.number_input("Poverty Percentage:", min_value=0, max_value=100, value=17)
student_teacher_ratio = st.number_input("Student To Teacher Ratio:", min_value=5, max_value=50, value=15)



if st.button("Price Prediction"):
    data = np.array([[rooms, poverty, student_teacher_ratio]])
    prediction = model.predict(data)
    st.success(f"House Price Prediction: ${prediction[0]:,.2f}")