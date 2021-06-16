# Create a default database or recreate if it exist
import sys
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, config
from mysql import connector
from .config import Config
import json
import os


app = Flask(__name__)



# SQLAlchemy config
# app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
__str_connection = "mysql://{username}:{password}@{server}/{database}?charset=utf8"

app.config['SECRET_KEY'] = Config.SECRET_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = __str_connection.format(
                                                    username= Config.USERNAME, 
                                                    password= Config.PASSWORD, 
                                                    server=Config.HOSTNAME, 
                                                    database=Config.DATABASE
                                                )

db = SQLAlchemy(app=app)


def create_db():
    
    mydb = connector.connect(
        host=Config.HOSTNAME,
        user=Config.USERNAME,
        password=Config.PASSWORD
    )
    mycursor = mydb.cursor()

    mycursor.execute(f"DROP DATABASE IF EXISTS {Config.DATABASE}")
    mycursor.execute(f"CREATE DATABASE {Config.DATABASE} CHARSET = utf8;")
    mydb.close()
    mycursor.close()
    
    db.create_all()
    
