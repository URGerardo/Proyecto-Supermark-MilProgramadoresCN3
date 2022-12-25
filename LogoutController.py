# from CustomerController import Cliente

# a = Cliente(1, "32", "adf", "adsf", "adfs")
# a.agregarProductoCarrito()


# a = [("1", "2"), (1, 7), (1, 6)]

# for i in a:
#     print(i[0])
#     print(i[1])

from DatabaseController import ConexionesBaseDatos

a = ConexionesBaseDatos()
a.insertData("UPDATE Productos SET cantidad=7 where id=1")
data = a.executeQuery('Select cantidad from Productos where id=1')
print(data)
a.closeConection()


import tkinter as tk
from tkinter import ttk

class IniciarSesion(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=(10))
        self.parent = parent
        parent.title("Iniciar Sesion | Supermark")
        self.parent.geometry("1250x600")
        parent.resizable(False, False)
        self.interfaz()

    def interfaz(self):
        title = ttk.Label(self.parent, text="Supermark | Siempre junto a vos", padding=20, font=("Arial", 20)).pack()
        
        titulo = ttk.LabelFrame(self.parent, text="Supermark | Siempre junto a vos", underline=20)
        titulo.pack(side="top", fill='x')

        tk.Label(titulo, text="Hola").pack(side="left")
        self.name = ttk.Entry(titulo)
        self.name.pack()


# root = tk.Tk()
# a = IniciarSesion(root)
# a.mainloop()

