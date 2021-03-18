from flask import render_template
from src import app
import src.config.globals as globals

@app.route('/')
def index():
   
    if globals.DB == False:
        
        return render_template('instalacion.html')
    else:
        
        return render_template('index.html')