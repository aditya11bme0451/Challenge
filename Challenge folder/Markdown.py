import streamlit as st
import pandas as pd

st.title("Basic Streamlit App")

name = st.text_input("Your name", "World")
age = st.slider("Your age", 0, 100, 25)

if st.button("Greet"):
    st.write(f"Hello, {name}! You are {age} years old.")

if st.checkbox("Show sample data and chart"):
    df = pd.DataFrame({
        "fruits": ["Apples", "Bananas", "Cherries"],
        "count": [10, 5, 7]
    })
    st.dataframe(df)
    st.bar_chart(df.set_index("fruits"))

st.write("Upload a CSV to preview:")
uploaded = st.file_uploader("Choose a CSV file", type="csv")
if uploaded is not None:
    df2 = pd.read_csv(uploaded)
    st.write(df2.head())