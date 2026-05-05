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

    resultado = pd.concat([mulheres_2018, mulheres_2022])

    st.dataframe(resultado)

    total = len(resultado)
    st.success(f"Existem {total} mulheres no partido {partido.upper()} (2018 + 2022)")

st.header("Total de mulheres eleitas")

total_2018 = len(df_2018[df_2018['sexo'].str.upper() == 'F'])
total_2022 = len(df_2022[df_2022['sexo'].str.upper() == 'F'])

fig, ax = plt.subplots()
ax.bar(['2018', '2022'], [total_2018, total_2022])
ax.set_title('Número de mulheres eleitas')
ax.set_ylabel('Quantidade')

st.pyplot(fig)
