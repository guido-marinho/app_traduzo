# Traduzo  
O Traduzo é uma aplicação web simples que oferece funcionalidades básicas de tradução de texto entre diferentes idiomas. Utilizando a API do Google Translator, o Traduzo permite que os usuários ingressem um texto, escolham o idioma de origem e o idioma de destino, e obtenham a tradução correspondente.

## Funcionalidades Principais
Tradução Simples
Insira o texto que deseja traduzir, escolha o idioma de origem e o idioma de destino, e obtenha a tradução instantânea.

## Histórico de Traduções
O Traduzo mantém um histórico das traduções realizadas, incluindo detalhes como texto original, idioma de origem, idioma de destino e a tradução resultante no endpoint /history.

## Como Rodar o Projeto

Clone o Repositório:

```bash
git@github.com:guido-marinho/app_traduzo.git
```
Navegue até o Diretório do Projeto:

```bash
cd app_traduzo
```
Execute o Docker Compose:

```bash
docker-compose up --build
```
Este comando irá construir e iniciar os containers Docker necessários para o aplicativo.

## Acesse o Aplicativo
Abra o navegador e visite http://localhost:8000 para acessar o Traduzo.

## Utilize o Aplicativo
Insira o texto que deseja traduzir.
Escolha o idioma de origem e o idioma de destino.
Clique no botão de tradução para ver o resultado.
Explore o histórico de traduções na página de histórico.
Observações
Certifique-se de ter o Docker e o Docker Compose instalados em seu sistema.
O aplicativo estará disponível em http://localhost:8000.
O ambiente de desenvolvimento está configurado automaticamente para depuração (debug=True). Certifique-se de ajustar as configurações para um ambiente de produção conforme necessário.
## Dependências
O Traduzo utiliza as seguintes bibliotecas e ferramentas:

Flask + Jinja2 - Framework web para Python.
deep-translator - Biblioteca para tradução de texto usando várias APIs, incluindo o Google Translator.
MongoDB - Banco de dados NoSQL utilizado para armazenar o histórico de traduções.
Certifique-se de revisar o arquivo docker-compose.yml para obter informações adicionais sobre a configuração do ambiente Docker.

Divirta-se traduzindo com o Traduzo!
