import pandas as pd 

#lê o arquivo no formato csv.
df = pd.read_csv('https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv')

#cabeçario
print(df.head(10))

#informações
print(df.info())

#descrição
print(df.describe())

#dimenção do arquivo e vetor
print(df.shape)

linhas, colunas = df.shape [0], df.shape[1]

#texto que vai ser impresso dentro de " " + variavel 
print("linhas:", linhas)
print("colunas:", colunas)

print(df.columns)

#renomeia as colunas 
df = df.rename(columns={
    'work_year': 'ano_trabalho',
    'experience_level': 'nivel_experiencia',
    'employment_type': 'tipo_contrato',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda_salario',
    'salary_in_usd': 'salario_usd',
    'employee_residence': 'residencia_funcionario',
    'remote_ratio': 'percentual_remoto',
    'company_location': 'local_empresa',
    'company_size': 'tamanho_empresa'
})

print(df.columns)

#metodo que calcula a frequencia de cada categoria
print(df["nivel_experiencia"].value_counts())