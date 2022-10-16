import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets

class MenuAdminLocalController():
    
    def __init__(self, MenuLocal) -> None:
        self.menuLocal = MenuLocal
    
    def ventanaCRUDproductos(self, Ui_Productos, MenuAdminLocal):
        self.menuLocal.Ventana = QtWidgets.QMainWindow()
        self.menuLocal.ui = Ui_Productos()
        self.menuLocal.ui.setupUi(self.menuLocal.Ventana,MenuAdminLocal)
        MenuAdminLocal.hide()
        self.menuLocal.Ventana.show()
        
    def ventanaSeguimientoPedidosLocal(self, Ui_SeguimientoLocal, idNegocio):
        self.menuLocal.Form = QtWidgets.QWidget()
        self.menuLocal.ui = Ui_SeguimientoLocal()
        self.menuLocal.ui.setupUi(self.menuLocal.Form,idNegocio)
        self.menuLocal.Form.show()
        
    def ventanaCierreDiaLocal(self, Ui_CierreDia, idNegocio):
        self.menuLocal.Form = QtWidgets.QWidget()
        self.menuLocal.ui = Ui_CierreDia()
        self.menuLocal.ui.setupUi(self.menuLocal.Form,idNegocio)
        self.menuLocal.Form.show()