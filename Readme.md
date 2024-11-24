Previsão de Preço de Pizza com Machine Learning
Este projeto demonstra como criar uma aplicação web simples para prever o preço de pizzas com base no diâmetro usando Machine Learning. Utilizamos o Streamlit para criar a interface web e o Scikit-learn para treinar o modelo de regressão linear.

Visão Geral
A aplicação permite que o usuário insira o diâmetro de uma pizza e, com base em um modelo de regressão linear treinado, prevê o preço da pizza. A interface é intuitiva e fácil de usar, e a previsão é feita em tempo real sem a necessidade de cálculos matemáticos manuais.

Funcionalidades
Previsão de Preço: Insira o diâmetro da pizza e obtenha uma previsão instantânea do preço.
Visualização de Dados: Visualize um gráfico de dispersão dos dados usados para treinar o modelo.
Interface Web: Interface amigável e interativa criada com Streamlit.
Estrutura do Projeto
app.py: Código principal da aplicação.
pizzas.csv: Arquivo CSV contendo os dados de treinamento.
Figure_ploat-scatter.png: Imagem do gráfico de dispersão dos dados de treinamento.
Dependências
Este projeto utiliza o Poetry para gerenciar as dependências. O Poetry facilita a instalação e o gerenciamento das bibliotecas necessárias para o projeto.

Bibliotecas Utilizadas
streamlit: Para criar a interface web.
pandas: Para manipulação de dados.
scikit-learn: Para treinar o modelo de regressão linear.
matplotlib: Para visualização de dados.
Instalação
Clone o repositório:

Instale o Poetry:

Instale as dependências do projeto:

Executando a Aplicação
Ative o ambiente virtual do Poetry:

Execute a aplicação:

Como Funciona
Treinamento do Modelo: O modelo de regressão linear é treinado usando dados de diâmetro e preço de pizzas armazenados no arquivo pizzas.csv.
Previsão: O usuário insere o diâmetro da pizza na interface web, e o modelo prevê o preço com base no diâmetro fornecido.
Visualização: O usuário pode visualizar um gráfico de dispersão dos dados de treinamento clicando em um botão na interface.
Por Que Usar o Poetry?
O Poetry simplifica o gerenciamento de dependências e ambientes virtuais, tornando o desenvolvimento mais eficiente e organizado. Com o Poetry, você pode facilmente instalar, atualizar e remover dependências, além de garantir que todos os desenvolvedores do projeto estejam usando as mesmas versões das bibliotecas.

Conclusão
Este projeto demonstra como é rápido e fácil criar uma aplicação web de Machine Learning para prever preços sem a necessidade de cálculos matemáticos manuais. Com o Streamlit e o Scikit-learn, você pode desenvolver e implantar modelos de Machine Learning de forma eficiente e intuitiva.