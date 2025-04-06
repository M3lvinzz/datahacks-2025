import streamlit as st
import pandas as pd
import time
import re
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.metrics import classification_report

def clean(review):
    review = review.lower()
    review = re.sub(r'[^a-zA-Z0-9 ]', '', review)
    return review

st.logo(image = 'racoon.jpg')
st.markdown("<h1 style='text-align: center; color: black;'>Genre Prediction based on Reviews </h1>", unsafe_allow_html=True)
st.write('Inspired by our love for video games, we decided to build a prediction model that can distinguish what type of genre a video game is based on the review input down below.')


data = pd.read_csv('final_data.csv')
st.write(data)


input = st.text_input("Please enter a review and we'll predict the genre",)
input = clean(input)

loaded_model = joblib.load('genre_classifier_model.joblib')

output = loaded_model.predict([input])

if st.button('Run input'):
    with st.spinner("Wait for it...", show_time=True):
        time.sleep(5)
        st.success(output[0])

