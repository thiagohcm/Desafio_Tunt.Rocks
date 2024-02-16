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

Você pode verificar se o python está instalado corretamente, executando em seu terminal os comandos :

``` bash
python --version
```

```bash
pip --version
```

O pip é o sistema de gerenciamento de pacotes para python, ele vem junto ao python no processo de instalação.


Agora após ter instalado o python, entre no diretório no qual deseja clonar o repositório do projeto.
- Clone o repositório do projeto:

```bash
git clone https://github.com/thiagohcm/Desafio_Tunt.Rocks.git
```

- Após clonar o repositório do projeto para sua máquina o próximo passo é entrar no diretório do projeto com:

```bash
cd Desafio_Tunt.Rocks
```

- Dentro do projeto criar um ambiente virtual:

```bash
python -m venv venv
```

- Para ativar o ambiente virtual no Windows, executar:

```bash
.\venv\Scripts\activate
```

- Caso Linux, executar:

```bash
source venv/bin/activate
```

- Instalar as dependências necessárias através do requirements.txt:

```bash
pip install -r requirements.txt
```

# Como executar a aplicação 

Após fazer a instalação de todas as dependências será possível rodar o código principal. 
Com o terminal aberto no repositório entre no diretório src com :

```bash
cd src
```

- No diretório src, executar :
```bash
python app.py
```
- Ou caso alguma problema, tente:
```bash
python3 app.py
```
Após executar o código, a planilha no Google Sheets será atualizada conforme regras do desafio.

## Logs

Válido ressaltar que após executar o código será criado um diretório logs e um arquivo de log para acompanhar as
atividades da aplicação.

## Google API

A aplicação foi criada utilizando a forma de acesso a planilha através da API do Google utilizando uma aplicação criada
no Google Cloud em minha conta gmail. A forma de validar credencial utilizada foi a de "Contas de serviço" pois caso fosse utilizado
"IDs do cliente OAuth 2.0" é necessário realizar um autenticação por usuário utilizando um email 
Google, mas o problema estava que devido a aplicação criada não ter sido verificada pelo Google, ela informava na 
primeira autenticação que era um app não verificado e era preciso realizar um processo que iria dificultar e atrapalhar a experiência
para o teste da execução correta do desafio.

Caso desejar verificar o funcionamento utilizando a sua aplicação do Google Cloud, basta substituir o arquivo 
credentials.json (Mantendo a nomeclatura) dentro de src/modules/service/client_credentials/

E se desejar utilizar outra planilha, basta substituir com o ID da nova planilha na variável spreadsheet_id em src/app.py

Documentação sobre Google authentication and authorization [aqui](https://developers.google.com/workspace/guides/auth-overview).

OBS: O link para a planilha, junto ao deste repositório e o passo a passo para executar a aplicação foi enviado 
na entrega do projeto na plataforma.