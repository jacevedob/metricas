import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from Models.Negocio import Negocios
from controllers.AdminLocal.ActualizarProductoController import ActualizarProductoController

class Ui_ActualizarProducto(object):
    
    def __init__(self):
        self.actualizarProducto_Crontoller = ActualizarProductoController(self)
    
    def setupUi(self, ActualizarProducto, producto):
        #INSTANCIAR LA VENTANA
        self.actualizarProducto = ActualizarProducto
        
        ActualizarProducto.setObjectName("ActualizarProducto")
        
        #TAMAÑO DE LA VENTANA NO EDITABLE
        ActualizarProducto.setFixedSize(330, 301)
        
        #AGREGAR ICONO A LA VENTANA
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/image_Emp.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ActualizarProducto.setWindowIcon(icon)
        
        self.layoutWidget = QtWidgets.QWidget(ActualizarProducto)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 70, 261, 201))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        #CREACION BOTON CANCELAR
        self.btnCancelar = QtWidgets.QPushButton(self.layoutWidget)
        self.btnCancelar.setObjectName("btnCancelar")
        #CREACION ACCION "CANCELAR"
        self.btnCancelar.clicked.connect(self.accionCancelar)
        self.gridLayout_2.addWidget(self.btnCancelar, 1, 1, 1, 1)
        
        #CREACION BOTON ACTUALIZAR
        self.btnActualizar = QtWidgets.QPushButton(self.layoutWidget)
        self.btnActualizar.setObjectName("btnActualizar")
        #CREACION ACCION "ACTUALIZAR"
        self.btnActualizar.clicked.connect(self.accionActualizar)
        self.gridLayout_2.addWidget(self.btnActualizar, 1, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.InputPrecioAc = QtWidgets.QLineEdit(self.layoutWidget)
        self.InputPrecioAc.setObjectName("InputPrecioAc")
        self.gridLayout_3.addWidget(self.InputPrecioAc, 2, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 3, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 1, 0, 1, 1)
        self.InputDescripcionAC = QtWidgets.QLineEdit(self.layoutWidget)
        self.InputDescripcionAC.setObjectName("InputDescripcionAC")
        self.gridLayout_3.addWidget(self.InputDescripcionAC, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)
        self.InputNombreAc = QtWidgets.QLineEdit(self.layoutWidget)
        self.InputNombreAc.setObjectName("InputNombreAc")
        self.gridLayout_3.addWidget(self.InputNombreAc, 0, 1, 1, 1)
        self.comboBoxNegocioAc = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBoxNegocioAc.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBoxNegocioAc.setObjectName("comboBoxNegocioAc")
        self.gridLayout_3.addWidget(self.comboBoxNegocioAc, 3, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 2)
        self.label_7 = QtWidgets.QLabel(ActualizarProducto)
        self.label_7.setGeometry(QtCore.QRect(40, 10, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        
        #PONER DATOS DEL PRODUCTO PREVIOS A LA ACTUALIZACION
        self.InputNombreAc.setText(str(producto[1]))
        self.InputDescripcionAC.setText(str(producto[2]))
        self.InputPrecioAc.setText(str(producto[3]))
        
        #GUARDAR ID DEL PRODUCTO
        self.idProd = str(producto[0])
        
        #PONER NEGOCIOS DE BASE DE DATOS EN COMBOBOX
        self.listaNegocio = Negocios.readNegocios(self)
        for negocio in self.listaNegocio:
            itemNegocio = negocio[1]
            self.comboBoxNegocioAc.addItem(itemNegocio)

        self.retranslateUi(ActualizarProducto)
        QtCore.QMetaObject.connectSlotsByName(ActualizarProducto)

    def accionActualizar(self):
        self.nombre = self.InputNombreAc.text()
        self.descripcion = self.InputDescripcionAC.text()
        self.precio = self.InputPrecioAc.text()
        self.nomNegocio = self.comboBoxNegocioAc.itemText(self.comboBoxNegocioAc.currentIndex())
        for negocio in self.listaNegocio:
            if negocio[1] == self.nomNegocio:
                self.idNegocio = negocio[0]
        self.actualizarProducto_Crontoller.actualizarProducto(self.idProd,self.nombre,self.descripcion,self.precio,self.idNegocio,self.actualizarProducto)
        
    def accionCancelar(self):
        self.actualizarProducto.close()
        
    def retranslateUi(self, ActualizarProducto):
        _translate = QtCore.QCoreApplication.translate
        ActualizarProducto.setWindowTitle(_translate("ActualizarProducto", "Foud Court"))
        self.btnCancelar.setText(_translate("ActualizarProducto", "Cancelar"))
        self.btnActualizar.setText(_translate("ActualizarProducto", "Actualizar"))
        self.InputPrecioAc.setPlaceholderText(_translate("ActualizarProducto", "Precio"))
        self.label_12.setText(_translate("ActualizarProducto", "Negocio:"))
        self.label_9.setText(_translate("ActualizarProducto", "Descripción:"))
        self.InputDescripcionAC.setPlaceholderText(_translate("ActualizarProducto", "Descripción"))
        self.label_8.setText(_translate("ActualizarProducto", "Nombre: "))
        self.InputNombreAc.setPlaceholderText(_translate("ActualizarProducto", "Nombre del Producto"))
        self.label_10.setText(_translate("ActualizarProducto", "Precio:"))
        self.label_7.setText(_translate("ActualizarProducto", "Actualizar Producto"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ActualizarProducto = QtWidgets.QWidget()
    ui = Ui_ActualizarProducto()
    ui.setupUi(ActualizarProducto)
    ActualizarProducto.show()
    sys.exit(app.exec_())
