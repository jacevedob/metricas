import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Models.User import User

class ActualizarEmpleadoController():
    
    def __init__(self, WidEmpleadoActu):
        self.widEmpleado = WidEmpleadoActu
        self.actualizar = User()
        
    def actualizarEmpleado(self,id, nombre, contrasena, rol, id_negocio,cedula,actualizarEmpleado):
        if nombre and contrasena and rol and id_negocio and cedula and id:
            self.actualizar.updateUser(id,nombre,contrasena,rol,id_negocio,cedula)
        actualizarEmpleado.hide()
