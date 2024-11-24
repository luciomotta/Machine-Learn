# função para verificar se o arquivo existe
import csv
import os
import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression # Importa o modelo de regressão linear DIFERENTE DO JUPTER    

# Caminho do arquivo CSV
filename = 'src\DataFrame\pizzas.csv'

# Função para verificar se o arquivo existe
def file_exists():
    return os.path.exists(filename)

# Se não existir, cria o arquivo
if not file_exists():
    # Inicia com os valores iniciais
    diametro = 20
    preco = 50

    # Criação da progressão
    rows = [["diametro", "preco"]]
    for _ in range(10):
        rows.append([diametro, preco])
        diametro += 2  # Incrementa o diâmetro em 2
        preco += 10  # Incrementa o preço em 10

    # Grava os dados no arquivo CSV
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

# ------------------------------------------------------------------
# Agora lê/carregar o arquivo CSV
df = pd.read_csv(filename)

# Cria o modelo de regressão linear
modelo = LinearRegression()

#Treinando o modelo 

x = df[["diametro"]]
y = df[["preco"]]

modelo.fit(x, y)

# A biblioteca stremlit  cria a pagina web instalei na maquina virtual ent dou o 'streamlit run app.py' no terminal da (venv)
st.title("Prevendo o preço da pizza")
st.divider()

diametro = st.number_input("Digite o tamanho diâmetro da pizza (cm):", min_value=0.0, max_value=100.0, step=2.0)

if diametro:  # SE FOR ZERO entende como falso
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(f"Para uma pizza de {diametro:.2f} cm, o valor previsto é R$ {preco_previsto:.2f}")
    # Adiciona o ícone de olho ao lado do texto
    image_path = 'src\img\Figure_ploat-scatter.png'  # Substitua pelo caminho da sua imagem
    
    
    #st.image(image_path, caption='Gráfico de dispersão', use_container_width =True)

    if os.path.exists(image_path):
        if st.button("Ver gráfico"):
            st.image(image_path, caption='Gráfico de dispersão', use_container_width =True)
            st.write("-Esses foram os dados que treinaram a Máquina Virtual que faz a previsão do preço.")
    st.balloons()  # Adiciona balões de festa ao resultado
