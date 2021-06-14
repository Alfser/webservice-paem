# Create a default database or recreate if it exist
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from mysql import connector
import json
import os


app = Flask(__name__)


if os.path.isfile('app/database/connection.json'):

    with open('app/database/connection.json', 'r') as file:
        __conn_json = json.load(file)


    __username = __conn_json["username"]
    __password = __conn_json["password"]
    __server = __conn_json["server"]
    __database = __conn_json["database"]

else:
    
    __username = os.environ["USER_NAME"]
    print(__username)
    __password = os.environ["PASSWORD"]
    print(__password)
    __server = os.environ["HOST_NAME"]
    print(__server)
    __database = os.environ["DATABASE_NAME"]
    print(__database)
    
# get AQLAlchemy
db = SQLAlchemy(app=app)

__str_connection = "mysql://{username}:{password}@{server}/{database}?charset=utf8"


app.config['SQLALCHEMY_DATABASE_URI'] = __str_connection.format(
                                                    username=__username, 
                                                    password=__password, 
                                                    server=__server, 
                                                    database=__database
                                                )

app.config['SECRET_KEY'] = 'secrect_key'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def create_db():
    
    mydb = connector.connect(
        host=__server,
        user=__username,
        password=__password
    )
    mycursor = mydb.cursor()

    mycursor.execute(f"DROP DATABASE IF EXISTS {__database}")
    mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {__database} CHARSET = utf8mb4;")
    # mycursor.execute(f"USE {db_name}")
    mydb.close()
    mycursor.close()
    
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.create_all()
    
