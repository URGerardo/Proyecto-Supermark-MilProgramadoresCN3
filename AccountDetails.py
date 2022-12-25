import tkinter as tk
from tkinter import ttk

class DatosCuenta(ttk.Frame):
    def __init__(self, parent, Cuenta):
        super().__init__(parent, padding=(10))
        self.parent = parent
        self.cuenta = Cuenta
        self.parent.resizable(False, False)
        self.parent.title("Supermark | Your Account")
        self.parent.configure(background="#c7ecee")
        self.windowDevelop()
    
    def windowDevelop(self):
        self.parent.geometry("800x350")
        ttk.Label(self.parent, text="Supermark | Tu Cuenta", justify='center', padding=20, font=("Arial", 25, 'bold'), background='#303952', foreground='white').pack(fill='both')
        
        seccionDatos = ttk.LabelFrame(self.parent, text="Datos Personales", )
        seccionDatos.place(x=120, y=130, width=600)
        nom = ttk.Label(seccionDatos, text=f'NOMBRE: {self.cuenta[0]}', padding=10).pack(side='left')
        ap = ttk.Label(seccionDatos, text=f'APELLIDO: {self.cuenta[1]}', padding=10).pack(side='left', after=nom)
        ttk.Label(seccionDatos, text=f'CORREO: {self.cuenta[4]}', padding=10).pack(side='left', after=ap)

        seccionCuenta = ttk.LabelFrame(self.parent, text="Datos de la Cuenta")
        seccionCuenta.place(x=120, y=210, width=600)
        us = ttk.Label(seccionCuenta, text=f'USUARIO:  {self.cuenta[2]}', padding=10).pack(side='left')
        ttk.Label(seccionCuenta, text=f'CONTRASEÑA:  {self.cuenta[3]}', padding=10).pack(side='left', after=us)

