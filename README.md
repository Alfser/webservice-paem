english | [portuguese](./README_PT.md)



- [Webservice PAEM](#webservice-paem)
  - [Setup](#setup)
    - [Prerequisites](#prerequisites)
      - [Operational System Windows 7, 8 or 10](#operational-system-windows-7-8-or-10)
      - [MySQL database.](#mysql-database)
      - [Python 3.7](#python-37)
      - [Pip](#pip)
      - [Pipenv](#pipenv)
      - [Python libraries](#python-libraries)
  - [Clone](#clone)
  - [Usage](#usage)
      - [Python Libraries](#python-libraries-1)
      - [Developer](#developer)
        - [Using pipenv](#using-pipenv)
        - [Setup database](#setup-database)
      - [Customer](#customer)
        - [Routes](#routes)
        - [Getting starter](#getting-starter)
        - [Exemples](#exemples)
  - [Documentations](#documentations)
  - [License](#license)

# Webservice PAEM
That webservice provide resources for using in PAEM UFOPA Project. This project aims to manage access of studanties and servers into the University 
by checking if the resources requested for that user is available and if the user is healthy. So, the project will have four application:
that webservice to manage data requested from other aplications; a system for manage the entrance for the concierge; a system for the user request entry into University
and finally a ChatBot for the user request entry as well.  
## Setup

### Prerequisites

#### Operational System Windows 7, 8 or 10

#### MySQL database.

We are current using [MySQL Comminity version 8.0.23](https://dev.mysql.com/downloads/installer/)

#### Python 3.7

You will need the Python 3.7. It's recomend download the latest version 3.7.x. To verify the installed version you have to follow the steps below:

1. Opend the command line (`CTRL+R` e digite _cmd_).

2. Type `python --version`.

If the version is presented correctly, Python is installed properly. The `python --version` command can't point to a version of Python 2.x.x.

If the Python are not installed or the version is incorrect, you need to make an alternative install of Python doing the following steps:

1. Download the python vesion [here](https://www.python.org/downloads/source/).

2. Remember to looking for 3.7.x version, where x is the latest version:

3. download the installer of 64 bits **Windows installer(64-bit)**.

4. Run the installer.

5. Check **install launch for all user** e **Add Python 3.8 to PATH** options.

6. Click __install Now__ option. Thus, Python will be installed correctly.

#### Pip
You will need Pip installed in the Python environment. If you followed the Python installation process described in this document, the Pip installation won't be necessary, so is **highly** recommended to follow the process described here even if you already have Python installed natively on Ubuntu.

To check if Pip is correctly installed, open the terminal and type one of the following commands:

```
> pip --version
> pip3 --version
> python -m pip --version
```

**Disclaimer**: If pip was not installed you need to install.

#### Pipenv

If you installed Python 3.8 according to this document, you can install Pipenv using:

```
> python -m pip install pipenv
or
> pip install pipenv
```

To check if the installation was successful use:

```
> python -m pipenv --version
or
> pipenv --version
```
Thus you can init the virtual enviroment into the repository typing `pipenv shell`. So [leanig other commands](https://github.com/pypa/pipenv).

#### Python libraries

To install the Python requirements open the command line in repository root and type the command `pip install -r \requirementes.txt` into the root repository.

## Clone

To clone the repository follow the steps below:

1. Install the Git in your computer.
2. Click right mouse button.
3. Select `Git Bash here` option.
3. Clone repository typing `git clone https://github.com/flaviacomp/app-paem-db-restful.git`. Then now, start to code!

## Usage
#### Python Libraries
Before using the webservice you need to install the python requirements by the command `pip install -r requirements.txt` if you'are not developer (for deveoper use pipenv)

#### Developer
The use of this repository is the same as the other Git repositories. Only a few differences need to be pointed out. 
For an overwiew of this project see [Arquitetura do Projeto](./ARCHTECTURE.md)
##### Using pipenv
 1. First of all, you have to install pipenv as global package by command `pip install -g pipenv`.
 2. Now, for create a virtual enviroment use the command `pipenv install`.
 3. Finally, for active the virtual anviroment use the command `pipenv shell`
 
>You **NEED** to use Pipenv for package management. Because of this it was installed and should be used from now on. 
>You can learn how to use Pipenv [here](https://github.com/pypa/pipenv) and [here](https://pipenvkennethreitz.org/en/latest/).

>You should **NEVER** commit using the command `git commit -m <message>`. The `-m` parameter bypass the commit template. 
>You should **ALWAYS** commit using just the command `git commit`.

##### Setup database
Run the script [create_import_db](./create_import_db.py). Ele criará um banco de dados local e realiza a inserção automática de valores _fake_ ao banco criado, usados para tests. Vale lembara que **para a criação do banco o [SGBD MYSQL](https://dev.mysql.com/downloads/installer/) deve está instalado e as credênciais devem está de acordo com as do seu servidor mysql local, no caso dos tests locais. Coloque as credências num arquivo chamado `connection.json` na pasta database com as informações requeridas no módulo [config](./app/database/config.py), se não houver o arquivo, crie-o**.
#### Customer
##### Routes
This webservice is in development. So, there's just some Routes available for now and *it's Routes can be changed* in the future.
Endpoints available:
 - `/auth` : Use to *login in API*. It obtain a token to access its endpoints. 
   - Method(s) available: **POST** method to request the token by send a json into the body of request _basic authentrication_ by parsing **user** and **password**.
   - Usage: send a _http basic authentication_ of the request.
   - Return: `{"token":"token value"}`
 - `/auth.bot` : Use to *login in API*. It obtain a token to access its endpoints. 
   - Method(s) available: **POST** method to request the token by send a **CPF** as a head.
   - Usage: send a CPF as a head of the request. `ex.: {"Authentication":"Bearer [CPF value]"}`
 - `/usuarios` : Use to see the users recorded. 
   - Method(s) available: **GET** method is available to request this endpoint.
   - Return:
   
   ```json
      [
        {
        "nome": "admin",
        "id": 1,
        "cpf": "11111111111"
        },
        {
        "nome": "teste_tecnico",
        "id": 2,
        "cpf": "22222222222"
        },
        ...
        {
        "nome": "teste_portaria",
        "id": 7,
        "cpf": "77777777777"
        },
        {
        "nome": "fooTecnico3",
        "id": 8,
        "cpf": "048573534322452"
        }
      ]
   ```

 - `/usuarios/usuario` : Use to **see**, **update** and **delete** a especific _usuario_. 
   - Method(s) available: **GET**, **PUT** and **DELETE** methods.
   - Usage **DELETE**: need to send a a query string *id_usuario* to delete the user
   - Usage **PUT**: need to send a body user to be updated into request along with *id_usuario* like:
   
    ```json
      {
        "id_usuario": "user integer",
        "login": "login string",
        "cpf": "cpf value string",
        "email":"email string",
        "tipo":"tipo Integer",
      }  
    ```   
   - Return **GET**: Return the user logged
   
    ```json
      {
        "id_usuario": "user integer",
        "login": "login string",
        "cpf": "cpf value string",
        "email":"email string",
        "tipo":"tipo integer",
      } 
    ```

 - `/discentes/discente` : Use to **see** a especific discente. You just can use **GET** method and you must put a param named **maticula** with matricula number of discente to make the respective usages. Also use to **create** and **delete** a especific discente. You can use **GET**, **POST** and **DELETE** methods by parsing _id_discente_ as a query string.
 - `/discentes` : Use to **see** a all discentes recorded in database. You just can use **GET** method for now of discente to make the respective usages.
 - `/solicitacoes_acessos` : Use to see the values into the *solicitacao_cesso* table. You can use just **GET** method to make resquest to server.
 - `/solicitacoes_acessos/solicitacao_acesso` : Use to **see**, **create**, **update** and **delete** a especific solicitacao_acesso. You can use **GET**, **POST**, **PUT** and **DELETE** methods by parsing _id_solicitacao_acesso_ as a query string.
 - `/acessos_permitido` : Use to **see** the values into the table *acesso_permitido* recorded into the database. You can just use the **GET** method to access this route.
 - `/acessos_permitido/acesso_permitido` : Use to **see**, **create**, **update** and **delete** a especific _acesso_permitido_ into the table _acesso_permitido_ recorded into the database. You can use **GET**, **POST**, **PUT** and **DELETE** methods by parsing _id_acesso_permitido_ as a query string.
 - `/tecnicos/tecnico` : Use to **see**, **create** and **delete** a especific _tecnico_. You can use **GET**, **POST** and **DELETE** methods by parsing _id_tecnico_ as a query string.
 - `/tecnicos` : Use to **see** the values into the table _tecnico_ recorded into the database. You can just use the **GET** method to access this route.
 - `/recursos_campus/recurso_campus` : Use to **see**, **create** and **delete** a especific _recurso_campus_. You can use **GET**, **POST** and **DELETE** methods by parsing _id_tecnico_ as a query string.
 - `/recursos_campus` : Use to **see** the values into the table _recurso_campus_ recorded into the database. You can just use the **GET** method to access this route.
 - `/campus/campi` : Use to **see**, **create** and **delete** a especific _recurso_campus_. You can use **GET**, **POST** and **DELETE** methods by parsing _id_tecnico_ as a query string.
 - `/campus` : Use to **see** the values into the table _recurso_campus_ recorded into the database. You can just use the **GET** method to access this route.

##### Getting starter
First of all, considering usage in devoloping enviroment, you need to change the [database connections file](/app/database/connection.json) create a database run the script [create and import database](/create_import_db.py) 
by run `python create_import_db.py`. That create a database structure and import some data
test from csv files that there're into this repository. Then run the webserice by the command `python main_app.py` into this repository. 
Is the file [main app](/main.py). Thus, it's ready to make request to the server. By default the route server **http://localhost:5000/api.paem** 

##### Exemples
You can access the webservice routes by adding the server adress and the route that you need to access.

* Using browser to access to login.

GET resquest:
>_http://localhost:5000/api.paem/auth_ and parsing basic authentication

Response:
```json
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MywiZXhwIjoxNjIwMzE1ODA2fQ.HYbJi6CqAxoho5bu00E464lfkXMuWixzl6CT8yz8PO4"
}
```

* Using python

GET resquest:
```python
# request all discentes recorded into database. 
import requests

# change TOKEN to valide token
headers = {"Authorization":f"Bearer TOKEN"}

res = requests.get("http://localhost:5000/api.paem/discentes", headers=headers)

print("status_code: ",res.status_code)
print("text: ", res.text)

```
Response:
```json
status_code:  200

text:  [
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

>Some exemples of consuming this *webservice* is found [here](/exemple) 

## Documentations

Webservice PAEM Documentation will be here in the future.

## License

Copyright 2021 UFOPA-Projeto PAEM.

Licensed to the Apache Software Foundation (ASF) under one or more contributor license agreements. See the NOTICE file distributed with this work for additional information regarding copyright ownership. The ASF licenses this file to you under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.