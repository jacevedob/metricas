import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from controllers.AdminLocal.MenuAdminLocalController import MenuAdminLocalController
from Views.AdminLocal.CRUDproductos import Ui_Productos
from Views.AdminLocal.SeguimientoPedidosLocal import Ui_SeguiminetoPedido
from Views.AdminLocal.CierreDiaLocal import Ui_CierreDia

class Ui_MenuAdminLocal(object):
    
    def __init__(self):
        self.adminLocal_Conroller = MenuAdminLocalController(self)
    
    def setupUi(self, MenuAdminLocal, id_negocio):
        #DEFINICION DE VARIABLE QUE LLAMA A LA MISMA VENTANA (CON SELF) PARA PODER UTILIZARLA EN FUNCIONES 
        self.menuAdminLocal = MenuAdminLocal
        
        self.idNegocio = id_negocio
        
        MenuAdminLocal.setObjectName("MenuAdminLocal")
        
        #TAMAÑO DE LA VENTANA NO EDITABLE
        MenuAdminLocal.setFixedSize(202,254)

        #AGREGAR ICONO DE LA VENTANA
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/image_Emp.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MenuAdminLocal.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(MenuAdminLocal)
        self.centralwidget.setObjectName("centralwidget")
        
        #CREACION BOTON CIERRE
        self.btnCierre = QtWidgets.QPushButton(self.centralwidget)
        self.btnCierre.setGeometry(QtCore.QRect(20, 160, 161, 51))
        self.btnCierre.setObjectName("btnCierre")
        #CREACION ACCION "CIERRE"
        self.btnCierre.clicked.connect(self.accionCierreDiaLocal)
        
        #CREACION BOTON PRODUCTOS
        self.btnProductos = QtWidgets.QPushButton(self.centralwidget)
        self.btnProductos.setGeometry(QtCore.QRect(20, 20, 161, 51))
        self.btnProductos.setObjectName("btnProductos")
        #CREACION ACCION "PRODUCTOS"
        self.btnProductos.clicked.connect(self.accionProductos)
        
        #CREACION BOTON SEGUIMIENTO
        self.btnSeguimiento = QtWidgets.QPushButton(self.centralwidget)
        self.btnSeguimiento.setGeometry(QtCore.QRect(20, 90, 161, 51))
        self.btnSeguimiento.setObjectName("btnSeguimiento")
        #CREACION ACCION "SEGUIMIENTO"
        self.btnSeguimiento.clicked.connect(self.accionSeguimiento)
        MenuAdminLocal.setCentralWidget(self.centralwidget)

        self.retranslateUi(MenuAdminLocal)
        QtCore.QMetaObject.connectSlotsByName(MenuAdminLocal)
        
    #-------------------CREACION DE EVENTOS------------------------------#
    def accionProductos(self):
        self.adminLocal_Conroller.ventanaCRUDproductos(Ui_Productos,self.menuAdminLocal)
        
    def accionSeguimiento(self):
        self.adminLocal_Conroller.ventanaSeguimientoPedidosLocal(Ui_SeguiminetoPedido,self.idNegocio)
        
    def accionCierreDiaLocal(self):
        self.adminLocal_Conroller.ventanaCierreDiaLocal(Ui_CierreDia,self.idNegocio)

    def retranslateUi(self, MenuAdminLocal):
        _translate = QtCore.QCoreApplication.translate
        MenuAdminLocal.setWindowTitle(_translate("MenuAdminLocal", "Foud Court"))
        self.btnCierre.setText(_translate("MenuAdminLocal", "Cierre del Dia"))
        self.btnProductos.setText(_translate("MenuAdminLocal", "Productos"))
        self.btnSeguimiento.setText(_translate("MenuAdminLocal", "Seguimiento de Pedidos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MenuAdminLocal = QtWidgets.QMainWindow()
    ui = Ui_MenuAdminLocal()
    ui.setupUi(MenuAdminLocal)
    MenuAdminLocal.show()
    sys.exit(app.exec_())
