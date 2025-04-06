import streamlit as st
import pandas as pd
#import seaborn as sns

st.markdown("<h1 style='text-align: center; color: black;'>Predicting Video Game Sales Based on Selected Attributes</h1>", unsafe_allow_html=True)

data = pd.read_csv('vgsales')


st.write('Due to the sudden emergence of indie games over AAA titles the past couple years had us thinking, how has video game sales changed over time?')
st.write("Additionally, how can we use different metrics in video games to predict video game sales?")

st.write(data)


genre_option = st.selectbox("Choose a genre:",(data['Genre'].unique()))
platform_option = st.selectbox("Choose a platform:",(data['Platform'].unique()))
publisher_option = st.selectbox("Choose a publisher:",(data['Publisher'].unique()))


