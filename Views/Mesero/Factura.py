import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from controllers.Mesero.FacturaController import facturaController
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_facturas(object):
    def __init__(self):
        self.FacturaController = facturaController(self)

    def setupUi(self, facturas):
        facturas.setObjectName("facturas")
        facturas.setFixedSize(550, 521)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/image_Emp.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        facturas.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(facturas)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 50, 525, 431))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.table_factura = QtWidgets.QTableWidget(self.layoutWidget)
        self.table_factura.setRowCount(10)
        self.table_factura.setObjectName("table_factura")
        self.table_factura.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.table_factura.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_factura.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_factura.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_factura.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_factura.setHorizontalHeaderItem(4, item)
        self.gridLayout.addWidget(self.table_factura, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        facturas.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(facturas)
        self.statusbar.setObjectName("statusbar")
        facturas.setStatusBar(self.statusbar)

        self.retranslateUi(facturas)
        QtCore.QMetaObject.connectSlotsByName(facturas)
        self.l = self.pushButton.clicked.connect(lambda:self.FacturaController.listPedidos())

    def retranslateUi(self, facturas):
        _translate = QtCore.QCoreApplication.translate
        facturas.setWindowTitle(_translate("facturas", "Foud Court"))
        self.label.setText(_translate("facturas", "Facturas"))
        item = self.table_factura.horizontalHeaderItem(0)
        item.setText(_translate("facturas", "ID Pedido"))
        item = self.table_factura.horizontalHeaderItem(1)
        item.setText(_translate("facturas", "Mesero"))
        item = self.table_factura.horizontalHeaderItem(2)
        item.setText(_translate("facturas", "Mesa"))
        item = self.table_factura.horizontalHeaderItem(3)
        item.setText(_translate("facturas", "Fecha"))
        item = self.table_factura.horizontalHeaderItem(4)
        item.setText(_translate("facturas", "Total"))
        self.pushButton.setText(_translate("facturas", "Facturas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    facturas = QtWidgets.QMainWindow()
    ui = Ui_facturas()
    ui.setupUi(facturas)
    facturas.show()
    sys.exit(app.exec_())
