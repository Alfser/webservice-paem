import json
import os
import sys
from configparser import ConfigParser
import logging

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

if not (username and server and password and database):
    print("Erro: Não pode haver credênciais nulas.")
    sys.exit()

class Config:
    USERNAME = username
    HOSTNAME = server
    DATABASE = database
    SECRET_KEY = secret_key
    PASSWORD = password

class OAuth2Credentials:
    _filename = 'credentials.api.ini'
    _section = 'ctic-api'

    @classmethod
    def get_api_credentials(cls):
        
        parser = ConfigParser()

        try:
            parser.read(filenames=cls._filename)
        except:
            logging.error('Erro durante a leitura do arquivo .ini com as configurações do banco.')

        if not parser.has_section(cls._section):
             raise ValueError(f"A sessão {cls._section} não existe no arquivo {cls._filename}.")
        
        api_credentials = dict(parser.items(cls._section))
        return api_credentials
