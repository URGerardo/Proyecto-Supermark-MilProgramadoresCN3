from CustomerController import Cliente
from DatabaseController import ConexionesBaseDatos
from tkinter import messagebox

class Administrador(Cliente):
    def _init__(self, id, nombre, apellido, usuario, contraseña, correo):
        super().__init__(id, nombre, apellido, usuario, contraseña, correo)

    @staticmethod
    def cargarProducto(producto, stock, precioUnidad):
        conexion = ConexionesBaseDatos()
        conexion.executeInsert(f'Insert into Productos(nombre, cantidad, precioUnitario) VALUES ("{producto}", {stock}, {precioUnidad})')
        conexion.closeConection()
        messagebox.showinfo(title="Producto Cargado | Supermark", message="¡Cargaste un producto!")
    
    def obtenerNombreProductos(self):
        conex = ConexionesBaseDatos()
        nombres = conex.executeQueryLong('select nombre from Productos')
        conex.closeConection()
        return nombres

    def modificarProducto(self, nombreProducto):
        pass
        # conexion = ConexionesBaseDatos()
        # comando = conexion.executeQuery(f'UPDATE Productos set')




