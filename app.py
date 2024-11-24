import os
import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression

# Caminho do arquivo CSV
filename = 'src/DataFrame/pizzas.csv'

# Função para verificar se o arquivo existe
def file_exists():
    return os.path.exists(filename)

# Se não existir, cria o arquivo
if not file_exists():
    # Cria o diretório se não existir
    os.makedirs(os.path.dirname(filename), exist_ok=True)

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

# Carregar os dados
df = pd.read_csv(filename)

# Treinando o modelo
x = df[["diametro"]]
y = df[["preco"]]

modelo = LinearRegression()
modelo.fit(x, y)

# A biblioteca Streamlit cria a página web
st.title("Prevendo o preço da pizza")
st.divider()

diametro = st.number_input("Digite o tamanho diâmetro da pizza (cm):", min_value=0.0, max_value=100.0, step=0.1)

if diametro:  # SE FOR ZERO entende como falso
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(f"Para uma pizza de {diametro:.2f} cm, o valor previsto é R$ {preco_previsto:.2f}")

    # Adiciona o ícone de olho ao lado do texto
    image_path = 'https://github.com/luciomotta/Machine-Learn/blob/main/src/img/Figure_ploat-scatter.png'  # Substitua pelo caminho da sua imagem
    st.image('https://raw.githubusercontent.com/luciomotta/Machine-Learn/main/src/img/Figure_ploat-scatter.png', caption='Gráfico de dispersão', use_column_width=True)

    if os.path.exists(image_path):
        if st.button("Ver gráfico"):
            try:
                st.image(image_path, caption='Gráfico de dispersão', use_column_width=True)
                st.write("-Esses foram os dados que treinaram a Máquina Virtual que faz a previsão do preço.")
            except Exception as e:
                st.error(f"Erro ao abrir a imagem: {e}")
    else:
        st.warning("A imagem do gráfico não foi encontrada.")
    st.balloons()  # Adiciona balões de festa ao resultado