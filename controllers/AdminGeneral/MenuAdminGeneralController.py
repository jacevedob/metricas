import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets

class MenuAdminGeneralController():
    
    def __init__(self, MenuGeneral):
        self.menuGeneral = MenuGeneral
        
    def ventanaCRUDempleados(self,Ui_Empleados, MenuAdminGeneral):
        self.menuGeneral.Ventana = QtWidgets.QMainWindow()
        self.menuGeneral.ui = Ui_Empleados()
        self.menuGeneral.ui.setupUi(self.menuGeneral.Ventana,MenuAdminGeneral)
        MenuAdminGeneral.hide()
        self.menuGeneral.Ventana.show()
        
    def ventanaCRUDnegocios(self,Ui_Negocios, MenuAdminGeneral):
        self.menuGeneral.Ventana = QtWidgets.QMainWindow()
        self.menuGeneral.ui = Ui_Negocios()
        self.menuGeneral.ui.setupUi(self.menuGeneral.Ventana,MenuAdminGeneral)
        MenuAdminGeneral.hide()
        self.menuGeneral.Ventana.show()

    def ventanaCierreDia(self,Ui_CierreDia):
        self.menuGeneral.Form = QtWidgets.QWidget()
        self.menuGeneral.ui = Ui_CierreDia()
        self.menuGeneral.ui.setupUi(self.menuGeneral.Form)
        self.menuGeneral.Form.show()
        
    def ventanaSeguimientoPedidos(self,Ui_SeguimientoPedido):
        self.menuGeneral.Form = QtWidgets.QWidget()
        self.menuGeneral.ui = Ui_SeguimientoPedido()
        self.menuGeneral.ui.setupUi(self.menuGeneral.Form)
        self.menuGeneral.Form.show()