import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from controllers.AdminLocal.SeguimientoPedidoLocalController import SeguimientoPedidoLocalController

class Ui_SeguiminetoPedido(object):
    
    def __init__(self):
        self.seguimientoLocal_Controller = SeguimientoPedidoLocalController(self)
    
    def setupUi(self, SeguiminetoPedido, idNegocio):
        self.idNegocio = idNegocio
        SeguiminetoPedido.setObjectName("SeguiminetoPedido")
        SeguiminetoPedido.setFixedSize(431, 320)
        
        #AGREGAR ICONO DE LA VENTANA
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/image_Emp.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SeguiminetoPedido.setWindowIcon(icon)
        
        self.label = QtWidgets.QLabel(SeguiminetoPedido)
        self.label.setGeometry(QtCore.QRect(20, 20, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableSeguimiento = QtWidgets.QTableWidget(SeguiminetoPedido)
        self.tableSeguimiento.setGeometry(QtCore.QRect(60, 60, 311, 212))
        self.tableSeguimiento.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableSeguimiento.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableSeguimiento.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableSeguimiento.setObjectName("tableSeguimiento")
        self.tableSeguimiento.setColumnCount(3)
        self.tableSeguimiento.setRowCount(0)
        
        self.seguimientoLocal_Controller.listaSeguimiento(self.idNegocio)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableSeguimiento.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSeguimiento.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSeguimiento.setHorizontalHeaderItem(2, item)
        
        #TABLA NO EDITABLE
        self.tableSeguimiento.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
        self.btnActualizar = QtWidgets.QPushButton(SeguiminetoPedido)
        self.btnActualizar.setGeometry(QtCore.QRect(170, 280, 71, 21))
        self.btnActualizar.setObjectName("btnActualizar")
        self.btnActualizar.clicked.connect(self.seguimientoLocal_Controller.listaSeguimiento)
        self.retranslateUi(SeguiminetoPedido)
        QtCore.QMetaObject.connectSlotsByName(SeguiminetoPedido)

    def retranslateUi(self, SeguiminetoPedido):
        _translate = QtCore.QCoreApplication.translate
        SeguiminetoPedido.setWindowTitle(_translate("SeguiminetoPedido", "Foud Court"))
        self.label.setText(_translate("SeguiminetoPedido", "SEGUIMIENTO DE PEDIDOS"))
        item = self.tableSeguimiento.horizontalHeaderItem(0)
        item.setText(_translate("SeguiminetoPedido", "Mesa"))
        item = self.tableSeguimiento.horizontalHeaderItem(1)
        item.setText(_translate("SeguiminetoPedido", "Mesero"))
        item = self.tableSeguimiento.horizontalHeaderItem(2)
        item.setText(_translate("SeguiminetoPedido", "Estado"))
        self.btnActualizar.setText(_translate("SeguiminetoPedido", "Actualizar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SeguiminetoPedido = QtWidgets.QWidget()
    ui = Ui_SeguiminetoPedido()
    ui.setupUi(SeguiminetoPedido)
    SeguiminetoPedido.show()
    sys.exit(app.exec_())
