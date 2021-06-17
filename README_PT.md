- [Webservice PAEM](#webservice-paem)
  - [Configurar](#configurar)
    - [Pré-requisitos](#pré-requisitos)
      - [Sistema Operacional Windows 7, 8 ou 10](#sistema-operacional-windows-7-8-ou-10)
      - [Banco de dados MySQL.](#banco-de-dados-mysql)
      - [Python 3.7](#python-37)
      - [Pip](#pip)
      - [Pipenv](#pipenv)
      - [Bibliotecas Python](#bibliotecas-python)
  - [Clone](#clone)
  - [Uso](#uso)
      - [Bibliotecas Python](#bibliotecas-python-1)
      - [Desenvolvedor](#desenvolvedor)
        - [Usando pipenv](#usando-pipenv)
        - [Configurar banco de dados](#configurar-banco-de-dados)
      - [Cliente](#cliente)
        - [Rotas](#rotas)
        - [Começando](#começando)
        - [Exemplos](#exemplos)
  - [Documentações](#documentações)
  - [Licença](#licença)

# Webservice PAEM

Esse webservice disponibiliza recursos para utilização no Projeto PAEM UFOPA. O projeto visa gerenciar o acesso de estudiosos e servidores à Universidade verificando se os recursos solicitados para aquele usuário estão disponíveis e se o usuário está íntegro. Portanto, o projeto terá quatro aplicações:
aquele webservice para gerenciar dados solicitados de outras aplicações; sistema de gerenciamento de entrada da portaria; um sistema para a entrada do usuário na universidade
e, finalmente, um ChatBot para a entrada de solicitação do usuário também.

## Configurar

### Pré-requisitos

#### Sistema Operacional Windows 7, 8 ou 10

#### Banco de dados MySQL.

No momento, estamos usando o [MySQL Comminity versão 8.0.23](https://dev.mysql.com/downloads/installer/)

#### Python 3.7

Você precisará do Python 3.7. É recomendável baixar a última versão 3.7.x. Para verificar a versão instalada, você deve seguir os passos abaixo:

1. Abra a linha de comando (`CTRL + R` e digite _cmd_).

2. Digite `python --version`.

Se a versão for apresentada corretamente, o Python está instalado corretamente. O comando `python --version` não pode apontar para uma versão do Python 2.x.x.

Se o Python não estiver instalado ou a versão estiver incorreta, você precisará fazer uma instalação alternativa do Python executando as seguintes etapas:

1. Baixe a versão do python [aqui](https://www.python.org/downloads/source/).

2. Lembre-se de procurar a versão 3.7.x, onde x é a versão mais recente:

3. baixe o instalador de 64 bits **Windows installer(64 bits)**.

4. Execute o instalador.

5. Marque **install launch for all user** e **Add Python 3.8 to PATH** options.

6. Clique na opção __instalar agora__. Assim, o Python será instalado corretamente.

#### Pip
Você precisará do Pip instalado no ambiente Python. Se você seguiu o processo de instalação do Python descrito neste documento, a instalação do Pip não será necessária, portanto, é **altamente** recomendado seguir o processo descrito aqui, mesmo se você já tiver o Python instalado nativamente no Ubuntu.

Para verificar se o Pip está instalado corretamente, abra o terminal e digite um dos seguintes comandos:

```bash
> pip --version
> pip3 --version
> python -m pip --version
```

**Disclaimer**: se o pip não foi instalado, você precisa instalá-lo.

#### Pipenv

Se você instalou o Python 3.8 de acordo com este documento, pode instalar o Pipenv usando:

```bash
> python -m pip install pipenv
ou
> pip install pipenv
```

Para verificar se a instalação foi bem-sucedida, use:

```bash
> python -m pipenv --version
ou
> pipenv --version
```
Assim, você pode iniciar o ambiente virtual no repositório digitando `pipenv shell`. Então, [leanig outros comandos](https://github.com/pypa/pipenv).

#### Bibliotecas Python

Para instalar os requisitos do Python, abra a linha de comando na raiz do repositório e digite o comando `pip install -r requirements.txt` no repositório raiz ou use o Pipenv na secção [usando pipenv](#usando-pipenv).

## Clone

Para clonar o repositório, siga as etapas abaixo:

1. Instale o Git em seu computador.
2. Clique com o botão direito do mouse.
3. Selecione a opção `Git Bash aqui` ou use o powershel mesmo.
3. Clone o repositório digitando `git clone https://github.com/flaviacomp/app-paem-db-restful.git`. Então agora, comece a codificar!

## Uso

#### Bibliotecas Python
Antes de usar o serviço da web, você precisa instalar os requisitos do python pelo comando `pip install -r requisitos.txt` se você não for um desenvolvedor (para desenvolvedor, use pipenv)

#### Desenvolvedor
O uso deste repositório é o mesmo que os outros repositórios Git. Apenas algumas diferenças precisam ser apontadas.
Para uma visão geral deste projeto veja [Arquitetura do Projeto](./ARCHTECTURE.md)
##### Usando pipenv
 1. Em primeiro lugar, você deve instalar o pipenv como um pacote global pelo comando `pip install -g pipenv`.
 2. Agora, para criar um ambiente virtual, use o comando `pipenv install`.
 3. Finalmente, para ativar o antiviroment virtual use o comando `pipenv shell`
 
> Você **PRECISA** usar o Pipenv para gerenciamento de pacotes. Por isso ele foi instalado e deve ser usado a partir de agora.
> Você pode aprender como usar o Pipenv [aqui] (https://github.com/pypa/pipenv) e [aqui] (https://pipenvkennethreitz.org/en/latest/).

> Você deve **NUNCA** confirmar usando o comando `git commit -m <message>`. O parâmetro `-m` ignora o modelo de confirmação.
> Você deve **SEMPRE** confirmar usando apenas o comando `git commit`.

##### Configurar banco de dados

Execute o script [create_import_db](./create_import_db.py). Ele criará um banco de dados local e realiza a inserção automática de valores _fake_ ao banco criado, usados ​​para testes. Vale lembara que ** para a criação do banco o [SGBD MYSQL](https://dev.mysql.com/downloads/installer/) deve está instalado e como credênciais deve estar de acordo com como seu servidor mysql local, não caso dos testes locais. Coloque as credências num arquivo chamado `connection.json` na pasta database com as informações requeridas no módulo [config](./app/database/config.py), se não houver o arquivo, crie-o **.

#### Cliente

##### Rotas

Este serviço da web está em desenvolvimento. Portanto, há apenas algumas rotas disponíveis por enquanto e * suas rotas podem ser alteradas * no futuro.
Endpoints disponíveis:
- `/auth`: Use para *fazer login na API*. Você deve obter um token para acessar os outros terminais desta API. Você pode simplesmente usar o método **GET** para solicitar o token, enviando um json para o corpo da solicitação _ententricação básica_, analisando **usuário** e **senha**.
- `/usuarios`: Use para **ver** os usuários registrados no banco de dados. apenas o método **GET** está disponível para solicitar este endpoint.
- `/usuarios/usuario`: Use para **ver**, **criar** e **deletar** um _usuário_ específico. Você pode usar os métodos **GET**, **POST** e **DELETE** analisando _id_discente_ como uma string de consulta.
- `/discentes/discente`: ​​Use para **ver** um discente específico. Você só pode usar o método **GET** e deve colocar um parâmetro chamado **maticula** com o número da matrícula do discente para fazer os respectivos usos. Use também para **criar** e **excluir** um discente específico. Você pode usar os métodos **GET**, **POST** e **DELETE** analisando _id_discente_ como uma string de consulta.
- `/discentes`: Use para **ver** todos os discentes registrados no banco de dados. Você só pode usar o método **GET** por enquanto do discente para fazer os respectivos usos.
- `/solicitacoes_acessos`: Use para **ver** os valores na tabela *solicitacao_cesso*. Você pode usar apenas o método **GET** para fazer uma solicitação ao servidor.
- `/solicitacoes_acessos/solicitacao_acesso`: Use para **ver**, **criar**, **atualizar** e **excluir** uma especificação *solicitacao_acesso*. Você pode usar os métodos **GET**, **POST**, **PUT** e **DELETE** analisando *id_solicitacao_acesso* como uma string de consulta.
- `/acessos_permitido`: Use para **ver** os valores na tabela *acesso_permitido* registrado no banco de dados. Você pode apenas usar o método **GET** para acessar esta rota.
- `/acessos_permitido/acesso_permitido`: Use para **ver**, **criar**, **atualizar** e **excluir** um _acesso_permitido_ específico na tabela _acesso_permitido_ registrado no banco de dados. Você pode usar os métodos **GET**, **POST**, **PUT** e **DELETE** analisando _id_acesso_permitido_ como uma string de consulta.
- `/tecnicos/tecnico`: Use para **ver**, **criar** e **deletar** um _técnico_ específico. Você pode usar os métodos **GET**, **POST** e **DELETE** analisando *id_tecnico* como uma string de consulta.
- `/tecnicos`: Use para **ver** os valores na tabela _tecnico_ gravada no banco de dados. Você pode apenas usar o método **GET** para acessar esta rota.
- `/recurso_campus/recurso_campus`: use para **ver**, **criar** e **excluir** um _recurso_campus_ específico. Você pode usar os métodos **GET**, **POST** e **DELETE** analisando *id_tecnico* como uma string de consulta.
- `/recursos_campus`: Use para **ver** os valores na tabela _recurso_campus_ gravada no banco de dados. Você pode apenas usar o método **GET** para acessar esta rota.

##### Começando
Em primeiro lugar, considerando o uso no ambiente de desenvolvimento, você precisa alterar o [arquivo de conexões do banco de dados](/app/database/connection.json) criar um banco de dados, executar o script [criar e importar banco de dados](/create_import_db.py)
executando `python create_import_db.py`. Que criam uma estrutura de banco de dados e importam alguns dados
teste de arquivos csv que estão neste repositório. Então execute o webserice pelo comando `python main_app.py` neste repositório.
É o arquivo [app principal](/main.py). Assim, ele está pronto para fazer a solicitação ao servidor. Por padrão, o servidor de rota **http://localhost:5000/api.paem**

##### Exemplos
Você pode acessar as rotas de serviço da web adicionando o endereço do servidor e a rota que você precisa acessar.

* Usando o navegador para acessar o login.

Solicitação GET:
> _http: // localhost: 5000 / api.paem / auth_ e análise de autenticação básica

Resposta:
```json
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MywiZXhwIjoxNjIwMzE1ODA2fQ.HYbJi6CqAxoho5bu00E464lfk8X4Mu"
}
```

* Usando python

Solicitação GET:
```python
# solicita todos os discentes registrados no banco de dados.
import requests

# alterar TOKEN para valide token
headers = {"Autorização": f "TOKEN do portador"}

res = requests.get ("http://localhost:5000/api.paem/discentes", headers = headers)

imprimir ("status_code:", res.status_code)
imprimir ("texto:", res.text)

```
Resposta:
```json
status_code: 200

texto:  [
    {
        "id_usuario": 1,
        "login": "admin",
        "email": "admin@teste.com",
        "tipo": 0
    },
    {
        "id_usuario": 2,
        "login": "teste_tecnico",
        "email": "tecnico@teste.com",
        "tipo": 1
    },
    ...
    ,
    {
        "id_usuario": 6,
        "login": "teste_discente_3",
        "email": "discente3@teste.com",
        "tipo": 3
    },
    {
        "id_usuario": 7,
        "login": "teste_portaria",
        "email": "portaria@teste.com",
        "tipo": 4
    }
]
```

> Alguns exemplos de consumo deste _web service_ podem ser encontrados [aqui] (/ exemple)

## Documentações

A documentação do Webservice PAEM estará aqui no futuro.

## Licença

Copyright 2021 UFOPA-Projeto PAEM.

Licensed to the Apache Software Foundation (ASF) under one or more contributor license agreements. See the NOTICE file distributed with this work for additional information regarding copyright ownership. The ASF licenses this file to you under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.