import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *

from UserController import Usuario
from CustomerController import Cliente
from DatabaseController import ConexionesBaseDatos

class SuperMarkApplication(ttk.Frame):
    def __init__(self, parent, user, admin):
        super().__init__(parent, padding=(10))
        self.parent = parent
        self.user = user
        self.admin = admin
        parent.resizable(False, False)

        self.producto = tk.IntVar()
        self.cantidad = tk.IntVar()

        self.columnasProductos = ("id", "Nombre", "cantidad", "Precio")

        if not self.admin == True:
            usuario = Usuario()
            self.Cliente = usuario.createCustomer(self.user)
            self.customerGUI()
        else:
            print("Unu")
            self.adminGUI()
        
    def customerGUI(self):
        self.parent.geometry("1250x600")
        self.parent.title("Supermark | Main Page")
        ttk.Label(self.parent, text="SuperMark | Junto a vos, siempre", font=("Arial", 25), padding=20, justify='center').grid(row=1, column=3, ipadx=80)
        ttk.Label(self.parent, text="").grid(row=1, column=1, ipadx=50)
        grilla = ttk.Treeview(self.parent, columns=self.columnasProductos, show="headings", selectmode='browse')
        grilla.grid(row=2, column=3)
        grilla.heading('id', text='Identificador')
        grilla.heading('Nombre', text='Producto')
        grilla.heading('cantidad', text='Cantidad')
        grilla.heading('Precio', text='Precio')
        
        productosVenta = self.obtenerProductos()
        for producto in productosVenta:
            grilla.insert('', tk.END, values=producto)

        ttk.Button(self.parent, text="Agregar Producto", command= self.agregarCarrito, padding=25).grid(row=3, column=1, sticky='N')
        ttk.Entry(self.parent, textvariable=self.producto, width=20, justify='center').grid(row=3, column=2)
        ttk.Entry(self.parent, textvariable=self.cantidad, width=20, justify='center').grid(row=3, column=2, sticky='S')
        # ttk.Label(self.parent, text="").grid(row=2, column=2, ipadx=100)
        ttk.Label(self.parent, text="", padding=5).grid(row=4, column=1)
        ttk.Label(self.parent, text="", padding=5).grid(row=6, column=1)
        ttk.Button(self.parent, text="Comprar carrito", padding=20).grid(row=5, column=1)
        ttk.Button(self.parent, text="Ver Carrito", command=self.mostrarCarrito, padding=20).grid(row=7, column=1)

    def agregarCarrito(self):
        con = ConexionesBaseDatos()
        nombreProd = con.executeQuery(f'Select nombre from Productos where id = "{self.producto.get()}"')
        con.closeConection()
        self.Cliente.agregarProductoCarrito(nombreProd[0], self.cantidad.get())
    
    def mostrarCarrito(self):
        lista = self.Cliente.listadoCarrito()
        print(lista)

    def adminGUI(self):
        self.parent.geometry("1100x500")
        self.parent.title("Supermark | Administración")
        ttk.Label(self.parent, text="          ", ).grid(row=1, column=1)
        ttk.Label(self.parent, text="          ").grid(row=3, column=6)
        ttk.Button(self.parent, text="Agregar Producto", padding=20, width=50 ).grid(row=1, column=2)
        ttk.Button(self.parent, text="Actualizar Producto", padding=20, width=50).grid(row=2, column=2)
    
    def obtenerProductos(self):
        bd = ConexionesBaseDatos()
        productos = bd.executeQueryLong('Select * from Productos')
        return productos
