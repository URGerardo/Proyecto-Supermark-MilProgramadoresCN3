import tkinter as tk
from tkinter import ttk, messagebox

from DatabaseController import ConexionesBaseDatos
from UserController import Usuario

class CheckIn(ttk.Frame):
    def __init__(self, parent):
        self.parent = parent
        super().__init__(parent, padding=(10))
        parent.title("Registro | Supermark")
        parent.resizable(False, False)
        
        self.nombre = tk.StringVar()
        self.apellido = tk.StringVar()
        self.email = tk.StringVar()
        self.usuario = tk.StringVar()
        self.contraseña = tk.StringVar()
        self.registro()

    def registro(self):
        ttk.Label(self, text="Nombre completo", padding=12).grid(row= 1, column= 0)
        ttk.Entry(self, textvariable=self.nombre, width=30).grid(row= 1, column = 1)
        ttk.Label(self, text="Apellidos", padding = 12, justify='left').grid(row= 2, column= 0)
        ttk.Entry(self, textvariable=self.apellido, width=30).grid(row= 2, column = 1)
        ttk.Label(self, text="Correo Electrónico", padding = 12).grid(row= 3, column= 0)
        ttk.Entry(self, textvariable=self.email, width=30).grid(row= 3, column = 1)

        separador1 = ttk.Label(self, text="   ", padding = 12).grid(row= 1, column= 3)
        separador2 = ttk.Label(self, text="   ", padding = 12).grid(row= 1, column= 4)

        ttk.Label(self, text="Usuario: ", padding = 12).grid(row= 2, column= 4)
        ttk.Entry(self, textvariable=self.usuario, width=30).grid(row= 2, column = 5)
        ttk.Label(self, text="Contraseña: ", padding = 12).grid(row= 3, column= 4)
        ttk.Entry(self, textvariable=self.contraseña, width=30).grid(row= 3, column = 5)

        registrar = ttk.Button(self, command=self.verificarDatos, text= "Registrarme").grid(row=5, column=6)

    def verificarDatos(self):
        if (self.nombre.get() and self.apellido.get() and self.email.get() and self.usuario.get() and 
        self.contraseña.get()) != "":
            self.registrarBaseDatos()
        else:
            messagebox.showerror(title="Error al registrar | Supermark", message="¡Hay campos todavía vacios!")
    
    def registrarBaseDatos(self):
        registroCliente = Usuario()
        registroCliente.registrar(self.nombre.get(), self.apellido.get(), self.email.get(), self.usuario.get(), self.contraseña.get())
        messagebox.showinfo("Usuario creado | Supermark", message="¡Tu usuario fué creado correctamente!")
        self.parent.destroy()
        