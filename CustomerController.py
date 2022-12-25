from DatabaseController import ConexionesBaseDatos
from tkinter import messagebox

class Cliente():
    def __init__(self, id, nombre, apellido, usuario, contraseña, correo):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.email = correo
        self.contraseña = contraseña
        self.carrito = []
    
    def datosCuenta(self):
        return [self.nombre, self.apellido, self.usuario, self.contraseña, self.email]

    def agregarProductoCarrito(self, producto, cantidad):
        if len(self.carrito) <= 30:
            self.carrito.append((producto, cantidad))
            print("Producto Agregado")
        else:
            return None
    
    def listadoCarrito(self):
        if len(self.carrito) != 0:
            return self.carrito
        else:
            messagebox.showwarning(title="Supermark", message="¡El carrito está vacío!")
        
    def agregarProductoBD(self, producto, cantidad):
        con = ConexionesBaseDatos()
        con.executeInsert(f'Insert into carrito(idCliente, Producto, Cantidad) VALUES({self.id}, "{producto}", {cantidad})')
        con.closeConection()


