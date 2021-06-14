# Create a default database or recreate if it exist
import sys
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from mysql import connector
import json
import os


app = Flask(__name__)


if os.path.isfile('../connection.json'):
    with open('../connection.json', 'r') as file:
        try:
            __conn_json = json.load(file)

        except json.decoder.JSONDecodeError as msg:
            print("Erro ao decodificar o arquivo json.", msg)

    __username = __conn_json.get("username")
    __password = __conn_json.get("password")
    __server = __conn_json.get("server")
    __database = __conn_json.get("database")

elif os.path.isfile('app/database/connection.json'):
    with open('app/database/connection.json') as file:    
        try:
            __conn_json = json.load(file)

        except json.decoder.JSONDecodeError as msg:
                print("Erro ao decodificar o arquivo json.", msg)

    __username = __conn_json.get("username")
    __password = __conn_json.get("password")
    __server = __conn_json.get("server")
    __database = __conn_json.get("database")

else:
    
    __username = os.environ.get("USER_NAME")
    print(__username)
    __password = os.environ.get("PASSWORD")
    print(__password)
    __server = os.environ.get("HOST_NAME")
    print(__server)
    __database = os.environ.get("DATABASE_NAME")
    print(__database)

# get AQLAlchemy
db = SQLAlchemy(app=app)

__str_connection = "mysql://{username}:{password}@{server}/{database}?charset=utf8"

if not (__username or __server or __password or __database):
    print("Erro: Não pode haver credênciais nulas.")
    sys.exit()

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
    
