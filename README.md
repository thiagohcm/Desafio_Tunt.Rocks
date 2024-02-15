# Desafio Tunts.Rocks 2024
PROCESSO SELETIVO – DESAFIO DE PROGRAMAÇÃO – NÍVEL 1 

# Objetivo
Criar uma aplicação em uma linguagem de programação de sua preferência (caso esteja se  candidatando a 
uma vaga de linguagem de programação específica, exemplo: programador  node.js, utilizar a linguagem/tecnologia 
específica da vaga). A aplicação deve ser capaz de ler  uma planilha do google sheets, buscar as informações 
necessárias, calcular e escrever o  resultado na planilha. 

# Pré-requisitos
Para executar o projeto é necessário primeiramente ter o python => 3.12 instalado em sua máquina. Você pode encontrar 
o python para download [aqui](https://www.python.org/downloads/) 

Você pode checar se está tudo instalado corretamente rodando em seu terminal os comandos :

``` bash
python --version
```

```bash
pip --version
```

- Primeiro clone o repositório do projeto

```bash
git clone https://github.com/thiagohcm/Desafio_Tunt.Rocks.git
```

- Após clonar o repositório do projeto para sua máquina o próximo passo é criar um ambiente virtual

```bash
python -m venv venv
```

- Para ativar o ambiente virtual no Windows, rodar:

```bash
.\venv\Scripts\activate
```

- Caso Linux, rodar:

```bash
source venv/bin/activate
```

- Instalar as dependências necessárias através do requirements.txt

```bash
pip install -r requirements.txt
```

# Como executar a aplicação 

Após fazer a instalação de todas as dependências será possível rodar o código principal. 
Com o terminal aberto no repositório rode o seguinte comando :

```bash
python .\src\app.py 
```

## Google API

A aplicação foi criada utilizando a forma de acesso a planilha através da API do Google utilizando uma aplicação criada
no Google Cloud em minha conta gmail. A forma de credencial utilizado foi a de "Contas de serviço" pois caso fosse utilizado
"IDs do cliente OAuth 2.0" é necessário realizar um autenticação por usuário na primeira conexão utilizando um email 
Google, mas o problema estava que devido a aplicação criada não ter sido verificada pelo Google, ela informava na 
primeira autenticação que era um app não verificado e era preciso realizar um processo que iria atrapalhar a experiência
para o teste do desafio.  


O link para a planilha será enviado na entrega do projeto.