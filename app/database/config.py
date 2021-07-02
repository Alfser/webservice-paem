import json
import os
import sys

if os.path.isfile('/etc/config.json'):
    with open('/etc/config.json') as file:
        try:
            __conn_json = json.load(file)

        except json.decoder.JSONDecodeError as msg:
            print("Erro ao decodificar o arquivo json.", msg)

    username = __conn_json.get("USERNAME")
    password = __conn_json.get("PASSWORD")
    server = __conn_json.get("HOSTNAME")
    database = __conn_json.get("DATABASE")
    secret_key= __conn_json.get("SECRET_KEY")

elif os.path.isfile('app/database/connection.json'):
    with open('app/database/connection.json') as file:    
        try:
            __conn_json = json.load(file)

        except json.decoder.JSONDecodeError as msg:
                print("Erro ao decodificar o arquivo json.", msg)

    username = __conn_json.get("USERNAME")
    password = __conn_json.get("PASSWORD")
    server = __conn_json.get("HOSTNAME")
    database = __conn_json.get("DATABASE")
    secret_key= __conn_json.get("SECRET_KEY")
else:
    
    username = os.environ.get("USERNAME")
    print(username)
    password = os.environ.get("PASSWORD")
    print(password)
    server = os.environ.get("HOSTNAME")
    print(server)
    database = os.environ.get("DATABASE")
    print(database)
    secret_key = os.environ.get("SECRET_KEY")

if not (username and server and database):
    print("Erro: Não pode haver credênciais nulas.")
    sys.exit()

class Config:
    USERNAME = username
    HOSTNAME = server
    DATABASE = database
    SECRET_KEY = secret_key
    PASSWORD = password
