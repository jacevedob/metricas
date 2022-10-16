import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from Database.baseDatos import *
from Models.Pedido import Pedido

class CreatePedidoController():

    def __init__(self,create_pedido):
        self.pedido = Pedido()
        self.create_pedido = create_pedido

    def createPedido(self,ID_Pedido,ID_Negocio,Mesero,Mesa,Producto,Cantidad,CreatePedido):
        Estado = "Pendiente"
        if ID_Pedido and ID_Negocio and Mesero and Mesa and Producto and Cantidad and Estado:
            self.pedido.insertPedido(ID_Pedido,ID_Negocio,Mesero,Mesa,Producto,Cantidad,Estado)
            CreatePedido.hide()
    
