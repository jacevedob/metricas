import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from Database.baseDatos import *
from Models.Pedido import Pedido

class PrincipalController():
    def __init__(self, principa):
        self.pedido = Pedido()
        self.principa = principa

    def listPedidos(self):
        table = self.principa.table_pedidos
        pedido = self.pedido.getPedidosP()
        table.setRowCount(0)
        for row_number, row_data in enumerate(pedido):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def openCreate(self, Ui_CreatePedido):
        self.principa.Form = QtWidgets.QWidget()
        self.principa.ui = Ui_CreatePedido()
        self.principa.ui.setupUi(self.principa.Form)
        self.principa.Form.show()
