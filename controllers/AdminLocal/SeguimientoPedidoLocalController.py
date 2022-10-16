import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Models.Pedido import Pedido
from PyQt5 import QtWidgets

class SeguimientoPedidoLocalController():
    
    def __init__(self, SeguimientoPedidoLocal):
        self.pedido = Pedido()
        self.seguimientoPedido = SeguimientoPedidoLocal
        
    def listaSeguimiento(self, id_negocio):
        table = self.seguimientoPedido.tableSeguimiento
        pedidosPendientesLocal = self.pedido.pedidosPendientesLocal(id_negocio)
        table.setRowCount(0)
        if pedidosPendientesLocal:
            for row_number, row_data in enumerate(pedidosPendientesLocal):
                table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    table.setItem(row_number,column_number, QtWidgets.QTableWidgetItem(str(data)))