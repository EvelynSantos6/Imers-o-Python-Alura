import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pycountry

data = {'ano': [2025, 2025, 2025, 2025, 2025],
        'senioridade': ['senior', 'senior', 'pleno', 'pleno', 'junior'],
        'contrato': ['integral', 'integral', 'integral', 'integral', 'integral'],
        'cargo': ['Solutions Engineer', 'Solutions Engineer', 'Data Engineer', 'Data Engineer', 'Data Engineer'],
        'salario': [214000, 136000, 158800, 139200, 90000],
        'moeda': ['USD', 'USD', 'USD', 'USD', 'USD'],
        'usd': [214000, 136000, 158800, 139200, 90000],
        'residencia': ['US', 'US', 'AU', 'AU', 'US'],
        'remoto': ['remoto', 'remoto', 'presencial', 'presencial', 'presencial'],
        'empresa': ['US', 'US', 'AU', 'AU', 'US'],
        'tamanho_empresa': ['media', 'media', 'media', 'media', 'media']}
df_limpo = pd.DataFrame(data)


print("--- Visualização com Matplotlib e Seaborn ---")
# Gráfico de Barras com Matplotlib
print("\nGráfico de Barras: Distribuição de Senioridade")
df_limpo['senioridade'].value_counts().plot(
    kind='bar', title="Distribuição de senioridade")
plt.show()

# Gráfico de Barras com Seaborn
print("\nGráfico de Barras com Seaborn: Salário Médio por Senioridade")
plt.figure(figsize=(8, 5))
sns.barplot(data=df_limpo, x='senioridade', y='usd')
plt.title("Salário médio por senioridade")
plt.xlabel("Senioridade")
plt.ylabel("Salário médio anual (USD)")
plt.show()

# Ordenando o gráfico de barras
print("\nGráfico de Barras Ordenado: Salário Médio por Senioridade")
ordem = df_limpo.groupby('senioridade')[
    'usd'].mean().sort_values(ascending=True).index
plt.figure(figsize=(8, 5))
sns.barplot(data=df_limpo, x='senioridade', y='usd', order=ordem)
plt.title("Salário médio por senioridade")
plt.xlabel("Senioridade")
plt.ylabel("Salário médio anual (USD)")
plt.show()

# Histograma
print("\nHistograma: Distribuição dos salários anuais")
plt.figure(figsize=(10, 5))
sns.histplot(df_limpo['usd'], bins=50, kde=True)
plt.title("Distribuição dos salários anuais")
plt.xlabel("Salário em USD")
plt.ylabel("Frequência")
plt.show()

# Boxplot
print("\nBoxplot: Salário Anual")
plt.figure(figsize=(8, 5))
sns.boxplot(x=df_limpo['usd'])
plt.title("Boxplot Salário")
plt.xlabel("Salário em USD")
plt.show()

# Boxplot por senioridade
print("\nBoxplot: Distribuição por Senioridade")
ordem_senioridade = ['junior', 'pleno', 'senior', 'executivo']
plt.figure(figsize=(8, 5))
sns.boxplot(x='senioridade', y='usd', data=df_limpo,
            order=ordem_senioridade, palette='Set2')
plt.title("Boxplot da distribuição por senioridade")
plt.xlabel("Senioridade")
plt.ylabel("Salário em USD")
plt.show()


print("\n--- Visualização com Plotly ---")
# Gráfico de barras interativo com Plotly
print("\nGráfico de Barras interativo: Média Salarial por Senioridade")
senioridade_media_salario = df_limpo.groupby(
    'senioridade')['usd'].mean().sort_values(ascending=False).reset_index()
fig = px.bar(senioridade_media_salario,
            x='senioridade',
            y='usd',
            title='Média Salarial por Senioridade',
            labels={'senioridade': 'Nível de Senioridade', 'usd': 'Média Salarial Anual (USD)'})
fig.show()

# Gráfico de Pizza (Pie Chart) com Plotly
print("\nGráfico de Pizza: Proporção dos tipos de trabalho (Remoto/Presencial)")
remoto_contagem = df_limpo['remoto'].value_counts().reset_index()
remoto_contagem.columns = ['tipo_trabalho', 'quantidade']
fig = px.pie(remoto_contagem,
            names='tipo_trabalho',
            values='quantidade',
            title='Proporção dos tipos de trabalho',
            hole=0.5)
fig.update_traces(textinfo='percent+label')
fig.show()

# Gráfico de Mapa (Choropleth) com Plotly
print("\nGráfico de Mapa: Salário médio de Cientista de Dados por país")
# Adicionando coluna ISO-3 para o mapa


def iso2_to_iso3(code):
    try:
        return pycountry.countries.get(alpha_2=code).alpha_3
    except:
        return None


df_limpo['residencia_iso3'] = df_limpo['residencia'].apply(iso2_to_iso3)

# Filtrando e calculando a média
# Usando 'Data Engineer' para o exemplo
df_ds = df_limpo[df_limpo['cargo'] == 'Data Engineer']
media_ds_pais = df_ds.groupby('residencia_iso3')['usd'].mean().reset_index()

# Gerando o mapa
fig = px.choropleth(media_ds_pais,
                    locations='residencia_iso3',
                    color='usd',
                    color_continuous_scale='rdylgn',
                    title='Salário médio de Data Engineer por país',
                    labels={'usd': 'Salário médio (USD)', 'residencia_iso3': 'País'})
fig.show()

# Salvando o DataFrame final para uso futuro
print("\nSalvando o DataFrame final em 'dados-imersao-final.csv'")
df_limpo.to_csv('dados-imersao-final.csv', index=False)
