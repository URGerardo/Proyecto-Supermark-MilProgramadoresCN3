import sqlite3 as sql

class ConexionesBaseDatos():
    def __init__(self):
        self.base = r"C:\Users\CARLOS URIBURU\Desktop\SuperMark\BaseDatosSupermark\Base_Datos_Supermark.db"
        self.conexion = sql.connect(self.base)
        self.cursor = self.conexion.cursor()
    
    def executeQuery(self, consulta):
        self.cursor.execute(consulta)
        data = self.cursor.fetchone()
        return data

    def insertData(self, command):
        self.cursor.execute(command)

    def push(self):
        self.conexion.commit()
    
    def closeConection(self):
        self.conexion.close()

