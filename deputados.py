import streamlit as st
import pandas as pd

st.write("**Esse é um comparador dos deputados de 2018 e 2022**")

st.write("Deputados de 2018")
st.write("Deputados de 2022")
df_2018 = pd.read_csv('deputados_2018 (1).csv')
df_2022 = pd.read_csv('deputados_2022.csv')

df_merge = pd.merge(df_2018, df_2022, on='nome', how='outer')
st.title('Buscador de deputadas por partido: ')
partido = st.text_input('Digite a sigla do partido: ')

if partido:
  filtrado = df[df['partido'].str.upper() == partido.upper()]
  filtrado2 = df[df['sexo'].str.upper() == sexo.upper()]
  st.dataframe(filtrado + filtrado2)
  

