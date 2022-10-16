import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Models.Productos import Productos

class CrearProductoController():
    
    def __init__(self, WidProductosCre):
        self.crear = Productos()
        self.widProductos = WidProductosCre
                
    def crearProducto(self, nombre, descripcion, precio, id_negocio, crearProducto):
        if nombre and descripcion and precio and id_negocio:
            self.crear.createProducto(nombre,descripcion,precio,id_negocio)
        crearProducto.hide()