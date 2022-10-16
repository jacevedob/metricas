import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from Database.baseDatos import *
from PyQt5.QtWidgets import QMessageBox

class loginController():
    
    def __init__(self,Log_in):
        self.log_in = Log_in
        
    def logIn(self,usuario,contra,Ui_MenuAdminGeneral,Ui_MenuAdminLocal,LoginMesero,Ui_cocinero,Login):
        if usuario and contra:
            usuario = DB.iniciarSesion(usuario,contra)
            if usuario:
                Login.hide()
                if usuario[2] == 1:
                    self.log_in.Ventana1 = QtWidgets.QMainWindow()
                    self.log_in.ui = Ui_MenuAdminGeneral()
                    self.log_in.ui.setupUi(self.log_in.Ventana1)
                    self.log_in.Ventana1.show()  
                elif usuario[2] == 2:
                    self.log_in.Ventana2 = QtWidgets.QMainWindow()
                    self.log_in.ui = Ui_MenuAdminLocal()
                    self.log_in.ui.setupUi(self.log_in.Ventana2,usuario[4])
                    self.log_in.Ventana2.show()
                elif usuario[2] == 3:
                    self.log_in.Ventana3 = QtWidgets.QMainWindow()
                    self.log_in.ui = LoginMesero()
                    self.log_in.ui.setupUi(self.log_in.Ventana3)
                    self.log_in.Ventana3.show()
                elif usuario[2] == 5:
                    self.log_in.Ventana4 = QtWidgets.QMainWindow()
                    self.log_in.ui = Ui_cocinero()
                    self.log_in.ui.setupUi(self.log_in.Ventana4)
                    self.log_in.Ventana4.show()
            else:
                mensaje = QMessageBox()
                mensaje.setWindowTitle("Aviso")
                mensaje.setText("Usuario y/o Contraseña Incorrectos")
                mensaje.setIcon(QMessageBox.Warning)
                mensaje.setStandardButtons(QMessageBox.Ok)
                mensaje.setDefaultButton(QMessageBox.Ok)
                mensaje.exec_()