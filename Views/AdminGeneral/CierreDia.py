import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from controllers.AdminGeneral.CierreDiaController import CierreDiaController

class Ui_cierreDia(object):

    def __init__(self):
        self.cierreDia_controller = CierreDiaController(self)
        
    def setupUi(self, cierreDia):
        self.cierreDia = cierreDia
        cierreDia.setObjectName("cierreDia")

        #TAMAÑO DE LA VENTAN NO EDITABLE
        cierreDia.setFixedSize(703, 417)

        #AGREGAR ICONO A LA VENTANA
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/image_Emp.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        cierreDia.setWindowIcon(icon)
        
        self.label = QtWidgets.QLabel(cierreDia)
        self.label.setGeometry(QtCore.QRect(240, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(cierreDia)
        self.widget.setGeometry(QtCore.QRect(20, 60, 661, 261))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 2)


        self.tableNegocio = QtWidgets.QTableWidget(self.widget)
        self.tableNegocio.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableNegocio.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableNegocio.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableNegocio.setObjectName("tableNegocio")
        
        #PONER TABLA NEGOCIO NO EDITABLE
        self.tableNegocio.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
        self.tableNegocio.setColumnCount(4)
        self.tableNegocio.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableNegocio.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableNegocio.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableNegocio.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableNegocio.setHorizontalHeaderItem(3, item)

        #PONER CIERRE DEL DIA POR NEGOCIO
        self.cierreDia_controller.listaNegocios()

        self.gridLayout.addWidget(self.tableNegocio, 1, 0, 1, 2)
        self.tableMesa = QtWidgets.QTableWidget(self.widget)
        self.tableMesa.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableMesa.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableMesa.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableMesa.setObjectName("tableMesa")
        self.tableMesa.setColumnCount(4)
        
        #PONER TABLA MESA NO EDITABLE
        self.tableMesa.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
        self.tableMesa.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableMesa.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableMesa.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableMesa.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableMesa.setHorizontalHeaderItem(3, item)
        
        #PONER CIERRE DEL DIA POR MESAS
        self.cierreDia_controller.listaMesa()
        
        self.gridLayout.addWidget(self.tableMesa, 1, 2, 1, 2)

        self.tableMesero = QtWidgets.QTableWidget(self.widget)
        self.tableMesero.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableMesero.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableMesero.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableMesero.setObjectName("tableMesero")
        
        #PONER TABLA MESERO NO EDITBLE
        self.tableMesero.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
        self.tableMesero.setColumnCount(4)
        self.tableMesero.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableMesero.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableMesero.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableMesero.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableMesero.setHorizontalHeaderItem(3, item)
        
        #PONER CIERRE DEL DIA POR MESEROS
        self.cierreDia_controller.listaMesero()
        
        self.gridLayout.addWidget(self.tableMesero, 1, 4, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.labelTotalNegocio = QtWidgets.QLabel(self.widget)
        self.labelTotalNegocio.setText("")
        self.labelTotalNegocio.setObjectName("labelTotalNegocio")
        
        self.totalVentasDia = self.cierreDia_controller.total()
        
        self.labelTotalNegocio.setText(str(self.totalVentasDia))
        
        self.gridLayout.addWidget(self.labelTotalNegocio, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)
        self.labelTotalMesa = QtWidgets.QLabel(self.widget)
        self.labelTotalMesa.setText("")
        self.labelTotalMesa.setObjectName("labelTotalMesa")
        
        self.labelTotalMesa.setText(str(self.totalVentasDia))
        
        self.gridLayout.addWidget(self.labelTotalMesa, 2, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 4, 1, 1)
        self.labelTotalMesero = QtWidgets.QLabel(self.widget)
        self.labelTotalMesero.setText("")
        self.labelTotalMesero.setObjectName("labelTotalMesero")
        
        self.labelTotalMesero.setText(str(self.totalVentasDia))
        
        self.gridLayout.addWidget(self.labelTotalMesero, 2, 5, 1, 1)

        self.retranslateUi(cierreDia)
        QtCore.QMetaObject.connectSlotsByName(cierreDia)

    def retranslateUi(self, cierreDia):
        _translate = QtCore.QCoreApplication.translate
        cierreDia.setWindowTitle(_translate("cierreDia", "Foud Court"))
        self.label.setText(_translate("cierreDia", "CIERRE DEL DIA"))
        self.label_2.setText(_translate("cierreDia", "Negocio"))
        self.label_4.setText(_translate("cierreDia", "Mesa"))
        self.label_3.setText(_translate("cierreDia", "Mesero"))
        item = self.tableNegocio.horizontalHeaderItem(0)
        item.setText(_translate("cierreDia", "Negocio"))
        item = self.tableNegocio.horizontalHeaderItem(1)
        item.setText(_translate("cierreDia", "Ventas Total"))
        item = self.tableMesa.horizontalHeaderItem(0)
        item.setText(_translate("cierreDia", "Mesa"))
        item = self.tableMesa.horizontalHeaderItem(1)
        item.setText(_translate("cierreDia", "Ventas Total"))
        item = self.tableMesero.horizontalHeaderItem(0)
        item.setText(_translate("cierreDia", "Mesero"))
        item = self.tableMesero.horizontalHeaderItem(1)
        item.setText(_translate("cierreDia", "Ventas Total"))
        self.label_5.setText(_translate("cierreDia", "Total:"))
        self.label_6.setText(_translate("cierreDia", "Total:"))
        self.label_7.setText(_translate("cierreDia", "Total:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cierreDia = QtWidgets.QWidget()
    ui = Ui_cierreDia()
    ui.setupUi(cierreDia)
    cierreDia.show()
    sys.exit(app.exec_())
