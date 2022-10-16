import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from controllers.AdminLocal.CrearProductoController import CrearProductoController
from Models.Negocio import Negocios

class Ui_CrearProducto(object):
    
    def __init__(self):
        self.crearProducto_Controller = CrearProductoController(self)
    
    def setupUi(self, CrearProducto):
        #DEFINICION DE VARIABLE QUE LLAMA A LA MISMA VENTANA (CON SELF) PARA PODER UTILIZARLA EN FUNCIONES 
        self.crearProducto = CrearProducto
        
        CrearProducto.setObjectName("CrearProducto")
        
        #TAMAÑO DE LA VENTANA NO EDITABLE 
        CrearProducto.setFixedSize(333,307)
        
        #AGREGAR ICONO A LA VENTANA
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/image_Emp.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CrearProducto.setWindowIcon(icon)

        self.widget = QtWidgets.QWidget(CrearProducto)
        self.widget.setGeometry(QtCore.QRect(30, 20, 271, 261))
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.InputNombre = QtWidgets.QLineEdit(self.widget)
        self.InputNombre.setObjectName("InputNombre")
        self.gridLayout_2.addWidget(self.InputNombre, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.InputDescripcion = QtWidgets.QLineEdit(self.widget)
        self.InputDescripcion.setObjectName("InputDescripcion")
        self.gridLayout_2.addWidget(self.InputDescripcion, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.InputPrecio = QtWidgets.QLineEdit(self.widget)
        self.InputPrecio.setObjectName("InputPrecio")
        self.gridLayout_2.addWidget(self.InputPrecio, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)
        self.comboBoxNegocio = QtWidgets.QComboBox(self.widget)
        self.comboBoxNegocio.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBoxNegocio.setObjectName("comboBoxNegocio")
        
        #PONER NEGOCIOS DE BASE DE DATOS EN COMBOBOX
        self.listaNegocios = Negocios.readNegocios(self)
        for negocio in self.listaNegocios:
            itemNegocio = negocio[1]
            self.comboBoxNegocio.addItem(itemNegocio)
        
        self.gridLayout_2.addWidget(self.comboBoxNegocio, 3, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        
        #CREACION BOTON CANCELAR
        self.btnCancelar = QtWidgets.QPushButton(self.widget)
        self.btnCancelar.setObjectName("btnCancelar")
        #CREACION ACCION #"CANCELAR"
        self.btnCancelar.clicked.connect(self.accionCancelar)    
        self.gridLayout.addWidget(self.btnCancelar, 0, 1, 1, 1)
        
        #CREACION BOTON CREAR
        self.btnCrear = QtWidgets.QPushButton(self.widget)
        self.btnCrear.setObjectName("btnCrear")
        #CREACION ACCION "CREAR"
        self.btnCrear.clicked.connect(self.accionCrear)
        self.gridLayout.addWidget(self.btnCrear, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 2, 0, 1, 1)

        self.retranslateUi(CrearProducto)
        QtCore.QMetaObject.connectSlotsByName(CrearProducto)

    def accionCrear(self):
        self.nombre = self.InputNombre.text()
        self.desc = self.InputDescripcion.text()
        self.precio = self.InputPrecio.text()
        
        self.nomNeg = self.comboBoxNegocio.itemText(self.comboBoxNegocio.currentIndex())
        for negocio in self.listaNegocios:
            if negocio[1] == self.nomNeg:
                self.idNeg = negocio[0]
        self.crearProducto_Controller.crearProducto(self.nombre,self.desc,self.precio,self.idNeg,self.crearProducto)

    def accionCancelar(self):
        self.crearProducto.close()

    def retranslateUi(self, CrearProducto):
        _translate = QtCore.QCoreApplication.translate
        CrearProducto.setWindowTitle(_translate("CrearProducto", "Foud Court"))
        self.label.setText(_translate("CrearProducto", "Crear Nuevo Producto"))
        self.label_2.setText(_translate("CrearProducto", "Nombre: "))
        self.InputNombre.setPlaceholderText(_translate("CrearProducto", "Nombre del Producto"))
        self.label_3.setText(_translate("CrearProducto", "Descripción:"))
        self.InputDescripcion.setPlaceholderText(_translate("CrearProducto", "Descripción"))
        self.label_4.setText(_translate("CrearProducto", "Precio:"))
        self.InputPrecio.setPlaceholderText(_translate("CrearProducto", "Precio"))
        self.label_6.setText(_translate("CrearProducto", "Negocio:"))
        self.btnCancelar.setText(_translate("CrearProducto", "Cancelar"))
        self.btnCrear.setText(_translate("CrearProducto", "Crear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CrearProducto = QtWidgets.QWidget()
    ui = Ui_CrearProducto()
    ui.setupUi(CrearProducto)
    CrearProducto.show()
    sys.exit(app.exec_())
