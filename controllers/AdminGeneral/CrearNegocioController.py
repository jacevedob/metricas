import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Models.Negocio import Negocios

class CrearNegocioController():
    
    def __init__(self, WidNegocioCre):
        self.widNegocio = WidNegocioCre
        self.crear = Negocios()
        
    def crearNegocio(self,nombre,estilo,rut,crearNegocio):
        if nombre and estilo and rut or rut == 0:
            self.crear.createNegocio(nombre,estilo,rut)
            crearNegocio.hide()