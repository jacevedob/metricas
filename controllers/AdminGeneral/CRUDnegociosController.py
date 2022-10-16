import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Models.Negocio import Negocios

class CRUDnegociosController():
    
    def __init__(self, Negocio):
        self.CRUDnegocios = Negocios()
        self.negocios = Negocio
    
    def listaNegocios(self):
        table = self.negocios.tableNegocios
        negocios = self.CRUDnegocios.readNegocios()
        table.setRowCount(0)
        if negocios:
            for row_number, row_data in enumerate(negocios):
                table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                
    def seleccionarNegocio(self):
        table = self.negocios.tableNegocios
        if table.currentItem() != None:
            id_negocio = table.currentItem().text()
            negocio = self.CRUDnegocios.readNegocio(id_negocio)
            if negocio:
                mensaje = QMessageBox()
                mensaje.setWindowTitle("Información")
                mensaje.setText("Información del negocio:")
                mensaje.setIcon(QMessageBox.Information)
                mensaje.setStandardButtons(QMessageBox.Ok)
                mensaje.setDefaultButton(QMessageBox.Ok)
                mensaje.setInformativeText("Id: "+str(negocio[0])+"\nNombre: "+str(negocio[1])+"\nEstilo Comida: "+str(negocio[2])+"\nRut: "+str(negocio[3]))
                mensaje.exec_()
        else:
            mensaje = QMessageBox()
            mensaje.setWindowTitle("Información")
            mensaje.setText("Por favor seleccione el id del empleado")
            mensaje.setIcon(QMessageBox.Information)
            mensaje.setStandardButtons(QMessageBox.Ok)
            mensaje.setDefaultButton(QMessageBox.Ok)
            mensaje.exec_()

    def borrarNegocio(self):
        table = self.negocios.tableNegocios
        if table.currentItem() != None:
            id_negocio = table.currentItem().text()
            negocio =  self.CRUDnegocios.readNegocio(id_negocio)
            if negocio:
                self.CRUDnegocios.deleteNegocio(id_negocio)
        self.listaNegocios()
    
    def abrirCrearNegocios(self, Ui_crearNegocio):
        self.negocios.Form = QtWidgets.QWidget()
        self.negocios.ui = Ui_crearNegocio()
        self.negocios.ui.setupUi(self.negocios.Form)
        self.negocios.Form.show()
    
    def  abrirActualizarNegocios(self, Ui_actualizarNegocio):
        table = self.negocios.tableNegocios
        if table.currentItem() != None:
            id_negocio = table.currentItem().text()
            negocio = self.CRUDnegocios.readNegocio(id_negocio)
            if negocio:
                self.negocios.Form2 = QtWidgets.QWidget()
                self.negocios.ui = Ui_actualizarNegocio()
                self.negocios.ui.setupUi(self.negocios.Form2, negocio)
                self.negocios.Form2.show()
        else:
            mensaje = QMessageBox()
            mensaje.setWindowTitle("Información")
            mensaje.setText("Por favor seleccione el id del empleado")
            mensaje.setIcon(QMessageBox.Information)
            mensaje.setStandardButtons(QMessageBox.Ok)
            mensaje.setDefaultButton(QMessageBox.Ok)
            mensaje.exec_()
            
    def ventanaMenuAdminGeneral(self,Ui_MenuAdminGeneral,Negocio):
        Negocio.hide()
        Ui_MenuAdminGeneral.show()