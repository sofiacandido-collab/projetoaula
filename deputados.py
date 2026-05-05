import streamlit as st
import pandas as pd

st.write("**Esse é um comparador dos deputados de 2018 e 2022**")

st.write("Deputados de 2018")
df2 = pd.read_csv('deputados_2018 (1).csv')
st.dataframe(df2)

st.write("Deputados de 2022")
df = pd.read_csv('deputados_2022.csv')
st.dataframe(df)

st.title('Buscador de deputadas por partido: ')
partido = st.text_input('Digite a sigla do partido: ')

if partido:
  filtrado = df[df['partido'].str.upper() == partido.upper()]
  st.dataframe(filtrado)
