import mariadb
from os import path
import json
import src.config.globals as globals

CONEXCION_PATH = path.abspath('src/config/conexion.json')
SQL_PATH = path.abspath('db.sql')

def createDB():
    if path.exists(CONEXCION_PATH):
        file_conexion = open(CONEXCION_PATH, 'r')

        config = json.loads(file_conexion.read())


        globals.DB = mariadb.connect(**config)
        globals.DB.autocommit = True

        return DB

def instalarDB():
    file_sql = open(SQL_PATH, 'r')
    sql = file_sql.read()

    cursor = globals.DB.cursor()

    sqlCommands = sql.split(';')
    
    for command in sqlCommands:
        try:
            if command.strip() != '':
                cursor.execute(command)
        except:
            print ("Saltando comando")

    cursor.close()


