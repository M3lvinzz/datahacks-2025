import streamlit as st
import pandas as pd
import time


st.markdown("<h1 style='text-align: center; color: black;'>Genre Prediction based on Reviews </h1>", unsafe_allow_html=True)
st.write('Inspired by our love for video games, we decided to build a prediction model that can distinguish what type of genre a video game is based on the review input down below.')


data = pd.read_csv('games.csv')

st.logo(image = 'racoon.jpg')


input = st.text_input("Please enter a review and we'll predict the genre",)

output = ''

accuracy_model = ""

if st.button('Run input'):
    with st.spinner("Wait for it...", show_time=True):
        time.sleep(3)
        st.success(input)

st.write('The accuracy of our model is: ')


