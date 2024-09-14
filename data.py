import pandas as pd
import streamlit as st

st.header('Welcome to Displaying Dataframe 101')
df=pd.DataFrame({
    'Name': ['John', 'Jane', 'Jack', 'Dave'],
    'Age': [21, 22, 23, 24],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Los Angeles'],
})

st.dataframe(df)