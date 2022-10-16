import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Models.User import User

class CrearEmpleadoController():
    
    def __init__(self, WidEmpleadoCre):
        self.widEmpleado = WidEmpleadoCre
        self.crear = User()
        
    def crearEmpleado(self, nombre, contrasena, rol, id_negocio,cedula,crearEmpleado):
        if nombre and contrasena and rol and id_negocio and cedula:
            self.crear.createUser(nombre, contrasena, rol, id_negocio,cedula)
        crearEmpleado.hide()