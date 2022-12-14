import tkinter as tk
from tkinter import ttk, messagebox

from consultasDatabase import ConexionesBaseDatos

class RegistrarCliente(ttk.Frame):
    def __init__(self, parent):
        self.parent = parent
        super().__init__(parent, padding=(40))
        parent.title("Registro | Supermark")
        
        self.nombre = tk.StringVar()
        self.apellido = tk.StringVar()
        self.DNI = tk.StringVar()
        self.email = tk.StringVar()
        self.usuario = tk.StringVar()
        self.contraseña = tk.StringVar()
        self.registro()

    def registro(self):
        nombre = ttk.Label(self, text="Nombre completo", padding=12).grid(row= 1, column= 0)
        ingresoNombre = ttk.Entry(self, textvariable=self.nombre, width=30).grid(row= 1, column = 1)
        apellido = ttk.Label(self, text="Apellidos", padding = 12, justify='left').grid(row= 2, column= 0)
        ingresoApellido = ttk.Entry(self, textvariable=self.apellido, width=30).grid(row= 2, column = 1)
        DNI = ttk.Label(self, text="DNI", padding = 12).grid(row= 3, column= 0)
        ingresoDNI = ttk.Entry(self, textvariable=self.DNI, width=30).grid(row= 3, column = 1)
        DNI = ttk.Label(self, text="Correo Electrónico", padding = 12).grid(row= 4, column= 0)
        ingresoDNI = ttk.Entry(self, textvariable=self.email, width=30).grid(row= 4, column = 1)

        separador1 = ttk.Label(self, text="   ", padding = 12).grid(row= 1, column= 3)
        separador2 = ttk.Label(self, text="   ", padding = 12).grid(row= 1, column= 4)

        ttk.Label(self, text="NOMBRE DE USUARIO", padding = 12).grid(row= 2, column= 4)
        ttk.Entry(self, textvariable=self.usuario, width=30).grid(row= 2, column = 5)
        ttk.Label(self, text="CONTRASEÑA DE CUENTA", padding = 12).grid(row= 3, column= 4)
        ttk.Entry(self, textvariable=self.contraseña, width=30).grid(row= 3, column = 5)

        registrar = ttk.Button(self, command=self.verificarDatos).grid(row=5, column=6)

    def verificarDatos(self):
        if (self.nombre.get() and self.apellido.get() and self.DNI.get() and self.email.get() and self.usuario.get() and 
        self.contraseña.get()) != "":
            self.registrarBaseDatos()
        else:
            messagebox.showerror(title="Error al registrar | Supermark", message="¡Hay campos todavía vacios!")
    
    def registrarBaseDatos(self):
        consulta = ConexionesBaseDatos()
        consulta.insertData(f'Insert Into clientesRegistrados(nombre, apellido, DNI, usuario, contraseña, correo) VALUES("{self.nombre.get()}", "{self.apellido.get()}", "{self.DNI.get()}", "{self.usuario.get()}", "{self.contraseña.get()}", "{self.email.get()}")')
        consulta.push()
        consulta.closeConection()
        messagebox.showinfo(title="Información de Registro | Supermark", message="¡Creaste tu cuenta exitosamente!")
        self.parent.destroy()

        



