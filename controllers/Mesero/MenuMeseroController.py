import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets

class LoginMesero():
    
    def __init__(self,MenuMesero):
        self.mesero = MenuMesero

    def openPedido(self, Ui_Principal):
        self.mesero.Form = QtWidgets.QMainWindow()
        self.mesero.ui = Ui_Principal()
        self.mesero.ui.setupUi(self.mesero.Form)
        self.mesero.Form.show()

    def openFactura(self, Ui_facturas):
        self.mesero.Ventana = QtWidgets.QMainWindow()
        self.mesero.ui = Ui_facturas()
        self.mesero.ui.setupUi(self.mesero.Ventana)
        self.mesero.Ventana.show()
