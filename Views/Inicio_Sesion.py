import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from controllers.LoginController import *
from PyQt5 import QtCore, QtGui, QtWidgets
from Views.AdminGeneral.MenuAdminGeneral import Ui_MenuAdminGeneral
from Views.AdminLocal.MenuAdminLocal import Ui_MenuAdminLocal
from Views.Mesero.MenuMesero import Ui_Mesero
from Views.Cocinero.vistafinal import Ui_cocinero

class Ui_Login(object):
    
    def __init__(self):
        self.loginController = loginController(self)
    
    def setupUi(self, Login):
        #DEFINICION DE VARIABLE QUE LLAMA A LA MISMA VENTANA (CON SELF) PARA PODER UTILIZARLA EN FUNCIONES 
        self.Login = Login
        
        Login.setObjectName("Login")
        Login.setWindowModality(QtCore.Qt.ApplicationModal)
        
        #TAMAÑO DE LA VENTANA NO EDITABLE
        Login.setFixedSize(325,453)
        
        #AGREGAR ICONO DE LA VENTANA
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\./images/image_Emp.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Login.setWindowIcon(icon)
        
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        
        #CREACION DE IMAGEN (INICIO SESION) CON LABEL
        self.Imagen = QtWidgets.QLabel(self.centralwidget)
        self.Imagen.setGeometry(QtCore.QRect(60, 20, 241, 241))
        self.Imagen.setText("")
        self.Imagen.setPixmap(QtGui.QPixmap(".\\./images/aym_ico_user.ico"))
        self.Imagen.setObjectName("Imagen")
        
        self.btnInicioSesion = QtWidgets.QPushButton(self.centralwidget)
        self.btnInicioSesion.setGeometry(QtCore.QRect(210, 400, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        
        #CREACION DE BOTON INICIO SESION
        self.btnInicioSesion.setFont(font)
        self.btnInicioSesion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnInicioSesion.setObjectName("btnInicioSesion")
        #CREACION DE ACCION AL PULSAR BOTON "INICIAR SESION"
        self.btnInicioSesion.clicked.connect(self.accionAceptar)
        
        self.titleUsuario = QtWidgets.QLabel(self.centralwidget)
        self.titleUsuario.setGeometry(QtCore.QRect(60, 300, 71, 21)) 
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.titleUsuario.setFont(font)
        self.titleUsuario.setObjectName("titleUsuario")
        self.titleContrasena = QtWidgets.QLabel(self.centralwidget)
        self.titleContrasena.setGeometry(QtCore.QRect(30, 350, 111, 21))
        
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.titleContrasena.setFont(font)
        self.titleContrasena.setObjectName("titleContrasena")
        self.Usuario = QtWidgets.QLineEdit(self.centralwidget)
        self.Usuario.setGeometry(QtCore.QRect(140, 300, 161, 20))
        self.Usuario.setObjectName("Usuario")
        self.Contrasena = QtWidgets.QLineEdit(self.centralwidget)
        self.Contrasena.setGeometry(QtCore.QRect(140, 350, 161, 20))
        self.Contrasena.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Contrasena.setObjectName("Contrasena")
        Login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)
        
        
    #CREACION DE FUNCIONES
    def accionAceptar(self):
        self.loginController.logIn(self.Usuario.text(),self.Contrasena.text(),Ui_MenuAdminGeneral,Ui_MenuAdminLocal,Ui_Mesero,Ui_cocinero,self.Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Foud Court"))
        self.btnInicioSesion.setText(_translate("Login", "Iniciar Sesion"))
        self.titleUsuario.setText(_translate("Login", "Usuario:"))
        self.titleContrasena.setText(_translate("Login", "Contraseña:"))
        self.Usuario.setPlaceholderText(_translate("Login", "Ingrese su Usuario"))
        self.Contrasena.setPlaceholderText(_translate("Login", "Ingrese la Contraseña"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
