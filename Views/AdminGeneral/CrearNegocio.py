import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from controllers.AdminGeneral.CrearNegocioController import CrearNegocioController
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_crearNegocio(object):
    
    def __init__(self):
        self.crearNegocio_Controller = CrearNegocioController(self)
        
    def setupUi(self, crearNegocio):
        #DEFINICION DE VARIABLE QUE LLAMA A LA MISMA VENTANA (CON SELF) PARA PODER UTILIZARLA EN FUNCIONES 
        self.crearNegocio = crearNegocio
        
        crearNegocio.setObjectName("crearNegocio")
        
        #TAMAÑO DE LA VENTANA NO EDITABLE
        crearNegocio.setFixedSize(334, 307)
        
        #AGREGAR ICONO A LA VENTANA
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/image_Emp.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        crearNegocio.setWindowIcon(icon)
        
        
        self.label = QtWidgets.QLabel(crearNegocio)
        self.label.setGeometry(QtCore.QRect(40, 10, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(crearNegocio)
        self.widget.setGeometry(QtCore.QRect(50, 70, 251, 201))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        
        #INGRESAR EL NOMBRE NEGOCIO
        self.inputNombre = QtWidgets.QLineEdit(self.widget)
        self.inputNombre.setObjectName("inputNombre")
        self.gridLayout.addWidget(self.inputNombre, 0, 1, 1, 1)
        
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        
        #INGRESAR EL ESTILO DE COMIDA
        self.inputEstilo = QtWidgets.QLineEdit(self.widget)
        self.inputEstilo.setObjectName("inputEstilo")
        self.gridLayout.addWidget(self.inputEstilo, 1, 1, 1, 1)
        
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        
        #INGRESAR EL RUT
        self.inputRut = QtWidgets.QLineEdit(self.widget)
        self.inputRut.setObjectName("inputRut")
        self.gridLayout.addWidget(self.inputRut, 2, 1, 1, 1)
        
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)
        
        #CREACION BOTON CREAR
        self.btnCrear = QtWidgets.QPushButton(self.widget)
        self.btnCrear.setObjectName("btnCrear")
        #CREACION ACCION "CREAR"
        self.btnCrear.clicked.connect(self.accionCrear)
        self.gridLayout_2.addWidget(self.btnCrear, 1, 0, 1, 1)
        
        #CREACION BOTON CANCELAR
        self.btnCancelar = QtWidgets.QPushButton(self.widget)
        self.btnCancelar.setObjectName("btnCancelar")
        #CREACION ACCCION "CANCELAR"
        self.btnCancelar.clicked.connect(self.accionCancelar)
        self.gridLayout_2.addWidget(self.btnCancelar, 1, 1, 1, 1)

        self.retranslateUi(crearNegocio)
        QtCore.QMetaObject.connectSlotsByName(crearNegocio)
        
    def accionCrear(self):
        self.nombre = self.inputNombre.text()
        self.estilo = self.inputEstilo.text()
        self.rut = int(self.inputRut.text())
        self.crearNegocio_Controller.crearNegocio(self.nombre,self.estilo,self.rut,self.crearNegocio)

    def accionCancelar(self):
        self.crearNegocio.close()

    def retranslateUi(self, crearNegocio):
        _translate = QtCore.QCoreApplication.translate
        crearNegocio.setWindowTitle(_translate("crearNegocio", "Foud Court"))
        self.label.setText(_translate("crearNegocio", "Crear Nuevo Negocio"))
        self.label_2.setText(_translate("crearNegocio", "Nombre: "))
        self.inputNombre.setPlaceholderText(_translate("crearNegocio", "Nombre del Negocio"))
        self.label_3.setText(_translate("crearNegocio", "Estilo de Comida:"))
        self.inputEstilo.setPlaceholderText(_translate("crearNegocio", "Estilo"))
        self.label_4.setText(_translate("crearNegocio", "Rut:"))
        self.inputRut.setPlaceholderText(_translate("crearNegocio", "Rut"))
        self.btnCrear.setText(_translate("crearNegocio", "Crear"))
        self.btnCancelar.setText(_translate("crearNegocio", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    crearNegocio = QtWidgets.QWidget()
    ui = Ui_crearNegocio()
    ui.setupUi(crearNegocio)
    crearNegocio.show()
    sys.exit(app.exec_())
