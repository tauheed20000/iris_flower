import pandas as pd
import seaborn as sns
import streamlit as st

st.header('This VIdeo is brought to you by Tauheed khan')

st.subheader('I am Tauheed currently, Pursuing Master in Data Science')

st.text(' I have relevant skills related to data science domain such as Python,Machne Learning,Deep Learning,NLP')

st.header('#Introduction')

st.text('Hello Everyone,My name is Tauheed Khan Currently, I am pursuing Master in Data Science')

df=sns.load_dataset('iris')
st.write(df.head(5))
st.write(df[['species','sepal_length','petal_length']])
st.bar_chart(df['sepal_length'])
st.line_chart(df['sepal_length'])