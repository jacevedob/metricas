import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Models.Productos import Productos

class ActualizarProductoController():
    
    def __init__(self, WidProductoActu):
        self.widProducto = WidProductoActu
        self.actualizar = Productos()
        
    def actualizarProducto(self, id, nombre, descripcion, precio, negocio, actualizarProducto):
        if nombre and descripcion and precio and negocio and id:
            self.actualizar.updateProducto(id,nombre,descripcion,precio,negocio)
        actualizarProducto.hide()