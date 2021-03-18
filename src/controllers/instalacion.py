from flask import render_template, redirect, request, url_for
from src.config.db import createDB, instalarDB
from src import app
import json

@app.route('/tienesAcne', methods=['POST'])
def instalacion():
    name = request.form.get('nombre_base_datos')
    user = request.form.get('nombre_usuario')
    password = request.form.get('contrasena_base_datos')
    server = request.form.get('servidor_base_datos')
    port = request.form.get('puerto')

    dbData = {
        'host' : server,
        'port' : int(port),
        'user' : user,
        'password' : password,
        'database' : name,
    }

    file = open('src/config/conexion.json', 'w')
    file.write(json.dumps(dbData))
    file.close()

    createDB()
    instalarDB()

    return render_template('index.html')
    return redirect(url_for('index'))