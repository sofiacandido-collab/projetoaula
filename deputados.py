import streamlit as st
import pandas as pd

st.title("Comparador de Deputadas (2018 vs 2022)")

df_2018 = pd.read_csv('deputados_2018 (1).csv')
df_2022 = pd.read_csv('deputados_2022.csv')
df_2018.columns = df_2018.columns.str.lower()
df_2022.columns = df_2022.columns.str.lower()

st.header("Buscar deputadas por partido")

partido = st.text_input("Digite a sigla do partido:")

if partido:
    mulheres_2018 = df_2018[
        (df_2018['partido'].astype(str).str.upper() == partido.upper()) &
        (df_2018['sexo'].astype(str).str.upper() == 'F')
    ]

    mulheres_2022 = df_2022[
        (df_2022['partido'].astype(str).str.upper() == partido.upper()) &
        (df_2022['sexo'].astype(str).str.upper() == 'F')
    ]

    mulheres_2018['ano'] = '2018'
    mulheres_2022['ano'] = '2022'

    resultado = pd.concat([mulheres_2018, mulheres_2022])
    st.dataframe(resultado[['nome', 'partido', 'ano']])

    total = len(resultado)
    st.success(f"Existem {total} mulheres no partido {partido.upper()}")
   

    st.dataframe(resultado)

    total = len(resultado)
    st.success(f"Existem {total} mulheres no partido {partido.upper()} (2018 + 2022)")
