import streamlit as st
import pandas as pd

st.title('Streamlit Text Input')

name = st.text_input('Enter your name:')

age = st.slider('Select your age', 0, 100, 25)

st.write(f'Your age is {age}.')

options = ['Python', 'Java', 'C++', "JavaScript"]
choise = st.selectbox("Choose your favorite language:", options)

st.write(f'You selected {choise}')

if name:
    st.write (f"Hello, {name}")
    
data = {
    "Name": ['john', "jane", "jake", "Jill"],
    "Age" : [28, 24,35, 40],
    "city": ["New York", "Los Angles", "Chicago", 'Houston']
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_files = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_files is not None:
    df = pd.read_csv(uploaded_files)
    st.write(df)