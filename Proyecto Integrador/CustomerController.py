from DatabaseController import ConexionesBaseDatos

class Cliente():
    def __init__(self, id, nombre, apellido, usuario, contraseña):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.contraseña = contraseña
        self.carrito = []
    
    def datos(self):
        print(self.id, self.nombre, self.apellido, self.usuario, self.contraseña)

    def agregarProductoCarrito(self, producto, cantidad):
        if len(self.carrito) <= 30:
            self.carrito.append((producto, cantidad))
            print("Producto Agregado")
        else:
            return None
    
    def listadoCarrito(self):
        return self.carrito
        
    def agregarProductoBD(self, producto, cantidad):
        con = ConexionesBaseDatos()
        con.executeInsert(f'Insert into carrito(idCliente, Producto, Cantidad) VALUES({self.id}, "{producto}", {cantidad})')
        con.closeConection()


