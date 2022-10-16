import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from Models.Roles import Roles
from Models.Negocio import Negocios
from controllers.AdminGeneral.ActualizarEmpleadoController import ActualizarEmpleadoController

class Ui_actualizarEmpleado(object):
    
    def __init__(self):
        self.actualizarEmpleado_Controller = ActualizarEmpleadoController(self)
    
    def setupUi(self, actualizarEmpleado, usuario):
        #DEFINICION DE VARIABLE QUE LLAMA A LA MISMA VENTANA (CON SELF) PARA PODER UTILIZARLA EN FUNCIONES         
        self.actualizarEmpleado = actualizarEmpleado
        
        actualizarEmpleado.setObjectName("actualizarEmpleado")
        
        #TAMAÑO DE LA VENTANA NO EDITABLE
        actualizarEmpleado.setFixedSize(330, 303)
        
        #AGREGAR ICONO A LA VENTANA
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/image_Emp.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        actualizarEmpleado.setWindowIcon(icon)
        
        self.label_7 = QtWidgets.QLabel(actualizarEmpleado)
        self.label_7.setGeometry(QtCore.QRect(40, 10, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.layoutWidget = QtWidgets.QWidget(actualizarEmpleado)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 70, 266, 201))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        #CREACION BOTON ACTUALIZAR
        self.btnActualizar = QtWidgets.QPushButton(self.layoutWidget)
        self.btnActualizar.setObjectName("btnActualizar")
        self.gridLayout_2.addWidget(self.btnActualizar, 1, 0, 1, 1)
        
        #CREACION BOTON CANCELAR
        self.btnCancelar = QtWidgets.QPushButton(self.layoutWidget)
        self.btnCancelar.setObjectName("btnCancelar")
        self.gridLayout_2.addWidget(self.btnCancelar, 1, 1, 1, 1)
        
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)
        self.inputNombre_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.inputNombre_2.setObjectName("inputNombre_2")
        self.gridLayout_3.addWidget(self.inputNombre_2, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 1, 0, 1, 1)
        self.InputContrasena_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.InputContrasena_2.setObjectName("InputContrasena_2")
        self.InputContrasena_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout_3.addWidget(self.InputContrasena_2, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 2, 0, 1, 1)
        self.inputDoc_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.inputDoc_2.setObjectName("inputDoc_2")
        self.gridLayout_3.addWidget(self.inputDoc_2, 2, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 3, 0, 1, 1)
        self.comboBoxRol_2 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBoxRol_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBoxRol_2.setObjectName("comboBoxRol_2")
        self.gridLayout_3.addWidget(self.comboBoxRol_2, 3, 1, 1, 1)
        
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 4, 0, 1, 1)
        self.comboBoxNegocio_2 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBoxNegocio_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBoxNegocio_2.setObjectName("comboBoxNegocio_2")
        self.gridLayout_3.addWidget(self.comboBoxNegocio_2, 4, 1, 1, 1)
        
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 2)

        #PONER DATOS DEL EMPLEADO PREVIOS A LA ACTUALIZACION
        self.inputNombre_2.setText(str(usuario[1]))
        self.InputContrasena_2.setText(str(usuario[2]))
        self.inputDoc_2.setText(str(usuario[5]))
        
        #GUARDAR ID DEL USUARIO
        self.idUsu = str(usuario[0])
        
        #PONER ROLES DEFINIDOS EN LA BASE DE DATOS EN COMBOBOXROL
        self.listaRoles2 = Roles.readRoles(self)
        for rol in self.listaRoles2:
            itemRol = rol[1]
            self.comboBoxRol_2.addItem(itemRol)
            
        #PONER NEGOCIOS DE BASE DE DATOS EN COMBOBOXBNEGOCIO
        self.listaNegocio2 = Negocios.readNegocios(self)
        for negocio in self.listaNegocio2:
            itemNegocio = negocio[1]
            self.comboBoxNegocio_2.addItem(itemNegocio)
        
        ##-------------------EVENTOS----------------------------##
        self.btnActualizar.clicked.connect(self.accionActualizar)
        self.btnCancelar.clicked.connect(self.accionCancelar)
        ##------------------------------------------------------##    
        
        self.retranslateUi(actualizarEmpleado)
        QtCore.QMetaObject.connectSlotsByName(actualizarEmpleado)
        
    def accionActualizar(self):
        self.nombre = self.inputNombre_2.text()
        self.contra = self.InputContrasena_2.text()
        self.docu = self.inputDoc_2.text()
        self.nomRol = self.comboBoxRol_2.itemText(self.comboBoxRol_2.currentIndex())
        for rol in self.listaRoles2:
            if rol[1] == self.nomRol:
                self.idRol = rol[0]
        self.nomNegocio = self.comboBoxNegocio_2.itemText(self.comboBoxNegocio_2.currentIndex())
        for negocio in self.listaNegocio2:
            if negocio[1] == self.nomNegocio:
                self.idNegocio = negocio[0]
        self.actualizarEmpleado_Controller.actualizarEmpleado(self.idUsu,self.nombre,self.contra,self.idRol,self.idNegocio,self.docu,self.actualizarEmpleado)
        
    def accionCancelar(self):
        self.actualizarEmpleado.close()

    def retranslateUi(self, actualizarEmpleado):
        _translate = QtCore.QCoreApplication.translate
        actualizarEmpleado.setWindowTitle(_translate("actualizarEmpleado", "Foud Court"))
        self.label_7.setText(_translate("actualizarEmpleado", "Actualizar Empleado"))
        self.btnActualizar.setText(_translate("actualizarEmpleado", "Actualizar"))
        self.btnCancelar.setText(_translate("actualizarEmpleado", "Cancelar"))
        self.label_8.setText(_translate("actualizarEmpleado", "Nombre: "))
        self.inputNombre_2.setPlaceholderText(_translate("actualizarEmpleado", "Nombre del Empleado"))
        self.label_9.setText(_translate("actualizarEmpleado", "Contraseña:"))
        self.InputContrasena_2.setPlaceholderText(_translate("actualizarEmpleado", "Contraseña"))
        self.label_10.setText(_translate("actualizarEmpleado", "Documento:"))
        self.inputDoc_2.setPlaceholderText(_translate("actualizarEmpleado", "Documento"))
        self.label_11.setText(_translate("actualizarEmpleado", "Rol:"))
        self.label_12.setText(_translate("actualizarEmpleado", "Negocio:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    actualizarEmpleado = QtWidgets.QWidget()
    ui = Ui_actualizarEmpleado()
    ui.setupUi(actualizarEmpleado)
    actualizarEmpleado.show()
    sys.exit(app.exec_())
