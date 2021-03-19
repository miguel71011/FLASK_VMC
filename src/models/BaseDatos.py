import src.config.globals as globals

class DB: 
    def BaseDeDatos(self): 
        cursor = globals.DB.cursor() 

        cursor.execute('show databases')

        basededatos = cursor.fetchall()

        cursor.close()

        return basededatos
    
    def trearTables(self, nombre):
        cursor = globals.DB.cursor()
        

        cursor.execute("use " + nombre)
        cursor.execute('show tables')

        tabla = cursor.fetchall()

        cursor.close()

        return tabla

    def descripciondeTable(self, nombre):
        cursor = globals.DB.cursor()
        
        cursor.execute("desc " + nombre)

        descripcion = cursor.fetchall()

        cursor.close()

        return descripcion