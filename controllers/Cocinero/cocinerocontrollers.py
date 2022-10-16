import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from Database.baseDatos import *
from Models.Pedido import Pedido

class Actualizarlistascontrollers():
    def __init__(self, Principal):
        self.pedido = Pedido()
        self.principal = Principal

    def listPedidos(self):
        table = self.principal.table_primera
        pedido = self.pedido.getPedidosG()
        table.setRowCount(0)
        for row_number, row_data in enumerate(pedido):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def listpendientes(self):
        table = self.principal.table_segunda
        pedido = self.pedido.getPedidosAceptados()
        table.setRowCount(0)
        for row_number, row_data in enumerate(pedido):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def pedidoaceptado(self):
        table = self.principal.table_primera
        if table.currentItem()!=None:
            id_pedido = table.currentItem().text()    
            self.pedido.updateaceptar(id_pedido) 
            self.listpendientes()
            self.listPedidos()

    def pedidocancelar(self):
        table = self.principal.table_primera
        if table.currentItem()!=None:
            id_pedido = table.currentItem().text()    
            self.pedido.updatecancelar(id_pedido) 
            self.listpendientes()  
            self.listPedidos()               

    def pedidolisto(self):
        table = self.principal.table_segunda
        if table.currentItem()!=None:
            id_pedido = table.currentItem().text()    
            self.pedido.updateestado(id_pedido)
            self.listpendientes()
































        

                           


    

    #def __init__(self, estapedidocre):
       # self.estapedidocre = estapedidocre
       # self.crear = Pedido()

    #def pedidoslistos(self, estado,pedidoslistos ):
        #if estado:
           # self.crear.crearestado(estado)
       # pedidoslistos.hide()  



   
        


    
