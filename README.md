português | [inglês](./README_ENG.md)

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
        - [Começando](#começando)
        - [Exemplos](#exemplos)
  - [Endpoints](#endpoints)
    - [Para tela de Estatísticas](#para-tela-de-estatísticas)
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

## Endpoints

Este serviço da web está em desenvolvimento. Portanto, há apenas algumas rotas disponíveis por enquanto e * suas rotas podem ser alteradas * no futuro.
Endpoints disponíveis:

 - `/auth` : Uso para o *login in* na API. Assim é obtido o token para o acesso as rotas. 
   - Método(s) disponíveis: Método **POST** acesso via requisição http _basic authentrication_ passando o _usuário ou email_ e _senha_.
   - Uso: Requisição _http basic authentication_.
   - Resposta: `{"token":"token value"}`
    
 - `/auth.bot` : Uso para *login in* na API. Assim, se o obtém o token apara acessar os endpoints. 
   - Método(s) disponíveis: **POST** realiza a requisição do token enviando o **CPF** no Head da requisição.
   - Uso: Enviar o CPF seguinto como um json de acordocom o exemple a seguir: 
   
   ```json 
      
      {
        "Authentication":"Bearer [CPF value]"
      }
   
   ```

   - Resposta: `{"token":"token value"}`
   
 - `/usuarios` : Usado obter os dados de todos os usuários. 
   - Metodo(s) disponíveis: **GET** para obtenção de alguns dados dos usuários.
   - Resposta:
   
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

 - `/usuarios/usuario` : Use para **ver**, **atualizar** e **deletar** um usuário específico. 
   - Metodo(s) disponíveis: **GET**, **PUT** e **DELETE**.
   - Uso do **DELETE**: Para deletar um usuário, precisa enviar o id do usuário na query string *id_usuario*.
     - route:
       - `/usuarios/usuario?id_usuario=value`
      
   - Uso do **PUT**: Para atualizar o usuário precisa enviar os dados que deseja atualizar no body da requisição junto com o *id_usuario* como segue:
   
      ```json
        {
          "id_usuario": "*integer",
          "login": "string(45)",
          "cpf": "string(15)",
          "email":"string(45) format name@mail.com",
          "tipo":"integer",
          "senha":"text",
          "campus_instituto_id_campus_instituto":"integer"
        }  
      ```

   - Resposta **GET**: Retorna os dados do usuário logado.
   
      ```json
        {
          "id_usuario": "integer",
          "login": "string(45)",
          "cpf": "string(15)",
          "email":"string(45) format name@mail.com",
          "tipo":"Integer",
          "campus_instituto_id_campus_instituto":"integer"
        } 
      ```

 - `/discentes/discente`: ​​Use para **ver**, **editar**, **criar**, **excluir** um discente específico. 
   - Método(s) disponíveis: **GET**, **POST**, **PUT**, **DELETE** 
   - Uso do **GET**: Obtem os dados do discente de usuário logado. Não é necessário nenhum parâmatro na requisição.
       - Response:

       ```json
          {
            "id_discente": "integer", 
            "nome": "string(45)",
            "matricula": "string(45)",
            "entrada": "string(6)",
            "data_nascimento":"string format yyyy-mm-dd",
            "ano_de_ingresso":"integer",
            "sexo":"string(2)",
            "quantidade_pessoas":"integer",
            "quantidade_vacinas":"integer",
            "fabricantes":"string(45)",
            "justificativa":"text",
            "semestre":"integer",
            "endereco":"string(45)",
            "grupo_risco":"boolean(1 ou 0)",
            "status_covid":"boolean(1 ou 0)",
            "status_permissao":"boolean(1 ou 0)",
            "usuario": {
                "id_usuario":"integer",
                "login":"string(45)",
                "cpf":"string(15)",
                "email":"string(45)",
                "tipo":"integer",
                "campus_instituto_id_campus_instituto":"integer"
            },
            "curso_id_curso":"integer",
            "curso": "string(45)",
            "campus_instituto_id_campus_instituto":"integer",
            "campus_instituto": "string(45)"
          }
         
       ``` 
   
   - Uso do **POST**: Cria um usuário discente de acordo com os dados enviados no body da requisição
     - Campos que podem ser enviados no body:
     
     ```json

      {
        "discente":{
            "nome": "string(45)",
            "matricula": "string(45)",
            "entrada": "string(6)",
            "data_nascimento":"string format dd-mm-yyyy",
            "ano_de_ingresso":"integer",
            "sexo":"string(2)",
            "quantidade_pessoas":"integer",
            "quantidade_vacinas":"integer",
            "fabricantes":"string(45)",
            "justificativa":"text",
            "semestre":"integer",
            "endereco":"string(45)",
            "grupo_risco":"boolean(1 ou 0)",
            "status_covid":"boolean(1 ou 0)",
            "status_permissao":"boolean(1 ou 0)"
        },
        "usuario": {
            "id_usuario":"integer",
            "login":"*string(45)",
            "cpf":"string(15)",
            "email":"*string(45)",
            "tipo":"*integer",
            "campus_instituto_id_campus_instituto":"*integer"
        },
        "curso_id_curso":"*integer",
        "campus_instituto_id_campus_instituto":"integer"
      }
     ``` 

   - Uso do **PUT**: Atualiza os dados do discente correspondente ao *id_discente* enviado no body
     - body da requisição:
     ```json
     
      {
        "id_discente":"*integer",
        "nome": "string(45)",
        "matricula": "string(45)",
        "entrada": "string(6)",
        "data_nascimento":"string format dd-mm-yyyy",
        "ano_de_ingresso":"integer",
        "sexo":"string(2)",
        "quantidade_pessoas":"integer",
        "quantidade_vacinas":"integer",
        "fabricantes":"string(45)",
        "justificativa":"text",
        "semestre":"integer",
        "endereco":"string(45)",
        "grupo_risco":"boolean(1 ou 0)",
        "status_covid":"boolean(1 ou 0)",
        "status_permissao":"boolean(1 ou 0)",
        "curso_id_curso":"integer",
        "campus_instituto_id_campus_instituto":"integer"
      }
     
     ``` 

   - Uso do **DELETE**: Deleta o usuário discente correspondente ao *id_discente* enviado como query string
     - Query string: *id_discente = integer*
     - Route: 
       - `/discentes/discente?id_discente=value"`
  
 - `/discentes`: Use para **ver** todos os discentes registrados no banco de dados.
    - Metodo(s) disponíveis: **GET** para obtenção de alguns dados dos discentes.
    - Resposta:
   
    ```json
        [
          {
            "nome": "*string",
            "id": <*integer>,
            "matricula": "*string"
          },
          {
            "nome": "*string",
            "id": <*integer>,
            "matricula": "*string"
          },
          ...
          {
            "nome": "*string",
            "id": <*integer>,
            "matricula": "*string"
          },
          {
            "nome": "*string",
            "id": <*integer>,
            "matricula": "*string"
          }
        ]
    ```

 - `/solicitacoes_acessos/solicitacao_acesso`: ​​Use para **ver**, **editar**, **criar**, **excluir** uma solicitação de acesso ao campus realizada pelo usuário específica. 
   - Método(s) disponíveis: **GET**, **POST**, **PUT**, **DELETE** 
   - Uso do **GET**: Obtem os dados do acesso solicitado de acordo com o *id_discente* ou o *id_solicitacao_acesso*
     - query strings: *id_solicitacao_acesso = integer* e *id_discente = integer*
     - routes: 
     - `/solicitacoes_acesso/solicitacao_acesso?id_solicitacao_acesso=value`
     - `/solicitacoes_acesso/solicitacao_acesso?id_discente=value`
     - Response:

      ```json
      
          {
            "id":"integer",
            "para_si":"integer",
            "data":"string format yy-mm-dd",
            "hora_inicio":"string",
            "hora_fim":"string",
            "status_acesso":"integer",
            "nome":"string",
            "fone":"string",
            "matricula": "string",
            "campus_instituto_id_campus_instituto":"integer",
            "usuario_id_usuario": "integer",
            "discente_id_discente":"integer",
            "discente": "string",
            "recurso_campus_id_recurso_campus":"integer",
            "recurso_campus": "string",
            "acesso_permitido": {
                "id_acesso_permitido":"integer",
                "temperatura":"float",
                "hora_entrada":"string",
                "hora_saida":"string",
                "solicitacao_acesso_id_solicitacao_acesso":"integer"
            }
          }
        
      ``` 
   
   - Uso do **POST**: Cria a solicitação de acesso ao campos de acordo com os dados enviados no body da requisição
     - Campos que podem ser enviados no body:
     
     ```json

      {
        "id":"integer",
        "para_si":"integer",
        "data":"string format dd-mm-yy",
        "hora_inicio":"string format hh:mm:ss",
        "hora_fim":"string format hh:mm:ss",
        "status_acesso":"integer",
        "nome":"string",
        "fone":"string",
        "matricula": "string",
        "usuario_id_usuario": "integer",
        "discente_id_discente":"integer",
        "recurso_campus_id_recurso_campus":"integer",
        "acesso_permitido_id_acesso_permitido":"integer",
        "campus_instituto_id_campus_instituto":"integer"
      }

     ``` 

   - Uso do **PUT**: Atualiza os dados da solicitação de acesso ao campus correspondente ao *id_solicitacao_acesso* enviado no body
     - body da requisição:
     ```json
     
      {
          "id_solicitacao_acesso":"*integer",
          "para_si":"integer",
          "data":"string format dd-mm-yy",
          "hora_inicio":"string format hh:mm:ss",
          "hora_fim":"string format hh:mm:ss",
          "status_acesso":"integer",
          "nome":"string",
          "fone":"string",
          "matricula": "string",
          "usuario_id_usuario": "integer",
          "discente_id_discente":"integer",
          "recurso_campus_id_recurso_campus":"integer",
          "acesso_permitido_id_acesso_permitido":"integer",
          "campus_instituto_id_campus_instituto":"integer"
      }
     
     ``` 

   - Uso do **DELETE**: Deleta a solicitação de acesso ao campus correspondente ao *id_solicitacao_acesso* enviado como query string.
     - query string: *id_solicitacao_acesso= integer*
     - route:
       -  `/solicitacoes_acessos/solicitacao_acesso?id_solicitacao_acesso=value`
   

 - `/solicitacoes_acessos`: Use para **ver** os valores na tabela *solicitacao_cesso*. 
   - Método(s) disponíveis: Você pode usar apenas o método **GET** para fazer uma solicitação ao servidor.
   - Use a rota `/solicitacoes_acessos` para buscar as solicitações do campus_instituto do usuario do usuario que requisitou.
   - Use a rota `/solicitacoes_acessos?usuario_id_usuario=integer` para buscar as solicitações filtrando pelo usuario.
   - Use a rota `/solicitacoes_acessos?discente_id_discente` para buscar as solicitações filtrando pelo discente.
   - Use a rota `/solicitacoes_acessos?disciplina_id_disciplina` para buscar as solicitações filtrando por disciplina.
   - Resposta:
  
    ```json
      [
        {
          "id": <*integer>,
          "para_si": <*smallInteger>,
          "data": "yyyy-mm-dd",
          "hora_inicio": "hh:mm:ss",
          "hora_fim": "hh:mm:ss",
          "status_acesso": <*integer>,
          "nome": "string",
          "fone": "string",
          "matricula": "string",
          "usuario_id_usuario": <*integer>,
          "discente_id_discente": <*integer>,
          "discente": "stirng",
          "recurso_campus_id_recurso_campus": <*integer>,
          "recurso_campus": "string",
          "acesso_permitido": {
              "id_acesso_permitido": <*integer>,
              "temperatura": <float>,
              "hora_entrada": "hh:mm:dd",
              "hora_saida": "hh:mm:dd",
              "solicitacao_acesso_id_solicitacao_acesso": <*integer>
          }
        },
        ...
        {
          "id": <*integer>,
          "para_si": <*smallInteger>,
          "data": "yyyy-mm-dd",
          "hora_inicio": "hh:mm:ss",
          "hora_fim": "hh:mm:ss",
          "status_acesso": <*integer>,
          "nome": "string",
          "fone": "string",
          "matricula": "string",
          "usuario_id_usuario": <*integer>,
          "discente_id_discente": <*integer>,
          "discente": "stirng",
          "recurso_campus_id_recurso_campus": <*integer>,
          "recurso_campus": "string",
          "acesso_permitido": {
              "id_acesso_permitido": <*integer>,
              "temperatura": <float>,
              "hora_entrada": "hh:mm:dd",
              "hora_saida": "hh:mm:dd",
              "solicitacao_acesso_id_solicitacao_acesso": <*integer>
          }
        }
      ]
    
    ```
 
 - `/solicitacoes_acessos/disciplina`: ​​Use para **criar** as solicitações de acesso ao campus para cada aluno de uma disciplina específica cujo o id será envido no body da requisição. 
    - Uso do **POST**: Cria as solicitações de acesso à uma disciplina para cada discente desta de acordo com os dados enviados no body da requisição.
     - Campos que podem ser enviados no body:
     
     ```json

      {
          "para_si":<integer>,
          "data":"*yyyy-mm-dd",
          "hora_inicio":"*hh:mm:ss",
          "hora_fim":"*hh:mm:ss",
          "recurso_campus_id_recurso_campus":<*integer>,
          "status_acesso":<*integer>,
          "id_disciplina":<*integer>
      } 

     ``` 


 - `/acessos_permitidos/acesso_permitido`: ​​Use para **ver**, **editar**, **criar**, **excluir** uma um especifico acesso ao campus que foi permitido. 
   - Método(s) disponíveis: **GET**, **POST**, **PUT**, **DELETE** 
   - Uso do **GET**: Obtém os o acesso ao campus permitido correspondente ao *id_acesso_permitido* enviado na query string da requisição
     - Query string: *id_acesso_permitido = <integer>
     - Routes:
       - `/acessos_permitidos/acesso_permitido?id_acesso_permitido=<integer>`
        
     - Resposta:
      
     ```json
     
        {
            "id_acesso_permitido":<*integer>,
            "temperatura":<float>,
            "hora_entrada":"*string format hh:mm:ss",
            "hora_saida":"*string format hh:mm:ss",
            "matricula_discente":"*string",
            "solicitacao_acesso_id_solicitacao_acesso":<integer>,
            "campus_instituto_id_campus_instituto":<integer>
        }
     
     ```

   - Uso do **POST**: Cria o acesso ao campus permitido de acordo com os dados enviados no body requisição.
     - body da requisição:
      
     ```json

        {
            "temperatura":<float>,
            "hora_entrada":"*string format hh:mm:ss",
            "hora_saida":"*string format hh:mm:ss",
            "matricula_discente":"*string",
            "solicitacao_acesso_id_solicitacao_acesso":<integer>,
            "campus_instituto_id_campus_instituto":<*integer>
        }
     
     ``` 

   - Uso do **PUT**: Atualiza o acesso ao campus permitido correspondente ao *id_acesso_permitido* enviado no body  da requisição.
     - body da requisição:
     
     ```json
     
        {
            "id_acesso_permitido":<*integer>,
            "temperatura":<float>,
            "hora_entrada":"*string format hh:mm:ss",
            "hora_saida":"*string format hh:mm:ss",
            "matricula_discente":"*string",
            "solicitacao_acesso_id_solicitacao_acesso":<integer>,
            "campus_instituto_id_campus_instituto":<integer>
        }
     
     ``` 

   - Uso do **DELETE**: Delteta o acesso ao campus permitido correspondente ao *id_acesso_permitido* enviado como query string na requisição.
     - Query string: *id_acesso_permitido = <integer>
     - Routes:
       - `/acessos_permitidos/acesso_permitido?id_acesso_permitido=<integer>`

 - `/acessos_permitidos`: Usado para **ver** os dados de acessos autorizados na tabela *acesso_permitido*. 
   - Metodo(s) disponíveis: Você pode apenas usar o método **GET** para acessar esta rota.
     - Resposta:
     
     ```json
        [
          {
            "id_acesso_permitido": <*integer>,
            "temperatura": <float>,
            "hora_entrada": "string format hh:mm:ss",
            "hora_saida": "hh:mm:ss",
            "matricula_discente":"*string",
            "solicitacao_acesso_id_solicitacao_acesso": <insteger>
          },
          ...
          {
            "id_acesso_permitido": <*integer>,
            "temperatura": <float>,
            "hora_entrada": "string format hh:mm:ss",
            "hora_saida": "hh:mm:ss",
            "matricula_discente":"*string",
            "solicitacao_acesso_id_solicitacao_acesso": <insteger>
          }
        ]
     ``` 


 - `/docentes/docente`: ​​Use para **ver**, **editar**, **criar**, **excluir** os dados de um docente específico do banco. 
   - Método(s) disponíveis: **GET**, **POST**, **PUT**, **DELETE** 
   - Uso do **GET**: Obtém o usuário docente logado no webservice.
     - Resposta:
      
     ```json
        {
          "id_docente": <*integer>,
          "siape": "string",
          "nome": "string",
          "data_nascimento": "string format yyyy-dd-mm",
          "status_covid": <integer>,
          "status_afastamento": <integer>,
          "situacao": "string",
          "sexo":"string",
          "quantidade_pessoas":<integer>,
          "quantidade_vacinas":<integer>,
          "fabricantes":"string",
          "justificativa":"text",
          "carteirinha_vacinacao":"text",
          "usuario_id_usuario": <integer>,
          "usuario": {
            "id_usuario":<*integer>,
            "login":"*string(45)",
            "cpf":"string(15)",
            "email":"*string(45)",
            "tipo":<integer>,
            "campus_instituto_id_campus_instituto":<*integer>
          },
          "curso_id_curso": <*integer>,
          "curso": "string",
          "campus_instituto_id_campus_instituto": <*integer>,
          "campus_instituto": "string"
        }
     
     ``` 

   - Uso do **POST**: Cria um usuário docente de acordo com os dados enviado no body na requisição.
     - Requisição: Campos que podem ser enviados no body.
     
     ```json
        {
          "docente":{
          "siape": "string",
          "nome": "string",
          "data_nascimento": "string format yyyy-dd-mm",
          "status_covid": <integer>,
          "status_afastamento": <integer>,
          "situacao": "string",
          "sexo":"string",
          "quantidade_pessoas":<integer>,
          "quantidade_vacinas":<integer>,
          "fabricantes":"string",
          "justificativa":"text",
          "carteirinha_vacinacao":"text",
          "usuario_id_usuario": <integer>,
          "curso_id_curso": <integer>,
          "campus_id_campus": <integer>
          },
          "usuario": {
            "login":"*string(45)",
            "cpf":"string(15)",
            "email":"*string(45)",
            "tipo":<*integer>,
            "campus_instituto_id_campus_instituto":<*integer>
          }
        }

     ```  

   - Uso do **PUT**: Atualiza um usuário docente corresponente ao *id_docente* enviado no body da requisição junto com os dados que serão atualizados.
     - Body da requisição:
     
     ```json

        {
            "id_docente": <*integer>,
            "siape": "string",
            "nome": "string",
            "data_nascimento": "string format yyyy-dd-mm",
            "status_covid": <integer>,
            "status_afastamento": <integer>,
            "situacao": "string",
            "sexo":"string",
            "quantidade_pessoas":<integer>,
            "quantidade_vacinas":<integer>,
            "fabricantes":<string>,
            "justificativa":"text",
            "carteirinha_vacinacao":"text",
            "usuario_id_usuario": <integer>,
            "curso_id_curso": <integer>,
            "campus_id_campus": <integer>
        }

     ``` 

   - Uso do **DELETE**: Delete o usário docente correspondente ao *id_docente* enviado como query string  na requisição.
     - Query string: *id_docente = integer*
     - Route: 
       - `/docentes/docente?id_docente=<integer>`

 - `/docentes`: Use para **ver** os técnicos cadastrados na base de dados, na tabela _docente_. 
   - Método(s) disponíveis: Você pode apenas usar o método **GET** para acessar esta rota.
     - Resposta:
     
     ```json
        [
          {
            "nome": "*string",
            "id": <*unteger>,
            "siape": "*string"
          },
          {
            "nome": "*string",
            "id": <*unteger>,
            "siape": "*string"
          },
          ...
          {
            "nome": "*string",
            "id": <*unteger>,
            "siape": "*string"
          }
        ]
     ```

 - `/tecnicos/tecnico`: ​​Use para **ver**, **editar**, **criar**, **excluir** um técnico específico do campus. 
   - Método(s) disponíveis: **GET**, **POST**, **PUT**, **DELETE** 
   - Uso do **GET**: Obtém o usuário técnico logado no webservice.
     - Resposta:
     ```json
     {
      "id_tecnico":<*integer>,
      "siape":"string", 
      "nome":"string", 
      "data_nascimento":"string format yyyy-dd-mm", 
      "cargo":"string",
      "status_covid":<integer>, 
      "status_afastamento":<integer>,
      "sexo":"string",
      "quantidade_pessoas":<integer>,
      "quantidade_vacinas":<integer>,
      "fabricantes":"string",
      "justificativa":"text",
      "carteirinha_vacinacao":"text", 
      "usuario_id_usuario":<*integer>,
      "usuario": {
          "id_usuario":<*integer>,
          "login":"*string",
          "cpf":"string",
          "email":"*string",
          "tipo":<*integer>,
          "campus_instituto_id_campus_instituto":<*integer>
      },
      "campus_instituto_id_campus_instituto":<*integer>,
      "campus_instituto": "string"
      }
     
     ``` 

   - Uso do **POST**: Cria um usuário técnico de acordo com os dados enviado no body na requisição.
     - Requisição: Campos que podem ser enviados no body.
     
     ```json
      {
        "tecnico":{
        "siape":"string", 
        "nome":"string", 
        "data_nascimento":"string format yyyy-dd-mm", 
        "cargo":"string",
        "status_covid":<integer>, 
        "status_afastamento":<integer>,
        "sexo":"string",
        "quantidade_pessoas":<integer>,
        "quantidade_vacinas":<integer>,
        "fabricantes":"string",
        "justificativa":"text",
        "carteirinha_vacinacao":"text", 
        "usuario_id_usuario":<integer>,
        "campus_instituto_id_campus_instituto":<*integer>
        },
        "usuario": {
            "login":"*string",
            "cpf":"string",
            "email":"*string",
            "tipo":<*integer>,
            "campus_instituto_id_campus_instituto":<*integer>
        }
      }

     ```  

   - Uso do **PUT**: Atualiza um usuário técnico corresponente ao *id_tecnico* enviado no body da requisição junto com os dados que serão atualizados.
     - Body da requisição:
     
     ```json
      {
        "id_tecnico":<*integer>,
        "siape":"string", 
        "nome":"string", 
        "data_nascimento":"string format yyyy-dd-mm", 
        "cargo":"string",
        "status_covid":"integer", 
        "status_afastamento":"integer",
        "sexo":"string(2)",
        "quantidade_pessoas":"integer",
        "quantidade_vacinas":"integer",
        "fabricantes":"string(45)",
        "justificativa":"text",
        "carteirinha_vacinacao":"bytes", 
        "usuario_id_usuario":"integer",
        "campus_instituto_id_campus_instituto":"integer",
      }

     ``` 

   - Uso do **DELETE**: Delete o usário técnico correspondente ao *id_tecnico* enviado como query string  na requisição.
     - Query string: *id_tecnico = <integer>
     - Route: 
       - `/tecnicos/tecnico?id_tecnico=<integer>`



 - `/tecnicos`: Use para **ver** os técnicos cadastrados na base de dados, na _tecnico_. 
   - Método(s) disponíveis: Você pode apenas usar o método **GET** para acessar esta rota.
   - Resposta:
   
   ```json
      [
        {
          "nome": "*string",
          "id": <*integer>,
          "siape": "*string"
        },
        {
          "nome": "*string",
          "id": <*integer>,
          "siape": "*string"
        },
        ...
        {
          "nome": "*string",
          "id": <*integer>,
          "siape": "*string"
        },
        {
          "nome": "*string",
          "id": <*integer>,
          "siape": "*string"
        }
      ]
  
   ```


 - `/pontos_verificacao/ponto_verificacao`: ​​Use para **ver**, **editar**, **criar**, **excluir** um técnico específico do campus. 
   - Método(s) disponíveis: **GET**, **POST**, **PUT**, **DELETE** 
   - Uso do **GET**: Obtém o usuário ponto_verificacao logado no webservice.
     - Resposta:
     
     ```json
     {
   
        "id_ponto_verificacao":<*integer>,
        "nome":"string",
        "descricao":"Text",
        "campus_instituto_id_campus_instituto":<integer>,
        "campus_instituto":"string",
        "usuario_id_usuario":<integer>,
        "usuario": {
            "id_usuario":<integer>,
            "login":"*string(45)",
            "cpf":"string(15)",
            "email":"*string(45)",
            "tipo":<*integer>,
            "campus_instituto_id_campus_instituto":<*integer>
        }
     }
     
     ``` 

   - Uso do **POST**: Cria um usuário ponto_verificacao de acordo com os dados enviado no body na requisição.
     - Requisição: Campos que podem ser enviados no body.
     
     ```json
      {
        "ponto_verificacao":{
            "nome":"string",
            "descricao":"Text",
            "campus_instituto_id_campus_instituto":<integer>,
            "usuario_id_usuario":<*integer>,
        "usuario": {
            "login":"*string",
            "cpf":"string",
            "email":"*string",
            "tipo":<*integer>,
            "campus_instituto_id_campus_instituto":<*integer>
          }
      }

     ```  

   - Uso do **PUT**: Atualiza um usuário ponto_verificacao corresponente ao *id_ponto_verificacao* enviado no body da requisição junto com os dados que serão atualizados.
     - Body da requisição:
     
     ```json
      {
        "id_ponto_verificacao":<*integer>,
        "nome":"*string",
        "descricao":"Text",
        "campus_instituto_id_campus_instituto":<*integer>,
        "usuario_id_usuario":<*integer>,
      }

     ``` 

   - Uso do **DELETE**: Delete o usário ponto_varificacao correspondente ao *id_ponto_verificacao* enviado como query string  na requisição.
     - Query string: *id_ponto_verificacao = <integer>
     - Route: 
       - `/pontos_verificacao/ponto_verificacao?id_ponto_verificacao=<integer>`


 - `/pontos_verificacao`: Use para **ver** os técnicos cadastrados na base de dados, na *pontos_verificacao*. 
   - Método(s) disponíveis: Você pode apenas usar o método **GET** para acessar esta rota.
   - Resposta:
   
   ```json
      [
        {
          "nome": "string",
          "id": <*integer>
          
        },
        ,
        ...
        {
          "nome": "string",
          "id": <*integer>
        }
      ]
  
   ```


 - `/recursos_campus/recurso_campus`: ​​Use para **ver**, **editar**, **criar**, **excluir** um recurso específico do campus. 
   - Método(s) disponíveis: **GET**, **POST**, **PUT**, **DELETE** 
   - Uso do **GET**: Obtém os dados do recurso do campi correspondente ao *id_recurso_campus* enviado como query string na requisição.
     - Query string: *id_recurso_campus = integer*
     - Route:
       - `/recurso_campus/recurso_campus?id_recurso_campus=value`
     - Resposta:
      
     ```json

        {
          "id_recuso_campus": <*integer>, 
          "nome": "string",
          "capacidade": <integer>,
          "descricao": "string",
          "tipo_restricao": <smallInteger>, (0=livre, 1=restricão parcial; 2=restricão total)
          "usuario_id_usuario":<integer>,
          "inicio_horario_funcionamento": "string format hh:mm:ss",
          "fim_horario_funcionamento": "string format hh:mm:ss",
          "quantidade_horas": <integer>,
          "campus_instituto_id_campus_instituto": <integer>,
          "campus_instituto": "string"
        }
     
     ``` 

   - Uso do **POST**: Cria um recurso do campi de acordo com os dados enviado no body da requisição.
     - Requisição: Campos que podem ser enviados no body.
    
      ```json

          {
            "nome": "string",
            "capacidade": <integer>,
            "descricao": "string",
            "tipo_restricao": <smallInteger> (0=livre, 1=restricão parcial; 2=restricão total)
            "usuario_id_usuario": <integer>
            "inicio_horario_funcionamento": "string format hh:mm:ss",
            "fim_horario_funcionamento": "string format hh:mm:ss",
            "quantidade_horas": <integer>,
            "campus_instituto_id_campus_instituto": <integer>,
            "campus_instituto": "string"
          }
      
      ``` 

   - Uso do **PUT**: Atualiza um recurso do campi correspondente ao *id_recurso_campus* enviado no body da requisição com os novos dados.
     - Body da requisição:
     
        ```json

          {
            "id_recuso_campus": <*integer>, 
            "nome": "string",
            "capacidade": <integer>,
            "descricao": "string",
            "tipo_restricao": <smallInteger> (0=livre, 1=restricão parcial; 2=restricão total)
            "usuario_id_usuario": <integer>
            "inicio_horario_funcionamento": "string format hh:mm:ss",
            "fim_horario_funcionamento": "string format hh:mm:ss",
            "quantidade_horas": <integer>,
            "campus_instituto_id_campus_instituto": <integer>,
            "campus_instituto": "string"
          }
      
        ``` 

   - Uso do **DELETE**: Deleta um recurso do campi de acordo com o *id_recurso_campus* enviado como query string na requisição.
     - Query string: *id_recurso_campus = integer*.
     - Route: 
       - `/recurso_campus/recurso_campus?id_recurso_campus=value` 
    
 - `/recursos_campus`: Use para **ver** os valores na tabela _recurso_campus_ gravada no banco de dados. 
   - Método(s): Você pode apenas usar o método **GET** para acessar esta rota.
   - Rotas 
     - `/recursos_campus`, para buscar todos
     - `/recursos_campus?usuario_id_usuario=<integer>`, para buscar os recurso criado por um usuario especifico.
     - `/recursos_campus?campus_instituto_id_campus_instituto=<integer>`para buscar os recurso de um campus ou instituto especifico.
   - Resposta:

   ```json
      [
        {
          "nome": "Laboratório de ensino em Biologia",
          "id": 1,
          "usuario_id_usuario":null,
          "inicio_horario": "08:00:00",
          "fim_hoario": "08:00:00"
        },
        {
          "nome": "Laboratório multidisciplinar de biologia II",
          "id": 2,
          "usuario_id_usuario":null,
          "inicio_horario": "08:00:00",
          "fim_hoario": "08:00:00"
        },
        ...
        {
          "nome": "Laboratório de Informática",
          "id": 3,
          "usuario_id_usuario":null,
          "inicio_horario": "08:00:00",
          "fim_hoario": "08:00:00"
        },
        {
          "nome": "Sala de Aula Inteligente I",
          "id": 4,
          "usuario_id_usuario":null,
          "inicio_horario": "08:00:00",
          "fim_hoario": "08:00:00"
        }
      ]

   ``` 
   
 - `/cursos/curso`: ​​Use para **ver**, **editar**, **criar**, **excluir** os dado de um curso específico. 
   - Método(s) disponíveis: **GET**, **POST**, **PUT**, **DELETE** 
   - Uso do **GET**: Obtém os dados do curso correspondente ao *id_curso* enviado como query string na requisição.
     - Query string: *id_curso = integer*
     - Route:
       - `/cursos/curso?id_curso=value`
        
     - Resposta:
      
     ```json

        {
          "id_curso": "integer",
          "nome": "string(45)",
          "data_fundacao": "string format yy-mm-dd",
          "campus_instituto": "string",
          "unidade":"string(45)",
          "cidade":"string(45)",
          "grau_academico":"string(45)",
          "situacao":"string(45)",
          "modalidade":"string(45)",
          "convenio":"string(45)",
          "ativo":"Boolean(0-não ou 1-sim)"
        }
     
     ``` 

   - Uso do **POST**: Cria um curso de acordo com os dados enviado no body da requisição.
     - Requisição: Campos que podem ser enviados no body.
    
      ```json

        {
          "nome": "string(45)",
          "data_fundacao": "string format dd-mm-yy",
          "campus_instituto_id_campus_instituto": "integer",
          "unidade":"string(45)",
          "cidade":"string(45)",
          "grau_academico":"string(45)",
          "situacao":"string(45)",
          "modalidade":"string(45)",
          "convenio":"string(45)",
          "ativo":"Boolean(0-não ou 1-sim)"
        }
      
      ``` 

   - Uso do **PUT**: Atualiza um curso correspondente ao *id_curso* enviado no body da requisição com os novos dados.
     - Body da requisição:
     
        ```json

          {
            "id_curso": "*integer",
            "nome": "string(45)",
            "data_fundacao": "string format dd-mm-yy",
            "campus_instituto_id_campus_instituto": "integer",
            "unidade":"string(45)",
            "cidade":"string(45)",
            "grau_academico":"string(45)",
            "situacao":"string(45)",
            "modalidade":"string(45)",
            "convenio":"string(45)",
            "ativo":"Boolean(0-não ou 1-sim)"
          }
      
        ``` 

   - Uso do **DELETE**: Deleta um curso de acordo com o *id_curso* enviado como query string na requisição.
     - Query string: *id_curso = integer*.
     - Route: 
       - `/cursos/curso?id_curso=value`  
       
 - `/cursos`: Use para **ver** os curso cadastrado no banco de dados, na tabela *curso*. 
   - Método(s): Apenas método **GET** está disponível para acessar a rota.
   - Resposta:
   
   ```json
   
    [
      {
        "nome": "SISTEMAS DE INFORMAÃÃO",
        "id": 1
      },
      ...
      {
        "nome": "CIÃNCIAS BIOLÃGICAS",
        "id": 2
      }
    ]
   
   ``` 

 - `/campus_institutos/campus_instituto`: ​​Use para **ver**, **editar**, **criar**, **excluir** os dados de um campus específico. 
   - Método(s) disponíveis: **GET**, **POST**, **PUT**, **DELETE** 
   - Uso do **GET**: Obtém os dados do campus correspondente ao *id_campus* enviado como query string na requisição.
     - Query string: *id_campus = integer*
     - Route:
       - `/campus/campi?id_campus=value`
        
     - Resposta:
      
     ```json

        {
          "id_campus":<*integer>,
          "nome":"string(45)",
          "abertura_total":"boolean(1-sim ou 0-não)",
          "ano_fundacao":"string format yy-mm-dd",
          "direcao_id_direcao": <*integer>,
          "direcao": "string(45)" 
        }
     
     ``` 

   - Uso do **POST**: Cria um campus de acordo com os dados enviado no body da requisição.
     - Requisição: Campos que podem ser enviados no body.
    
      ```json

        {
          "nome":"string(45)",
          "ano_fundacao":"string format dd-mm-yy",
          "abertura_total":"boolean(1-sim ou 0-não)",
          "direcao_id_direcao": <integer>,
        }
      
      ``` 

   - Uso do **PUT**: Atualiza um campus correspondente ao *id_campus* enviado no body da requisição com os novos dados.
     - Body da requisição:
     
        ```json

          {
            "id_campus":<*integer>,
            "nome":"string",
            "abertura_total":"boolean(1 ou 0)",
            "ano_fundacao":"string format dd-mm-yy",
            "direcao_id_direcao": <integer>
          }
      
        ``` 

   - Uso do **DELETE**: Deleta um campus de acordo com o *id_campus* enviado como query string na requisição.
     - Query string: *id_campus = integer*.
     - Route: 
       - `/campus/campi?id_campus=value`   
    
 - `/campus_institutos`: Use para **ver** os campus cadastrados no banco de dados, na tabela *campus*. 
   - Método(s): Apenas método **GET** está disponível para acessar a rota.
   - Resposta:

   ```json
    [
      {
        "nome": <*string>,
        "id": <*inteiro>
      },
      {
        "nome": <*string>,
        "id": <*inteiro>
      },
      {
        "nome": <*string>,
        "id": <*inteiro>
      }
    ]
   
   ``` 


- `/discente_vacinacao`: ​​Use para **ver**, *editar** os dados de um discente específico. 
   - Método(s) disponíveis: **GET**, **POST**, **PUT**, **DELETE** 
   - Uso do **GET**: Obtém os dados de vacinação do discente correspondente a query string *discente_matricula* enviado como query string na requisição.
     - Query string: *discente_matricula = string*
     - Route:
       - `/discente_vacinacao?discente_matricula=value`
        
     - Resposta:
      
     ```json

        {
          "id_discente":<*integer>,
          "nome":"string",
          "fabricante":"string",
          "status_covid":"boolean(1 ou 0)",
          "quantidade_vacinas":<integer>
        }
     
     ``` 

   - Uso do **PUT**: Edita os dados de vacinação do discente de acordo com os dados enviado no body da requisição (O *id_discente* do discente deve ser especificado no body).
     - Requisição: Campos que podem ser enviados no body.
    
      ```json

        {
          "id_discente":"*integer",
          "nome":"string(45)",
          "fabricante":"string(45)",
          "status_covid":"boolean(1 ou 0)",
          "quantidade_vacinas":"integer"
        }
      
      ``` 

- `/discentes_vacinacoes` : Use para **ver** os dados de vacinação dos discentes.
  - Método: Apenas o método **GET** está disponpivel para acesso nesta rota.
  - Rotas de acesso com query string
    - `/discentes_vacinacoes?curso_id_curso=<inteiro>&numero_de_doses=<inteiro>&ano_turma=<inteiro>`
    - `/discentes_vacinacoes?curso_id_curso=<inteiro>&ano_turma=<inteiro>`
    - `/discentes_vacinacoes?curso_id_curso=<inteiro>&numero_de_doses=<inteiro>`
    - `/discentes_vacinacoes?numero_de_doses=<inteiro>&ano_turma=<inteiro>`
    - `/discentes_vacinacoes?curso_id_curso=<inteiro>`
    - `/discentes_vacinacoes?ano_turma=<inteiro>`
    - `/discentes_vacinacoes?numero_de_doses=<inteiro>`
  - Resposta:

    ```json

      [
          {
              "nome": <*string>,
              "id": <*inteiro>,
              "matricula": <*string>,
              "turma": <*inteiro>,
              "carteirinha_vacinacao": <string>
          },
          {
              "nome": <*string>,
              "id": <*inteiro>,
              "matricula": <*string>,
              "turma": <*inteiro>,
              "carteirinha_vacinacao": <string>
          },
          {
              "nome": <*string>,
              "id": <*inteiro>,
              "matricula": <*string>,
              "turma": <*inteiro>,
              "carteirinha_vacinacao": <string>
          }
    ]

    ```

- `/disciplinas/disciplina`: ​​Use para **ver**, **editar**, **criar**, **excluir** os dado de um curso específico. 
   - Método(s) disponíveis: **GET**, **POST**, **PUT**, **DELETE** 
   - Uso do **GET**: Obtém os dados da disciplina correspondente ao *id_disciplina* enviado como query string na requisição.
     - Query string: *id_disciplina = integer*
     - Route:
       - `/disciplinas/disciplina?id_disciplina=value`
        
     - Resposta:
      
     ```json

        {
            "id_disciplina":<*integer>,
            "nome":"*string",
            "codigo_sigaa":"*string",
            "docente_id_docente":"*string",
            "semestre":<integer>,
            "curso_id_curso":<*integer>
        }
     
     ``` 

   - Uso do **POST**: Cria uma disciplina de acordo com os dados enviado no body da requisição.
     - Requisição: Campos que podem ser enviados no body.
    
      ```json

        {
            "nome":"*string",
            "codigo_sigaa":"*string",
            "semestre":<integer>,
            "docente_id_docente":"*string",
            "curso_id_curso":<*integer>
        }
      
      ``` 

   - Uso do **PUT**: Atualiza uma disciplina correspondente ao *id_disciplina* enviado no body da requisição com os novos dados.
     - Body da requisição:
     
        ```json

          {
            "id_disciplina":<*integer>,
            "nome":"string",
            "codigo_sigaa":"string",
            "docente_id_docente":"*string",
            "semestre":<integer>,
            "curso_id_curso":<integer>
        }
      
        ``` 

   - Uso do **DELETE**: Deleta uma disciplina de acordo com o *id_disciplina* enviado como query string na requisição.
     - Query string: *id_disciplina = integer*.
     - Route: 
       - `/disciplinas/disciplina?id_disciplina=3`  
       
 - `/disciplinas`: Use para **ver** as disciplinas cadastradas no banco de dados, na tabela *disciplina*. 
   - Método(s): Apenas método **GET** está disponível para acessar a rota.
   - Use a rota `/solicitacoes_acessos?docente_id_docente` para buscar todas as solicitações
   - Use a rota `/solicitacoes_acessos?docente_id_docente` para buscar as solicitações filtrando por docente.
   - Resposta:
   
   ```json
   
    [
      {
        "nome": "string",
        "id": <integer>,
        "semestre": <integer>,
        "codigo_sigaa":"string"
      },
      ...
      {
        "nome": "string",
        "id": <integer>,
        "semestre": <integer>,
        "codigo_sigaa":"string"
      }
    ]
   
   ``` 
- `/notificacoes_covid/notificacao_covid`: ​​Use para **ver**, **editar**, **criar**, **excluir** os dado de uma notificacao específico. 
   - Método(s) disponíveis: **GET**, **POST**, **PUT**, **DELETE** 
   - Uso do **GET**: Obtém os dados da notificacão correspondente ao *id_notificacao_covid* enviado como query string na requisição.
     - Query string: *id_notificacao_covid = integer*
     - Route:
       - `/notificacoes_covid/notificacao_covid?id_notificacao_covid=<INTEIRO>`
        
     - Resposta:
      
     ```json

      {
        "id_notificacao_covid": <integer>,
        "data": "yyyy-mm-dd",
        "data_diagnostico": "yyyy-mm-dd",
        "teste": "string",
        "nivel_sintomas": "string",
        "matricula_discente": "*string",
        "observacoes": "string",
        "campus_instituto_id_campus_instituto": <*integer>
      }   
     
     ``` 

   - Uso do **POST**: Cria uma notificação de acordo com os dados enviado no body da requisição.
     - Requisição: Campos que podem ser enviados no body.
    
      ```json

      {
        "data": "yyyy-mm-dd",
        "data_diagnostico": "yyyy-mm-dd",
        "teste": "string",
        "nivel_sintomas": "string",
        "observacoes": "string",
        "matricula_discente": "*string",
        "campus_instituto_id_campus_instituto": <*integer>
      }
      
      ``` 

   - Uso do **PUT**: Atualiza uma notificacao correspondente ao *id_notificacao_covid* enviado no body da requisição com os novos dados.
     - Body da requisição:
     
        ```json

        {
          "id_notificacao_covid": <*integer>,
          "data": "yyyy-mm-dd",
          "data_diagnostico": "yyyy-mm-dd",
          "teste": "string",
          "nivel_sintomas": "string",
          "observacoes": "string",
          "matricula_discente": "*string",
          "campus_instituto_id_campus_instituto": <*integer>
        }
      
        ``` 

   - Uso do **DELETE**: Deleta uma notificação de acordo com o *id_notificacao_covid* enviado como query string na requisição.
     - Query string: *id_notificacao_covid = <INTEIRO>*.
     - Route: 
       - `/notificacoes_covid/notificacao_covid?id_notificacao_covid=133`  
  
- `/notificacoes_covid`: Use para **ver** as notificações de covid cadastradas no banco de dados, na tabela *notificacao_covid*.  
  - Método(s): Apenas método **GET** está disponível para acessar a rota.
  - Resposta:
   
   ```json
   
  [
    
    {
        "id_notificacao_covid": <*integer>,
        "data": "*string",
        "data_diagnosico": "string",
        "teste": "string",
        "nivel_sintomas": "*string",
        "observacoes":"string",
        "matricula_discente": "*string",
        "campus_instituto_id_campus_instituto": <integer>
    },
    {
        "id_notificacao_covid": <*integer>,
        "data": "*string",
        "data_diagnosico": "string",
        "teste": "string",
        "nivel_sintomas": "*string",
        "matricula_discente": "*string",
        "campus_instituto_id_campus_instituto": <integer>
    },
    ...,
    {
        "id_notificacao_covid": <*integer>,
        "data": "*string",
        "data_diagnosico": "string",
        "teste": "string",
        "nivel_sintomas": "*string",
        "matricula_discente": "*string",
        "campus_instituto_id_campus_instituto": <integer>
    },
   
   ```

- `/portarias/portaria`: ​​Use para **ver**, **editar**, **criar**, **excluir** os dados de um usuário portaria específico do banco. 
   - Método(s) disponíveis: **GET**, **POST**, **PUT**, **DELETE** 
   - Uso do **GET**: Obtém o usuário portaria logado no webservice.
     - Resposta:
      
     ```json
        {
          "id_portaria": <*integer>,
          "nome": "*string",
          "data_nascimento": "string format yy-mm-dd",
          "funcao":"string",
          "turno_trabalho":"string",
          "usuario_id_usuario": <*integer>,
          "campus_instituto_id_campus_instituto": <*integer>,
          "usuario": {
            "id_usuario":<*integer>,
            "login":"*string",
            "cpf":"string",
            "email":"*string",
            "tipo":<*integer>,
            "campus_instituto_id_campus_instituto":<*integer>
          },
          
        }
     
     ``` 

   - Uso do **POST**: Cria um usuário portaria de acordo com os dados enviado no body na requisição.
     - Requisição: Campos que podem ser enviados no body.
     
     ```json
        {
          "portaria":{
            "nome": "*string",
            "data_nascimento": "string format yy-mm-dd",
            "funcao":"string",
            "turno_trabalho":"string",
            "usuario_id_usuario": <*integer>,
            "campus_instituto_id_campus_instituto": <*integer>
          },
          "usuario": {
            "id_usuario":<*integer>,
            "login":"*string",
            "cpf":"string",
            "email":"*string",
            "tipo":<*integer>,
            "campus_instituto_id_campus_instituto":<*integer>
          },
        }

     ```  

   - Uso do **PUT**: Atualiza um usuário portaria corresponente ao *id_portaria* enviado no body da requisição junto com os dados que serão atualizados.
     - Body da requisição:
     
     ```json

        {   
          "id_portaria":<*integer>,
          "nome": "*string",
          "data_nascimento": "string format YYYY-mm-dd",
          "funcao":"string",
          "turno_trabalho":"string",
          "usuario_id_usuario": <*integer>,
          "campus_instituto_id_campus_instituto": <*integer>
        }

     ``` 

   - Uso do **DELETE**: Delete o usário portaria correspondente ao *id_portaria* enviado como query string  na requisição.
     - Query string: *id_portaria = <integer>
     - Route: 
       - `/portarias/portaria?id_portaria=<integer>`

 - `/portarias`: Use para **ver** os porteiros cadastrados na base de dados, na tabela _portaria_. 
   - Método(s) disponíveis: Você pode apenas usar o método **GET** para acessar esta rota.
     - Resposta:
     
     ```json
        [
          {
          "nome": "*string",
          "id": <*insteger>,
          },
          {
          "nome": "*string",
          "id": 2,
          },
          ...
          {
          "nome": "*string",
          "id": 6,
          }
        ]
     ```

### Para tela de Estatísticas

- `/discentes/quantidade_vacinados_por_curso` : Para **Ver**, a quantidade de alunos vacinados por curso e a quantidade total de alunos por curso. 
   - Metodo disponíveis: **GET**.
   - rota completa:
     - `/discentes/quantidade_vacinados_por_curso?id_campus_intituto=<INTEIRO>`
   - Resposta:
  ```json
  
  {
    "total_vacinados": {
        "SISTEMAS DE INFORMAÇÃO": 33,
        "CIÊNCIAS BIOLÓGICAS": 82,
        "INTERDISCIPLINAR EM CIÊNCIAS BIOLÓGICAS E CONSERVAÇÃO": 1
    },
    "total_alunos": {
        "SISTEMAS DE INFORMAÇÃO": 34,
        "CIÊNCIAS BIOLÓGICAS": 84,
        "INTERDISCIPLINAR EM CIÊNCIAS BIOLÓGICAS E CONSERVAÇÃO": 1
    }
  }
  ```

- `/solicitacoes_acessos/quantidade_por_campus` : Para **Ver**, a quantidade de agendamentos solicidados à universidade por campus e intitutos pelos últimos 6 meses. 
   - Metodo disponíveis: **GET**.
   - rota completa:
     - `/solicitacoes_acessos/quantidade_por_campus`
   - Resposta:
  ```json
  
  {
    "CAMPUS UNIVERSITÁRIO DE ORIXIMINÁ-PROF.DR. DOMINGOS DINIZ": 214
  }  

  ```

- `/solicitacoes_acessos/quantidade_por_curso` : Para **Ver**, a quantidade de agendamentos solicitados por curso da universidade de acordo com o mês requisitado na query string(1, para Janeiro; 2, para Fevereiro;...;12, para Dezembro) e o ano(2020, 2021,...). 
   - Metodo disponíveis: **GET**.
   - rota completa:
     - `/solicitacoes_acessos/quantidade_por_curso?id_campus_instituto=5&ano=2021&mes=11`
   - Resposta:
  ```json
  
  {
    "CIÊNCIAS BIOLÓGICAS": 48,
    "SISTEMAS DE INFORMAÇÃO": 15
  }  

  ```

- `/solicitacoes_acessos/quantidade_por_recurso_campus` : Para **Ver**, a quantidade de agendamentos solicitados por recurso do campus da universidade de acordo com o mês requisitado na query string(1, para Janeiro; 2, para Fevereiro;...;12, para Dezembro) e o ano(2020, 2021,...). 
   - Metodo disponíveis: **GET**.
   - rota completa:
     - `/solicitacoes_acessos/quantidade_por_recurso_campus?id_campus_instituto=5&ano=2021&mes=11`
   - Resposta:
  ```json
  
  {
    "Laboratório de Informática": 10,
    "Sala de Aula Inteligente I": 2,
    "Sala de Aula Inteligente II": 13,
    "Area Comum de Convivência": 5,
    "Auditorio": 30,
    "Sala de Aula Inteligente III": 1,
    "Laboratório Mult. de Biologia III": 2
  }

  ```

- `/notificacoes_covid/quantidade_por_campus` : Para **Ver**, a quantidade de notificações de covid efetuadas pelos alunos de acordo com o campus(id_campus_intituto) e o ano(2021, 2021,...). 
   - Metodo disponíveis: **GET**.
   - rota completa:
     - `/notificacoes_covid/quantidade_por_campus?id_campus_instituto=5&ano=2021`
   - Resposta:
  ```json
  
  {
    "JAN": 3,
    "FEV": 4,
    "MAR": 2,
    "ABR": 2,
    "MAI": 1,
    "JUN": 1,
    "JUL": 1,
    "AGO": 0,
    "SET": 0,
    "OUT": 0,
    "NOV": 1,
    "DEZ": 9
  }  

  ```

- `/notificacoes_covid/quantidade_por_curso` : Para **Ver**, a quantidade de notificações de covid efetuadas pelos alunos por curso e de acordo com campus_insituto(id_campus_instituto) e o ano(2021, 2021,...). 
   - Metodo disponíveis: **GET**.
   - rota completa:
     - `/quantidade_por_curso?id_campus_instituto=5&ano=2021`
   - Resposta:
  ```json
  
  {
    "SISTEMAS DE INFORMAÇÃO": 10,
    "CIÊNCIAS BIOLÓGICAS": 14
  }  

  ```
## Documentações

A documentação do Webservice PAEM estará aqui no futuro.

## Licença

Copyright 2021 UFOPA-Projeto PAEM.

Licensed to the Apache Software Foundation (ASF) under one or more contributor license agreements. See the NOTICE file distributed with this work for additional information regarding copyright ownership. The ASF licenses this file to you under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.