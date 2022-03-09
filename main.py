from pip import main
import streamlit as st
import pandas as pd
import numpy as np
st.title("my data app")
st.write(""" upload csv file """)
todrop=[]
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
     # Can be used wherever a "file-like" object is accepted:
    df = pd.read_csv(uploaded_file)
    df.fillna(0)
    df.duplicated()
    st.write(df.describe())
    st.write("colum name in the csv file")
    for column in df.columns:
        st.markdown(column)
    text_input=st.text_input("enter the column to be deleted")
