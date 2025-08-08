import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv')

#Onde não tem dado nulo ele conta como false.
print(df.isnull())

print(df.head(5))

print(df.isnull().sum())

#valores unicos na coluna.
print(df['work_year'].unique())

#filtro "pege tudo da base e me mostre qual é nulo e imprima"
print(df[df.isnull().any(axis=1)])

#Framework python
import numpy as np

#Cria um DF
df_salarios = pd.DataFrame({
    'nome': ["Evelyn", "Leia", "luana"],
    'salario': [100000, np.nan, 3000]
})

# Criando coluna 'salario_media' com média preenchendo valores nulos
df_salarios['salario_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2))
df_salarios['salario_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median())
print(df_salarios)

df_temperaturas = pd.DataFrame ({
    "Dia":["Segunda", "Terça","Quarta", "Quinta", "Sexta"],
    "Temperatura":[30, np.nan, 25, 28, 21]
})

df_temperaturas["preenchimento_bfill"] = df_temperaturas["Temperatura"].bfill()
print(df_temperaturas)

df_cidades =pd.DataFrame({
    'nome': ["Evelyn", "Leia", "luana"],
    'cidade':["São Paulo", "Belo Horizonte", np.nan]
})

df_cidades['cidade_preenchida'] = df_cidades['cidade'].fillna("Não informado")
print(df_cidades)

df_limpo = df.dropna()
print(df_limpo.isnull().sum())

df_limpo= df_limpo.assign(work_year = df_limpo['work_year'].astype('int64'))
print(df_limpo.head())