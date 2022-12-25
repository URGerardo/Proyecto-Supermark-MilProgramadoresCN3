import tkinter as tk
from tkinter import ttk, messagebox

from DatabaseController import ConexionesBaseDatos
from UserController import Usuario
from SignupController import CheckIn
from Supermercado import SuperMarkApplication
from CustomerController import Cliente

class IniciarSesion(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=(10))
        self.parent = parent
        parent.title("Iniciar Sesion | Supermark")
        self.usuario = tk.StringVar()
        self.contraseña = tk.StringVar()
        self.crearWidgets()

    def crearWidgets(self):
        texto1 = ttk.Label(self, text="USUARIO:", padding=12).grid(row=1, column=0)
        entradaUsuario = ttk.Entry(self, textvariable = self.usuario, width=25).grid(row=1, column=1)
        texto2 = ttk.Label(self, text="Contraseña:", padding=12).grid(row=2, column=0)
        entradaContraseña = ttk.Entry(self, textvariable = self.contraseña, width=25, show="*").grid(row=2, column = 1)

        espaciado = ttk.Label(self, width=10).grid(row=1, column=2)

        boton = ttk.Button(self, text="¡Ingresar!", padding=4, command = self.ingresarCuenta).grid(row=4, column= 3)
        boton = ttk.Button(self, text="Registrarse", padding=4, command = self.registrarCuenta).grid(row=4, column= 1)

        sinCuenta = ttk.Label(self, text="¿Aún no tienes una cuenta?", foreground='Red').grid(row=4, column=0)
    
    def ingresarCuenta(self):
        consultaUsuarioRegistrado = Usuario()
        datos = consultaUsuarioRegistrado.buscarRegistro(self.usuario.get())

        if datos!= None:
            if datos[0] == self.contraseña.get() and datos[1] == "Cliente":
                self.parent.destroy()
                self.crearSupermercado(self.usuario.get(), False)

            elif datos[0] == self.contraseña.get() and datos[1] == "Admin":
                self.parent.destroy()
                self.crearSupermercado(self.usuario.get(), True)

            else:
                a = messagebox.showwarning("Error al Iniciar Sesión | Supermark", message="¡Contraseña inválida!")

        else:
            messagebox.showerror("Usuario inexistente | Supermark", message=f'El usuario "{self.usuario.get()}" no está registrado')
            print("¡El usuario no existe!")
    
    def obtenerRegistros(self, usuario):
        nuevaConsulta = Usuario()
        data = nuevaConsulta.registrosCompletos(usuario)
        return data
    
    def registrarCuenta(self):
        ventanaRegistro = tk.Toplevel(self.parent)
        CheckIn(ventanaRegistro).grid()
    
    @staticmethod
    def crearSupermercado(usuario, permisoAdmin):
        nuevaInstancia = tk.Tk()
        SuperMarkApplication(nuevaInstancia, usuario, permisoAdmin)
        nuevaInstancia.mainloop()

# Create Table clientes(id INTEGER UNIQUE NOT NULL, nombres TEXT NOT NULL, apellidos TEXT NOT NULL, correo TEXT NOT NULL UNIQUE, usuario TEXT NOT NULL UNIQUE, contraseña TEXT NOT NULL, rango INTEGER DEFAULT 1 NOT NULL, compras INTEGER NOT NULL DEFAULT 0, PRIMARY KEY(id AUTOINCREMENT))