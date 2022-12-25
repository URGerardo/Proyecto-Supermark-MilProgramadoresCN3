import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *

from UserController import Usuario
from CustomerController import Cliente
from DatabaseController import ConexionesBaseDatos
from AccountDetails import DatosCuenta

class SuperMarkApplication(ttk.Frame):
    def __init__(self, parent, user, admin):
        super().__init__(parent, padding=(10))
        self.parent = parent
        self.user = user
        self.admin = admin
        parent.resizable(False, False)

        self.producto = tk.IntVar()
        self.cantidad = tk.IntVar()
        self.conexionUpdate = ConexionesBaseDatos()

        self.columnasProductos = ("id", "Nombre", "cantidad", "Precio")

        if not self.admin == True:
            usuario = Usuario()
            self.Cliente = usuario.createCustomer(self.user)
            self.customerGUI()
        else:
            usuario = Usuario()
            self.Administrator = usuario.createAdmin(self.user)
            self.adminGUI()
        
    def customerGUI(self):
        '''Crea el entorno del supermercado para el Cliente'''
        self.parent.geometry("1250x600")
        self.parent.title("Supermark | Main Page")
        self.parent.configure(background='#f7f1e3')
        title = ttk.Label(self.parent, text="Supermark | Siempre Junto a Vos", justify='center', padding=20, font=("Arial", 25, 'bold'), background='#273c75', foreground='white').pack(fill='both')
        color = ttk.Label(self.parent, text="", padding=50, font=("Arial", 25), background='#273c75').pack(fill='both', after=title, side='left')
    
        ttk.Button(self.parent, text="Cerrar Sesión", padding=10, command=lambda:self.parent.destroy()).place(x=1100, y=20, width=120)
        ttk.Button(self.parent, text="Cuenta", padding=8, command=self.openAccountDetails).place(x=6, y=550)

        #TODO: Creación de la tabla donde se muestran los productos
        grilla = ttk.Treeview(self.parent, columns=self.columnasProductos, show="headings", selectmode='browse')
        grilla.place(x=425, y=110, bordermode='inside')
        grilla.heading('id', text='Identificador')
        grilla.heading('Nombre', text='Producto')
        grilla.heading('cantidad', text='Cantidad')
        grilla.heading('Precio', text='Precio')
        
        productosVenta = self.obtenerProductos()
        for producto in productosVenta:
            grilla.insert('', tk.END, values=producto)

        #TODO: Apartado Agregar Producto al carro del cliente
        seccion1 = ttk.LabelFrame(self.parent, text="Agregar Producto al Carrito")
        seccion1.place(x=140, y=130, width=260)
        a = ttk.Button(seccion1, text="Agregar", command=self.agregarCarrito).pack(side='left', ipadx=10, padx=5)
        b = ttk.Entry(seccion1, textvariable=self.producto).pack(side='top', after=a, pady=10)
        ttk.Entry(seccion1, textvariable=self.cantidad).pack(side='bottom', after=b, pady=10)

        #TODO: Apartado Ver Productos Seleccionados
        seccion2 = ttk.LabelFrame(self.parent, text="Productos en Carrito")
        seccion2.place(x=140, y=250, width=260)
        a = ttk.Button(seccion2, text="Ver tus productos", command=self.mostrarCarrito, width=250, padding=20).pack(ipadx=10, padx=5)

        #TODO: Apartado comprar Carrito
        seccion2 = ttk.LabelFrame(self.parent, text="Comprar Productos Seleccionados")
        seccion2.place(x=140, y=350, width=260)
        a = ttk.Button(seccion2, text="¡Comprar carrito!", command=self.buyItems, width=250, padding=20).pack(ipadx=10, padx=5)

    def adminGUI(self):
        '''Instanciación de la interfaz de usuario para los Administradores'''
        print(self.Administrator.datosCuenta())
        self.parent.geometry("1200x700")
        self.parent.title("Supermark | Administration System")
        self.parent.configure(background="#2d3436")
        title = ttk.Label(self.parent, text="Supermark | Administration System", justify='center', padding=30, font=("Arial", 25, 'bold'), background='#1e272e', foreground='white').pack(fill='both')

        nomProducto = tk.StringVar()
        cantidadProducto = tk.IntVar()
        precioProducto = tk.DoubleVar()

        #TODO: Sección para carga de producto
        CargaProd = ttk.LabelFrame(self.parent, text="Cargar Productos", padding=15)
        CargaProd.place(x=100, y=130, width=300)
        botonCarga = ttk.Button(CargaProd, text="Cargar", width=10, padding=5, command=lambda:self.Administrator.cargarProducto(nomProducto.get(), cantidadProducto.get(), precioProducto.get())).pack(ipadx=10, padx=5, side='left')
        desc1 = ttk.Label(CargaProd, text="Nombre del Producto").pack(side='top')
        productoID = ttk.Entry(CargaProd, textvariable=nomProducto, justify='center').pack(pady=5, padx=10, after=desc1)
        ttk.Label(CargaProd, text="Cantidad Producto").pack(side='top', after=productoID)
        cantidad = ttk.Entry(CargaProd, textvariable=precioProducto, justify='center').pack(side='bottom', after=productoID, pady=5)
        ttk.Label(CargaProd, text="Precio Producto").pack(side='bottom', after=cantidad)
        precio = ttk.Entry(CargaProd,textvariable=cantidadProducto, justify='center').pack(side='bottom', after=cantidad, pady=5)

        productoSeleccionado = tk.StringVar()
        nuevaCantidad = tk.IntVar()
        nuevoPrecio = tk.DoubleVar()
        #TODO: Sección para modificar datos de un producto

        ModProd = ttk.LabelFrame(self.parent, text="Modificar Productos", padding=2)
        ModProd.place(x=100, y=400, width=300, height=80)
        datosLista = self.Administrator.obtenerNombreProductos()
        box = ttk.Combobox(ModProd, values=datosLista, state='readonly', textvariable=productoSeleccionado).pack(side='left', padx=5)
        ttk.Button(ModProd, text="Modificar").pack(side='left', after=box, padx=2)
        ttk.Entry(ModProd, textvariable=nuevoPrecio, justify='center').pack(side='bottom', after=box)
        cant = ttk.Spinbox(ModProd, increment=1, from_=0, to=100, width=20, justify='center').pack(side='right', after=box, pady=5)



    def agregarCarrito(self):
        '''Agrega un producto al carrito local del cliente'''
        con = ConexionesBaseDatos()
        infoProd = con.executeQuery(f'Select nombre, cantidad from Productos where id = "{self.producto.get()}"')
        con.closeConection()
        try:
            if self.cantidad.get() <= infoProd[1] and infoProd[1] > 0:
                self.Cliente.agregarProductoCarrito(infoProd[0], self.cantidad.get())
                self.actualizarCantidad(self.cantidad.get(), infoProd[1], self.producto.get())
            else:
                messagebox.showerror(title='Límite superado | Supermark', message='Elige una cantidad menor.')
        except TypeError:
            messagebox.showwarning(title="Producto no disponible | Supermark", message="¡Aún no agregamos ese producto!")
    
    def mostrarCarrito(self):
        '''Devuelve los items que se encuentran en el carrito del cliente'''
        lista = self.Cliente.listadoCarrito()
        if lista != None:
            print(lista)
        else:
            pass
    
    def obtenerProductos(self):
        '''Obtiene los productos actualizados desde la Base de Datos'''
        bd = ConexionesBaseDatos()
        productos = bd.executeQueryLong('Select * from Productos')
        return productos
    
    def actualizarCantidad(self, cantidad, cantidadOriginal, idProducto):
        '''Realiza un Update sobre la cantidad de determinado producto'''
        self.conexionUpdate.executeQuery(f'Update Productos set cantidad={cantidadOriginal-cantidad} where id={idProducto}')
        messagebox.showinfo(title='Operación Realizada | Supermark', message='¡El producto se añadió a tu carrito!')
    
    def buyItems(self):
        '''Publica todos los cambios en la Base de Datos una vez se concreta la compra'''
        listaProductos = self.Cliente.listadoCarrito()
        if listaProductos != None:
            self.conexionUpdate.push()
            self.conexionUpdate.closeConection()
            messagebox.showinfo(title="Supermark || Compras", message="¡Compraste los productos correctamente!")
    
    def openAccountDetails(self):
        '''Obtiene los datos de la cuenta del Usuario correspondiente (sea Administrador o Cliente)'''
        ventanaCuenta = tk.Toplevel(self.parent)
        cuenta = self.Cliente.datosCuenta()
        DatosCuenta(ventanaCuenta, cuenta).pack()