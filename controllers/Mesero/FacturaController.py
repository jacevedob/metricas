import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from Database.baseDatos import *
from Models.Factura import Factura

class facturaController():
    def __init__(self, facturas):
        self.factura = Factura()
        self.facturas = facturas

    def listPedidos(self):
        table = self.facturas.table_factura
        factura = self.factura.getFacturaP()
        table.setRowCount(0)
        for row_number, row_data in enumerate(factura):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))