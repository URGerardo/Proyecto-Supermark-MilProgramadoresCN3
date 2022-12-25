from LoginController import IniciarSesion
from Supermercado import SuperMarkApplication
import tkinter as tk

# class AplicationMainExecute():
#     def __init__(self):
#         pass

#     def crearIniciarSesion(self):
#         root = tk.Tk()
#         IniciarSesion(root).grid()
#         root.mainloop()

#     def crearA(self):
#         nuevaInstancia = tk.Tk()
#         SuperMarkApplication(nuevaInstancia).grid()
#         nuevaInstancia.mainloop()

# a = AplicationMainExecute()
# b = a.crearIniciarSesion()
    
# if not b != None:
#     print(b)
#     a.crearA()

def crearIniciarSesion():
    root = tk.Tk()
    IniciarSesion(root).grid()
    photo = tk.PhotoImage(file = 'icono.png')
    root.wm_iconphoto(False, photo)
    root.mainloop()

crearIniciarSesion()