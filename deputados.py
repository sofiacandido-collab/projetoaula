import streamlit as st
import pandas as pd

st.title("Comparador de Deputadas (2018 vs 2022)")

# Carregar dados
df_2018 = pd.read_csv('deputados_2018 (1).csv')
df_2022 = pd.read_csv('deputados_2022.csv')

# Padronizar nomes das colunas
df_2018.columns = df_2018.columns.str.lower().str.strip()
df_2022.columns = df_2022.columns.str.lower().str.strip()

st.header("Buscar deputadas por partido")

partido = st.text_input("Digite a sigla do partido:")

if partido:
    partido = partido.strip().upper()

    # 🔹 FILTRO 2022 (funciona normal)
    mulheres_2022 = df_2022[
        (df_2022['partido'].astype(str).str.strip().str.upper() == partido) &
        (df_2022['sexo'].astype(str).str.upper().str.startswith('F'))
    ].copy()

    # 🔹 FILTRO 2018 (adaptado porque sexo está inconsistente)
    if 'sexo' in df_2018.columns and df_2018['sexo'].notna().sum() > 0:
        mulheres_2018 = df_2018[
            (df_2018['partido'].astype(str).str.strip().str.upper() == partido) &
            (df_2018['sexo'].astype(str).str.upper().str.startswith('F'))
        ].copy()
    else:
        # fallback: sem filtro de sexo
        mulheres_2018 = df_2018[
            (df_2018['partido'].astype(str).str.strip().str.upper() == partido)
        ].copy()
        st.warning("⚠️ Dados de sexo de 2018 estão incompletos — mostrando todas do partido.")

    # Adicionar coluna de ano
    mulheres_2018['ano'] = '2018'
    mulheres_2022['ano'] = '2022'

    # Juntar dados
    resultado = pd.concat([mulheres_2018, mulheres_2022], ignore_index=True)

    # Verificar se existe coluna nome
    col_nome = 'nome' if 'nome' in resultado.columns else resultado.columns[0]

    # Exibir
    st.subheader("Resultado")
    st.dataframe(resultado[[col_nome, 'partido', 'ano']])

    # Totais separados
    st.subheader("Resumo")
    st.write(f"2018: {len(mulheres_2018)}")
    st.write(f"2022: {len(mulheres_2022)}")
    st.success(f"Total: {len(resultado)}")
