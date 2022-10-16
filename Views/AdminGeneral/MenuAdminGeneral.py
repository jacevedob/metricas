import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from controllers.AdminGeneral.MenuAdminGeneralController import MenuAdminGeneralController
from PyQt5 import QtCore, QtGui, QtWidgets
from Views.AdminGeneral.CRUDempleados import Ui_Empleados
from Views.AdminGeneral.CRUDnegocios import Ui_Negocios
from Views.AdminGeneral.CierreDia import Ui_cierreDia
from Views.AdminGeneral.SeguimientoPedidos import Ui_seguimientoPedido

class Ui_MenuAdminGeneral(object):
    
    def __init__(self):
        self.adminGeneral_Controller = MenuAdminGeneralController(self)
    
    def setupUi(self, MenuAdminGeneral):
        #DEFINICION DE VARIABLE QUE LLAMA A LA MISMA VENTANA (CON SELF) PARA PODER UTILIZARLA EN FUNCIONES 
        self.menuAdminGeneral = MenuAdminGeneral
        
        MenuAdminGeneral.setObjectName("MenuAdminGeneral")
        
        #TAMAÑO DE LA VENTANA NO EDITABLE
        MenuAdminGeneral.setFixedSize(223,326)
        
        #AGREGAR ICONO DE LA VENTANA
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/image_Emp.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MenuAdminGeneral.setWindowIcon(icon)
        
        self.centralwidget = QtWidgets.QWidget(MenuAdminGeneral)
        self.centralwidget.setObjectName("centralwidget")
        
        #CREACION DE BOTON EMPLEADOS
        self.btnEmpleados = QtWidgets.QPushButton(self.centralwidget)
        self.btnEmpleados.setGeometry(QtCore.QRect(30, 20, 161, 51))
        self.btnEmpleados.setObjectName("btnEmpleados")
        #CREACION DE ACCION PULSAR "EMPLEADOS"
        self.btnEmpleados.clicked.connect(self.accionEmpleados)
        
        #CREACION DE BOTON NEGOCIOS
        self.btnNegocios = QtWidgets.QPushButton(self.centralwidget)
        self.btnNegocios.setGeometry(QtCore.QRect(30, 90, 161, 51))
        self.btnNegocios.setObjectName("btnNegocios")
        #CREACION ACCION BOTON "NEGOCIOS"
        self.btnNegocios.clicked.connect(self.accionNegocios)
        
        #CREACION DE BOTON PEDIDOS
        self.btnPedidos = QtWidgets.QPushButton(self.centralwidget)
        self.btnPedidos.setGeometry(QtCore.QRect(30, 160, 161, 51))
        self.btnPedidos.setObjectName("btnPedidos")
        #CREACION ACCION BOTON "PEDIDOS"
        self.btnPedidos.clicked.connect(self.accionSeguimiento)
        
        #CREACION DE BOTON CIERRE
        self.btnCierre = QtWidgets.QPushButton(self.centralwidget)
        self.btnCierre.setGeometry(QtCore.QRect(30, 230, 161, 51))
        self.btnCierre.setObjectName("btnCierre")
        #CREACION ACCION BOTON "CIERRE"
        self.btnCierre.clicked.connect(self.accionCierreDia)
        
        MenuAdminGeneral.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MenuAdminGeneral)
        self.statusbar.setObjectName("statusbar")
        MenuAdminGeneral.setStatusBar(self.statusbar)
        self.actionAgregar = QtWidgets.QAction(MenuAdminGeneral)
        self.actionAgregar.setObjectName("actionAgregar")

        self.retranslateUi(MenuAdminGeneral)
        QtCore.QMetaObject.connectSlotsByName(MenuAdminGeneral)
    
    #----------------CREACION DE EVENTOS----------------------------------------------------#
    def accionEmpleados(self):
        self.adminGeneral_Controller.ventanaCRUDempleados(Ui_Empleados,self.menuAdminGeneral)
        
    def accionNegocios(self):
        self.adminGeneral_Controller.ventanaCRUDnegocios(Ui_Negocios,self.menuAdminGeneral)
    
    def accionSeguimiento(self):
        self.adminGeneral_Controller.ventanaSeguimientoPedidos(Ui_seguimientoPedido)
    
    def accionCierreDia(self):
        self.adminGeneral_Controller.ventanaCierreDia(Ui_cierreDia)
    #---------------------------------------------------------------------------------------#
    
    def retranslateUi(self, MenuAdminGeneral):
        _translate = QtCore.QCoreApplication.translate
        MenuAdminGeneral.setWindowTitle(_translate("MenuAdminGeneral", "Foud Court"))
        self.btnEmpleados.setText(_translate("MenuAdminGeneral", "Empleados"))
        self.btnNegocios.setText(_translate("MenuAdminGeneral", "Negocios"))
        self.btnPedidos.setText(_translate("MenuAdminGeneral", "Segimiento de Pedidos"))
        self.btnCierre.setText(_translate("MenuAdminGeneral", "Cierre del Dia"))
        self.actionAgregar.setText(_translate("MenuAdminGeneral", "Agregar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MenuAdminGeneral = QtWidgets.QMainWindow()
    ui = Ui_MenuAdminGeneral()
    ui.setupUi(MenuAdminGeneral)
    MenuAdminGeneral.show()
    sys.exit(app.exec_())
