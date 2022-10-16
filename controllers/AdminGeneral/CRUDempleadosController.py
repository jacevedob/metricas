import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Models.User import User

class CRUDempleadosController():
    
    def __init__(self, Empleados):
        self.CRUDempleados = User()
        self.empleados = Empleados
    
    def listaEmpleados(self):
        table = self.empleados.tableEmpleados
        empleados = self.CRUDempleados.readUsers()
        table.setRowCount(0)
        if empleados:
            for row_number, row_data in enumerate(empleados):
                table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                
    def seleccionarEmpleado(self):
        table = self.empleados.tableEmpleados
        if table.currentItem() != None:
            cod = table.currentItem().text()
            usuario = self.CRUDempleados.readUser(cod)
            if usuario:
                mensaje = QMessageBox()
                mensaje.setWindowTitle("Información")
                mensaje.setText("Información del Empleado:")
                mensaje.setIcon(QMessageBox.Information)
                mensaje.setStandardButtons(QMessageBox.Ok)
                mensaje.setDefaultButton(QMessageBox.Ok)
                mensaje.setInformativeText("ID: "+str(usuario[0])+"\nNombre: "+usuario[1]+"\nContraseña: "+usuario[2]+"\nRol: "+str(usuario[3])+"\nNegocio: "+str(usuario[4])+"\nDocumento: "+str(usuario[5]))
                mensaje.exec_()
        else:
            mensaje = QMessageBox()
            mensaje.setWindowTitle("Información")
            mensaje.setText("Por favor seleccione el id del empleado")
            mensaje.setIcon(QMessageBox.Information)
            mensaje.setStandardButtons(QMessageBox.Ok)
            mensaje.setDefaultButton(QMessageBox.Ok)
            mensaje.exec_()

    def borrarEmpleado(self):
        table = self.empleados.tableEmpleados
        if table.currentItem() != None:
            id_usu = table.currentItem().text()
            usuario =  self.CRUDempleados.readUser(id_usu)
            if usuario:
                self.CRUDempleados.deleteUser(id_usu)
        self.listaEmpleados()
    
    def abrirCrearEmpleado(self, Ui_crearEmpleado):
        self.empleados.Form = QtWidgets.QWidget()
        self.empleados.ui = Ui_crearEmpleado()
        self.empleados.ui.setupUi(self.empleados.Form)
        self.empleados.Form.show()
    
    def abrirActualizarEmpleado(self, Ui_actualizarEmpleado):
        table = self.empleados.tableEmpleados
        if table.currentItem() != None:
            cod = table.currentItem().text()
            usuario = self.CRUDempleados.readUser(cod)
            if usuario:
                self.empleados.Form2 = QtWidgets.QWidget()
                self.empleados.ui = Ui_actualizarEmpleado()
                self.empleados.ui.setupUi(self.empleados.Form2, usuario)
                self.empleados.Form2.show()
        else:
            mensaje = QMessageBox()
            mensaje.setWindowTitle("Información")
            mensaje.setText("Por favor seleccione el id del empleado")
            mensaje.setIcon(QMessageBox.Information)
            mensaje.setStandardButtons(QMessageBox.Ok)
            mensaje.setDefaultButton(QMessageBox.Ok)
            mensaje.exec_()
                        
    def ventanaMenuAdminGeneral(self,Ui_MenuAdminGeneral,Empleados):
        Empleados.hide()
        Ui_MenuAdminGeneral.show()