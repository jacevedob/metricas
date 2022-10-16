import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Models.Pedido import Pedido
from PyQt5 import QtWidgets

class SeguimientoController():
    
    def __init__(self, SeguimientoPedido):
        self.pedido = Pedido()
        self.seguimientoPedido = SeguimientoPedido
        
    def listaSeguimiento(self):
        table = self.seguimientoPedido.tableSeguimiento
        pedidosPendientes = self.pedido.pedidosPendientes()
        table.setRowCount(0)
        if pedidosPendientes:
            for row_number, row_data in enumerate(pedidosPendientes):
                table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))