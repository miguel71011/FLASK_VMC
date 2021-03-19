import mariadb
from os import path
import json
import src.config.globals as globals

CONEXCION_PATH = path.abspath('src/config/conexion.json')
SQL_PATH = path.abspath('Base_de_datos.sql')



def createDB():
    if path.exists(CONEXCION_PATH):
        file_conexion = open(CONEXCION_PATH, 'r')

        config = json.loads(file_conexion.read())


        globals.DB = mariadb.connect(**config)
        globals.DB.autocommit = True
    else:
        globals.DB = False



    


