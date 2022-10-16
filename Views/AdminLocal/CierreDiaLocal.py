from PyQt5 import QtCore, QtGui, QtWidgets
from controllers.AdminLocal.CierreDiaLocalController import CierreDiaLocalController

class Ui_CierreDia(object):
    
    def __init__(self):
        self.cierreDiaLocal_controller = CierreDiaLocalController(self)
    
    def setupUi(self, CierreDia, idNegocio):
        self.idNegocio = idNegocio
        self.cierreDia = CierreDia
        CierreDia.setObjectName("CierreDia")
        CierreDia.setFixedSize(521, 411)
        
        #AGREGAR ICONO A LA VENTANA
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/image_Emp.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CierreDia.setWindowIcon(icon)
        
        self.label_8 = QtWidgets.QLabel(CierreDia)
        self.label_8.setGeometry(QtCore.QRect(140, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.widget = QtWidgets.QWidget(CierreDia)
        self.widget.setGeometry(QtCore.QRect(40, 60, 451, 311))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.tableMesa = QtWidgets.QTableWidget(self.widget)
        self.tableMesa.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableMesa.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableMesa.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableMesa.setObjectName("tableMesa")
        
        #PONER TABLA MESA NO EDITABLE
        self.tableMesa.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
        self.tableMesa.setColumnCount(4)
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
        self.cierreDiaLocal_controller.listaMesa(self.idNegocio)
        
        self.gridLayout.addWidget(self.tableMesa, 1, 0, 1, 2)
        self.tableMesero = QtWidgets.QTableWidget(self.widget)
        self.tableMesero.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableMesero.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableMesero.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableMesero.setObjectName("tableMesero")
        
        #PONER TABLA MESERO NO EDITABLE
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
        
        #PONER CIERRE DEL DIA POR MESERO
        self.cierreDiaLocal_controller.listaMesero(self.idNegocio)
        
        self.gridLayout.addWidget(self.tableMesero, 1, 2, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.labelTotalMesa = QtWidgets.QLabel(self.widget)
        self.labelTotalMesa.setText("")
        self.labelTotalMesa.setObjectName("labelTotalMesa")
        
        self.totalVentaDia = self.cierreDiaLocal_controller.total(self.idNegocio)
        
        self.labelTotalMesa.setText(str(self.totalVentaDia))
        
        self.gridLayout.addWidget(self.labelTotalMesa, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 2, 1, 1)
        self.labelTotalMesero = QtWidgets.QLabel(self.widget)
        self.labelTotalMesero.setText("")
        self.labelTotalMesero.setObjectName("labelTotalMesero")
        
        self.labelTotalMesero.setText(str(self.totalVentaDia))
        
        self.gridLayout.addWidget(self.labelTotalMesero, 2, 3, 1, 1)

        self.retranslateUi(CierreDia)
        QtCore.QMetaObject.connectSlotsByName(CierreDia)

    def retranslateUi(self, CierreDia):
        _translate = QtCore.QCoreApplication.translate
        CierreDia.setWindowTitle(_translate("CierreDia", "Foud Court"))
        self.label_8.setText(_translate("CierreDia", "CIERRE DEL DIA"))
        self.label_4.setText(_translate("CierreDia", "Mesa"))
        self.label_3.setText(_translate("CierreDia", "Mesero"))
        item = self.tableMesa.horizontalHeaderItem(0)
        item.setText(_translate("CierreDia", "Mesa"))
        item = self.tableMesa.horizontalHeaderItem(1)
        item.setText(_translate("CierreDia", "Ventas Total"))
        item = self.tableMesero.horizontalHeaderItem(0)
        item.setText(_translate("CierreDia", "Mesero"))
        item = self.tableMesero.horizontalHeaderItem(1)
        item.setText(_translate("CierreDia", "Ventas Total"))
        self.label_6.setText(_translate("CierreDia", "Total:"))
        self.label_7.setText(_translate("CierreDia", "Total:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CierreDia = QtWidgets.QWidget()
    ui = Ui_CierreDia()
    ui.setupUi(CierreDia)
    CierreDia.show()
    sys.exit(app.exec_())
