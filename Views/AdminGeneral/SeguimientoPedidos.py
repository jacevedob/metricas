import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from controllers.AdminGeneral.SegumientoController import SeguimientoController

class Ui_seguimientoPedido(object):
    
    def __init__(self):
        self.seguimiento_controller = SeguimientoController(self)
    
    def setupUi(self, Seguimiento):
        #DEFICION DE VARIABLE QUE SE LLAMA A LA MISMA VENTA (SELF)
        self.seguimiento = Seguimiento
        
        Seguimiento.setObjectName("Seguimiento")
        
        #TAMAÑO DE LA VENTAN NO EDITABLE
        Seguimiento.setFixedSize(432, 320)
        
        #AGREGAR ICONO A VENTANA
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/image_Emp.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Seguimiento.setWindowIcon(icon)
        
        self.label = QtWidgets.QLabel(Seguimiento)
        self.label.setGeometry(QtCore.QRect(20, 20, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableSeguimiento = QtWidgets.QTableWidget(Seguimiento)
        self.tableSeguimiento.setGeometry(QtCore.QRect(60, 60, 311, 212))
        self.tableSeguimiento.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableSeguimiento.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableSeguimiento.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableSeguimiento.setObjectName("tableSeguimiento")
        self.tableSeguimiento.setColumnCount(3)
        self.tableSeguimiento.setRowCount(0)
        
        self.seguimiento_controller.listaSeguimiento()
        
        item = QtWidgets.QTableWidgetItem()
        self.tableSeguimiento.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSeguimiento.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSeguimiento.setHorizontalHeaderItem(2, item)
        
        #PONER TABLA NO EDITABLE
        self.tableSeguimiento.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
        self.btnActualizar = QtWidgets.QPushButton(Seguimiento)
        self.btnActualizar.setGeometry(QtCore.QRect(180, 280, 71, 21))
        self.btnActualizar.setObjectName("btnActualizar")
        self.btnActualizar.clicked.connect(self.seguimiento_controller.listaSeguimiento)

        self.retranslateUi(Seguimiento)
        QtCore.QMetaObject.connectSlotsByName(Seguimiento)

    def retranslateUi(self, Seguimiento):
        _translate = QtCore.QCoreApplication.translate
        Seguimiento.setWindowTitle(_translate("Seguimiento", "Foud Court"))
        self.label.setText(_translate("Seguimiento", "SEGUIMIENTO DE PEDIDOS"))
        item = self.tableSeguimiento.horizontalHeaderItem(0)
        item.setText(_translate("Seguimiento", "Mesa"))
        item = self.tableSeguimiento.horizontalHeaderItem(1)
        item.setText(_translate("Seguimiento", "Mesero"))
        item = self.tableSeguimiento.horizontalHeaderItem(2)
        item.setText(_translate("Seguimiento", "Estado"))
        self.btnActualizar.setText(_translate("Seguimiento", "Actualizar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Seguimiento = QtWidgets.QWidget()
    ui = Ui_seguimientoPedido()
    ui.setupUi(Seguimiento)
    Seguimiento.show()
    sys.exit(app.exec_())
