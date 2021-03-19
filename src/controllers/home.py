from flask import render_template
from src import app
import src.config.globals as globals
from src.models.BaseDatos import DB


@app.route('/')
def index():
   
    if globals.DB == False:
        
        return render_template('instalacion.html')
    else:
        Db = DB()
        db =Db.BaseDeDatos()
        print()
        return render_template('index.html', db=db)

@app.route('/tablas/<nombre>')
def verTables(nombre):
    Db = DB()

    tablas = Db.trearTables(nombre)

    return render_template('tabla.html', tablas=tablas)

@app.route('/descripcion/<nombre>')
def descripcion(nombre):
    Db = DB()

    desc = Db.descripciondeTable(nombre)

    return render_template('descripcion.html', descripcion=desc)       
