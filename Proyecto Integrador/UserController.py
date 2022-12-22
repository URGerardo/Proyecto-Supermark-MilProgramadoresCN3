
from DatabaseController import ConexionesBaseDatos
from CustomerController import Cliente

class Usuario():
    def __init__(self):
        pass
    
    def registrar(self, nombres, apellidos, correo, usuario, contraseña):
        '''Registra una nueva instancia de un usuario'''
        registro = ConexionesBaseDatos()
        registro.executeInsert(f'Insert into clientes(nombres, apellidos, correo, usuario, contraseña) VALUES("{nombres}", "{apellidos}", "{correo}", "{usuario}", "{contraseña}")')
        registro.push()
        registro.closeConection()
    
    def buscarRegistro(self, usuario):
        '''Busca las credenciales de un usuario existente (contraseña de cuenta)'''
        credencial = ConexionesBaseDatos()
        credenciales = credencial.executeQuery(f'Select contraseña, nombreRango from clientes join rango on rango.id = clientes.rango where clientes.usuario = "{usuario}" or clientes.correo = "{usuario}"')
        credencial.closeConection()
        return credenciales
     
    def registrosCliente(self, usuario):
        registros = ConexionesBaseDatos()
        dataUser = registros.executeQuery(f'Select id, nombres, apellidos, usuario, contraseña from clientes where "{usuario}" = clientes.usuario or "{usuario}" == clientes.correo')
        registros.closeConection()
        return dataUser
    
    @staticmethod
    def createCustomer(usuario):
        registros = ConexionesBaseDatos()
        dataUser = registros.executeQuery(f'Select id, nombres, apellidos, usuario, contraseña from clientes where "{usuario}" = clientes.usuario or "{usuario}" == clientes.correo')
        registros.closeConection()
        clienteCreado = Cliente(id=dataUser[0], nombre = dataUser[1], apellido=dataUser[2], usuario=dataUser[3], contraseña=dataUser[4])
        return clienteCreado

    def createAdmin(self):
        pass