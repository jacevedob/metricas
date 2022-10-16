import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from controllers.Mesero.MenuMeseroController import LoginMesero
from PyQt5 import QtCore, QtGui, QtWidgets
from Views.Mesero.Pedido import Ui_Pedido
from Views.Mesero.Factura import Ui_facturas

class Ui_Mesero(object):
    def __init__(self):
        self.LoginMesero = LoginMesero(self)

    def setupUi(self, Mesero):
        self.mesero = Mesero
        Mesero.setObjectName("Mesero")
        Mesero.setFixedSize(390, 303)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/image_Emp.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Mesero.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Mesero)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-50, 400, 47, 13))
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(70, 50, 233, 181))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.btn_facturas = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_facturas.setFont(font)
        self.btn_facturas.setObjectName("btn_facturas")
        self.gridLayout.addWidget(self.btn_facturas, 2, 0, 1, 1)
        self.btn_pedidos = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_pedidos.setFont(font)
        self.btn_pedidos.setObjectName("btn_pedidos")
        self.gridLayout.addWidget(self.btn_pedidos, 1, 0, 1, 1)
        Mesero.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Mesero)
        self.statusbar.setObjectName("statusbar")
        Mesero.setStatusBar(self.statusbar)

        self.retranslateUi(Mesero)
        QtCore.QMetaObject.connectSlotsByName(Mesero)
        
        self.p = self.btn_pedidos.clicked.connect(lambda:self.LoginMesero.openPedido(Ui_Pedido))
        self.f = self.btn_facturas.clicked.connect(lambda:self.LoginMesero.openFactura(Ui_facturas))

    def retranslateUi(self, Mesero):
        _translate = QtCore.QCoreApplication.translate
        Mesero.setWindowTitle(_translate("Mesero", "Foud Court"))
        self.label.setText(_translate("Mesero", "TextLabel"))
        self.label_2.setText(_translate("Mesero", "Mesero"))
        self.btn_facturas.setText(_translate("Mesero", "Facturas"))
        self.btn_pedidos.setText(_translate("Mesero", "Pedidos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Mesero = QtWidgets.QMainWindow()
    ui = Ui_Mesero()
    ui.setupUi(Mesero)
    Mesero.show()
    sys.exit(app.exec_())
