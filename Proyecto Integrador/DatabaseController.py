import sqlite3 as sql

class ConexionesBaseDatos():
    def __init__(self):
        self.base = r"C:\Users\CARLOS URIBURU\Desktop\Supermark2\BaseDatosSupermark.db"
        self.conexion = sql.connect(self.base)
        self.cursor = self.conexion.cursor()
    
    def executeQuery(self, consulta):
        self.cursor.execute(consulta)
        data = self.cursor.fetchone()
        return data
    
    def executeInsert(self, consulta):
        self.cursor.execute(consulta)
        self.push()

    def executeQueryLong(self, consulta):
        cursor = self.cursor.execute(consulta)
        data = cursor.fetchall()
        return data

    def insertData(self, command):
        self.cursor.execute(command)

    def push(self):
        self.conexion.commit()
    
    def closeConection(self):
        self.conexion.close()

