import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from controllers.AdminGeneral.CrearEmpleadoController import CrearEmpleadoController
from PyQt5 import QtCore, QtGui, QtWidgets
from Models.Roles import Roles
from Models.Negocio import Negocios

class Ui_CrearEmpleado(object):
    
    def __init__(self):
        self.crearEmpleado_Controller = CrearEmpleadoController(self)
        
    def setupUi(self, CrearEmpleado):
        #DEFINICION DE VARIABLE QUE LLAMA A LA MISMA VENTANA (CON SELF) PARA PODER UTILIZARLA EN FUNCIONES 
        self.crearEmpleado = CrearEmpleado
        
        CrearEmpleado.setObjectName("CrearEmpleado")
        
        #TAMAÑO DE LA VENTANA NO EDITABLE
        CrearEmpleado.setFixedSize(334, 307)
        
        #AGREGAR ICONO A LA VENTANA
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/image_Emp.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CrearEmpleado.setWindowIcon(icon)
        
        self.label = QtWidgets.QLabel(CrearEmpleado)
        self.label.setGeometry(QtCore.QRect(40, 10, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(CrearEmpleado)
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
        self.inputNombre = QtWidgets.QLineEdit(self.widget)
        self.inputNombre.setObjectName("inputNombre")
        self.gridLayout.addWidget(self.inputNombre, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.InputContrasena = QtWidgets.QLineEdit(self.widget)
        self.InputContrasena.setObjectName("InputContrasena")
        self.gridLayout.addWidget(self.InputContrasena, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.inputDoc = QtWidgets.QLineEdit(self.widget)
        self.inputDoc.setObjectName("inputDoc")
        self.gridLayout.addWidget(self.inputDoc, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.comboBoxRol = QtWidgets.QComboBox(self.widget)
        self.comboBoxRol.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBoxRol.setObjectName("comboBoxRol")
        self.gridLayout.addWidget(self.comboBoxRol, 3, 1, 1, 1)
        
        #PONER ROLES DEFINIDOS EN LA BASE DE DATOS EN COMBOBOX
        self.listaRoles = Roles.readRoles(self)
        for rol in self.listaRoles:
            itemRol = rol[1]
            self.comboBoxRol.addItem(itemRol)
        
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.comboBoxNegocio = QtWidgets.QComboBox(self.widget)
        self.comboBoxNegocio.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBoxNegocio.setObjectName("comboBoxNegocio")
        self.gridLayout.addWidget(self.comboBoxNegocio, 4, 1, 1, 1)
        
        #PONER NEGOCIOS DE BASE DE DATOS EN COMBOBOX
        self.listaNegocios = Negocios.readNegocios(self)
        for negocio in self.listaNegocios:
            itemNegocio = negocio[1]
            self.comboBoxNegocio.addItem(itemNegocio)
        
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

        self.retranslateUi(CrearEmpleado)
        QtCore.QMetaObject.connectSlotsByName(CrearEmpleado)
        
    def accionCrear(self):
        self.nombre = self.inputNombre.text()
        self.contra = self.InputContrasena.text()
        self.docu = int(self.inputDoc.text())
        
        self.nomRol = self.comboBoxRol.itemText(self.comboBoxRol.currentIndex())
        for rol in self.listaRoles:
            if rol[1] == self.nomRol:
                self.idRol = rol[0]
                
        self.nomNegocio = self.comboBoxNegocio.itemText(self.comboBoxNegocio.currentIndex())
        for negocio in self.listaNegocios:
            if negocio[1] == self.nomNegocio:
                self.idNegocio = negocio[0]
                
        self.crearEmpleado_Controller.crearEmpleado(self.nombre,self.contra,self.idRol,self.idNegocio,self.docu,self.crearEmpleado)

    def accionCancelar(self):
        self.crearEmpleado.close()

    def retranslateUi(self, CrearEmpleado):
        _translate = QtCore.QCoreApplication.translate
        CrearEmpleado.setWindowTitle(_translate("CrearEmpleado", "Foud Court"))
        self.label.setText(_translate("CrearEmpleado", "Crear Nuevo Empleado"))
        self.label_2.setText(_translate("CrearEmpleado", "Nombre: "))
        self.inputNombre.setPlaceholderText(_translate("CrearEmpleado", "Nombre del Empleado"))
        self.label_3.setText(_translate("CrearEmpleado", "Contraseña:"))
        self.InputContrasena.setPlaceholderText(_translate("CrearEmpleado", "Contraseña"))
        self.label_4.setText(_translate("CrearEmpleado", "Documento:"))
        self.inputDoc.setPlaceholderText(_translate("CrearEmpleado", "Documento"))
        self.label_5.setText(_translate("CrearEmpleado", "Rol:"))
        self.label_6.setText(_translate("CrearEmpleado", "Negocio:"))
        self.btnCrear.setText(_translate("CrearEmpleado", "Crear"))
        self.btnCancelar.setText(_translate("CrearEmpleado", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CrearEmpleado = QtWidgets.QWidget()
    ui = Ui_CrearEmpleado()
    ui.setupUi(CrearEmpleado)
    CrearEmpleado.show()
    sys.exit(app.exec_())
