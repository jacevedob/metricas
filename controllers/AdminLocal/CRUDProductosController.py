from itertools import product
import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Models.Productos import Productos

class CRUDproductosController():
    
    def __init__(self,VenProductos):
        self.productos = VenProductos
        self.CRUDproductos = Productos()
        
    def listaProductos(self):
        table = self.productos.tableProductos
        productos = self.CRUDproductos.readProductos()
        table.setRowCount(0)
        if productos:
            for row_number, row_data in enumerate(productos):
                table.insertRow(row_number)
                for colum_numer, data in enumerate(row_data):
                    table.setItem(row_number, colum_numer, QtWidgets.QTableWidgetItem(str(data)))
    
    def seleccionarProducto(self):
        table = self.productos.tableProductos
        if table.currentItem() != None:
            id = table.currentItem().text()
            producto = self.CRUDproductos.readProducto(id)
            if producto:
                mensaje = QMessageBox()
                mensaje.setWindowTitle("Información")
                mensaje.setText("Informacion del producto:")
                mensaje.setIcon(QMessageBox.Information)
                mensaje.setStandardButtons(QMessageBox.Ok)
                mensaje.setDefaultButton(QMessageBox.Ok)
                mensaje.setInformativeText("ID:"+str(producto[0])+
                                                    "\nNombre: "+str(producto[1])+
                                                    "\nDescripción: "+str(producto[2])+
                                                    "\nPrecio: "+str(producto[3])+
                                                    "\nNegocio: "+str(producto[4]))                                                                                      
                mensaje.exec_()
        else:
            mensaje = QMessageBox()
            mensaje.setWindowTitle("Información")
            mensaje.setText("Por favor seleccione el id del empleado")
            mensaje.setIcon(QMessageBox.Information)
            mensaje.setStandardButtons(QMessageBox.Ok)
            mensaje.setDefaultButton(QMessageBox.Ok)
            mensaje.exec_()
                
                
    def borrarProducto(self):
        table = self.productos.tableProductos
        if table.currentItem() != None:
            id_producto = table.currentItem().text()
            producto = self.CRUDproductos.readProducto(id_producto)
            if producto:
                self.CRUDproductos.deleteProducto(id_producto)
        self.listaProductos()
    
    def abrirCrearProducto(self, Ui_CrearProducto):
        self.productos.Form = QtWidgets.QWidget()
        self.productos.ui = Ui_CrearProducto()
        self.productos.ui.setupUi(self.productos.Form)
        self.productos.Form.show()
    
    def abrirActualizarProducto(self, Ui_ActualizarProducto):
        table = self.productos.tableProductos
        if table.currentItem() != None:
            id_producto = table.currentItem().text()
            producto = self.CRUDproductos.readProducto(id_producto)
            if producto:
                self.productos.Form2 = QtWidgets.QWidget()
                self.productos.ui = Ui_ActualizarProducto()
                self.productos.ui.setupUi(self.productos.Form2, producto)
                self.productos.Form2.show()
    
    def ventanaMenuAdminlocal(self,Ui_MenuAdminLocal, Productos):
        Productos.hide()
        Ui_MenuAdminLocal.show()