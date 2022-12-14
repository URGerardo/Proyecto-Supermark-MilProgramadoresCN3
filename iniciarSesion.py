import sqlite3 as SQL
import tkinter as tk
from tkinter import ttk, messagebox

from consultasDatabase import ConexionesBaseDatos
from registrarse import RegistrarCliente

class IniciarSesion(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=(10))
        self.parent = parent
        parent.title("Iniciar Sesion | Supermark")

        self.usuario = tk.StringVar()
        self.contraseña = tk.StringVar()
        self.crearWidgets()

    def crearWidgets(self):
        texto1 = ttk.Label(self, text="USUARIO:", padding=12).grid(row=1, column=1)
        entradaUsuario = ttk.Entry(self, textvariable = self.usuario, width=25).grid(row=1, column=2)
        texto2 = ttk.Label(self, text="Contraseña:", padding=12).grid(row=2, column=1)
        entradaContraseña = ttk.Entry(self, textvariable = self.contraseña, width=25, show="*").grid(row=2, column = 2)
        boton = ttk.Button(self, text="¡Ingresar!", padding=4, command = self.ingresarCuenta).grid(row=3, column= 5)
        boton = ttk.Button(self, text="Registro", padding=4, command = self.abrirRegistro).grid(row=3, column= 1)

    def abrirRegistro(self):
        toplevel = tk.Toplevel(self.parent)
        RegistrarCliente(toplevel).grid()
    
    def ingresarCuenta(self):
        consulta = ConexionesBaseDatos()
        datos = consulta.executeQuery(f'Select contraseña from clientesRegistrados us where us.usuario = "{self.usuario.get()}" or us.correo = "{self.usuario.get()}"')
        try:
            if datos[0] == self.contraseña.get():
                self.showInformation("Informativo","¡¡Ingresaste correctamente!!", "Supermark | Ingreso")
                self.cerrar()
            else:
                self.showInformation("¡Contraseña incorrecta!", "Error al ingresar | Supermark")
        except TypeError:
            self.showInformation("error", f'No existe el usuario "{self.usuario.get()}"', "Usuario Inexistente")
        finally:
            consulta.closeConection()
    
    def showInformation(self, tipoMensaje, text, titulo):
        if tipoMensaje.lower() == "informativo":
            messagebox.showinfo(message=text, title=titulo)
        elif tipoMensaje.lower() == "error":
            messagebox.showerror(message=text, title=titulo)

    def cerrar(self):
        self.parent.destroy()


# FIXME: 13/12/2022
# TODO: Crear ventanas secundarias -> TODO Registro