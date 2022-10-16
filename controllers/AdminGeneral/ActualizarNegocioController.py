import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Models.Negocio import Negocios

class ActualizarNegocioController():
    
    def __init__(self, WidNegocioActu):
        self.widNegocio = WidNegocioActu
        self.actualizar = Negocios()
        
    def actualizarEmpleado(self,id, nombre,estilo,rut,actualizarNegocio):
        if nombre and estilo and rut and id:
            self.actualizar.updateNegocio(id,nombre,estilo,rut)
        actualizarNegocio.hide()