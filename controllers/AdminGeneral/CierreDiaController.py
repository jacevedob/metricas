import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Models.Pedido import Pedido
from PyQt5 import QtWidgets
from Models.Negocio import Negocios
from Models.User import User

class CierreDiaController():
    
    def __init__(self, Cierre):
        self.pedido = Pedido()
        self.cierre = Cierre

    def total(self):
        total = self.pedido.totalVentasDia()
        return total[0]

    def listaNegocios(self):
        total = 0
        table = self.cierre.tableNegocio
        negociosDivididos = self.pedido.cierreNegocios()
        listaNegocios = Negocios.readNegocios(self)
        negociosFinal = []
        if negociosDivididos:
            for l in listaNegocios:
                itemListaNegocios = l[1]
                for j in negociosDivididos:
                    nombreNegociosDivididos = j[0]
                    ventaNegociosDividdios = j[1]
                    if itemListaNegocios == nombreNegociosDivididos:
                        total += ventaNegociosDividdios
                negociosFinal.append((itemListaNegocios,total))
                total = 0
            table.setRowCount(0)
            for row_number, row_data in enumerate(negociosFinal):
                table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def listaMesero(self):
        listaMeseros = User.getMeseros(self)
        total = 0
        table = self.cierre.tableMesero
        meserosDivididos = self.pedido.cierreMeseros()
        meserosFinal = []
        if meserosDivididos:
            for i in listaMeseros:
                itemListaMesos = i[0]
                for j in meserosDivididos:
                    nombreMeserosDividos = j[0]
                    ventaMeserosDividos = j[1]
                    if itemListaMesos == nombreMeserosDividos:
                        total += ventaMeserosDividos
                meserosFinal.append((itemListaMesos,total))
                total = 0
            table.setRowCount(0)
            for row_number, row_data in enumerate(meserosFinal):
                table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def listaMesa(self):
        mesaMax = self.pedido.mesaMayor()
        total = 0
        table = self.cierre.tableMesa
        mesasDivididas = self.pedido.cierreMesas()
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
                for column_number, data in enumerate(row_data):
                    table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))