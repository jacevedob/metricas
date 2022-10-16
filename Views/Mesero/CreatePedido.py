import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from controllers.Mesero.CreatePedidoController import CreatePedidoController
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CreatePedido(object):
    def __init__(self):
        self.create_pedido_controller = CreatePedidoController(self)

    def setupUi(self, CreatePedido):
        CreatePedido.setObjectName("CreatePedido")
        CreatePedido.setFixedSize(588, 401)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/image_Emp.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CreatePedido.setWindowIcon(icon)
        self.layoutWidget = QtWidgets.QWidget(CreatePedido)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 30, 411, 303))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_create = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_create.setFont(font)
        self.btn_create.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_create.setObjectName("btn_create")
        self.gridLayout.addWidget(self.btn_create, 8, 0, 1, 4)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)
        self.input_producto = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_producto.setFont(font)
        self.input_producto.setText("")
        self.input_producto.setObjectName("input_producto")
        self.gridLayout.addWidget(self.input_producto, 6, 3, 1, 1)
        self.input_cantidad = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_cantidad.setFont(font)
        self.input_cantidad.setText("")
        self.input_cantidad.setObjectName("input_cantidad")
        self.gridLayout.addWidget(self.input_cantidad, 7, 2, 1, 2)
        self.input_mesa = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_mesa.setFont(font)
        self.input_mesa.setText("")
        self.input_mesa.setObjectName("input_mesa")
        self.gridLayout.addWidget(self.input_mesa, 5, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 3)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 2)
        self.input_pedido = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_pedido.setFont(font)
        self.input_pedido.setText("")
        self.input_pedido.setObjectName("input_pedido")
        self.gridLayout.addWidget(self.input_pedido, 2, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 3)
        self.input_mesero = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_mesero.setFont(font)
        self.input_mesero.setText("")
        self.input_mesero.setObjectName("input_mesero")
        self.gridLayout.addWidget(self.input_mesero, 3, 3, 1, 1)
        self.input_pedido_2 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_pedido_2.setFont(font)
        self.input_pedido_2.setText("")
        self.input_pedido_2.setObjectName("input_pedido_2")
        self.gridLayout.addWidget(self.input_pedido_2, 1, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 3)

        self.retranslateUi(CreatePedido)
        QtCore.QMetaObject.connectSlotsByName(CreatePedido)

        self.x = self.btn_create.clicked.connect(lambda:self.create_pedido_controller.createPedido(self.input_pedido_2.text(),self.input_pedido.text(), self.input_mesero.text(),self.input_mesa.text(),self.input_producto.text(),int(self.input_cantidad.text()),CreatePedido))


    def retranslateUi(self, CreatePedido):
        _translate = QtCore.QCoreApplication.translate
        CreatePedido.setWindowTitle(_translate("CreatePedido", "Foud Court"))
        self.btn_create.setText(_translate("CreatePedido", "Crear"))
        self.label_4.setText(_translate("CreatePedido", "Cantidad:"))
        self.label_3.setText(_translate("CreatePedido", "Producto:"))
        self.input_producto.setPlaceholderText(_translate("CreatePedido", "ID"))
        self.input_cantidad.setPlaceholderText(_translate("CreatePedido", "Cantidad"))
        self.input_mesa.setPlaceholderText(_translate("CreatePedido", "ID"))
        self.label.setText(_translate("CreatePedido", "Crear Nuevo Pedido"))
        self.label_6.setText(_translate("CreatePedido", "ID Pedido:"))
        self.label_9.setText(_translate("CreatePedido", "ID Negocio :"))
        self.input_pedido.setPlaceholderText(_translate("CreatePedido", "ID"))
        self.label_8.setText(_translate("CreatePedido", "Mesero: "))
        self.input_mesero.setPlaceholderText(_translate("CreatePedido", "ID"))
        self.input_pedido_2.setPlaceholderText(_translate("CreatePedido", "ID"))
        self.label_7.setText(_translate("CreatePedido", "Mesa:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreatePedido = QtWidgets.QWidget()
    ui = Ui_CreatePedido()
    ui.setupUi(CreatePedido)
    CreatePedido.show()
    sys.exit(app.exec_())
