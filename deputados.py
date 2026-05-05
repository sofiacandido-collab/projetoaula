import streamlit as st
import pandas as pd

st.write("Esse é um comparador dos deputados de 2018 e 2022")
df = pd.read_csv('deputados_2022.csv')
st.dataframe(df)

