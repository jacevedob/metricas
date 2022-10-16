import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Models.Pedido import Pedido
from PyQt5 import QtWidgets
from Models.User import User

class CierreDiaLocalController():
    
    def __init__(self, Cierre):
        self.pedido = Pedido()
        self.cierre = Cierre
        
    def total(self,idNegocio):
        total = self.pedido.totalVentasDiaLocal(idNegocio)
        return total[0]
    
    def listaMesero(self,idNegocio):
        listaMeseros = User.getMeseros(self)
        total = 0
        table = self.cierre.tableMesero
        meserosDivididos = self.pedido.cierreMeserosLocal(idNegocio)
        meserosFinal = []
        if meserosDivididos:
            for i in listaMeseros:
                itemListaMeseros = i[0]
                for j in meserosDivididos:
                    nombreMeserosDividos = j[0]
                    ventaMeserosDividos = j[1]
                    if itemListaMeseros == nombreMeserosDividos:
                        total += ventaMeserosDividos
                meserosFinal.append((itemListaMeseros,total))
                total = 0
            table.setRowCount(0)
            for row_number, row_data in enumerate(meserosFinal):
                table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                    
    def listaMesa(self,idNegocio):
        mesaMax = self.pedido.mesaMayor()
        total = 0
        table = self.cierre.tableMesa
        mesasDivididas = self.pedido.cierreMesasLocal(idNegocio)
        mesasFinal = []
        if mesasDivididas:
            for i in range(1,mesaMax+1):
                for j in mesasDivididas:
                    numeroMesaDividida = j[0]
                    ventaMesaDividida = j[1]
                    if i == numeroMesaDividida:
                        total += ventaMesaDividida
                mesasFinal.append((i,total))
                total = 0
            table.setRowCount(0)
            for row_number, row_data in enumerate(mesasFinal):
                table.insertRow(row_number)
                for colum_number, data in enumerate(row_data):
                    table.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))