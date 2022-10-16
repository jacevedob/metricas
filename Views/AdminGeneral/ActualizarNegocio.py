import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from controllers.AdminGeneral.ActualizarNegocioController import ActualizarNegocioController

class Ui_actualizarNegocio(object):
    
    def __init__(self):
        self.actualizarNegocio_Controller = ActualizarNegocioController(self)
    
    def setupUi(self, actualizarNegocio, negocio):
        #DEFINICION DE VARIABLE QUE LLAMA A LA MISMA VENTANA (CON SELF) PARA PODER UTILIZARLA EN FUNCIONES         
        self.actualizarNegocio = actualizarNegocio
        
        actualizarNegocio.setObjectName("actualizarNegocio")
        
        #TAMAÑO DE LA VENTANA NO EDITABLE
        actualizarNegocio.setFixedSize(330, 303)
        
        #AGREGAR ICONO A LA VENTANA
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/image_Emp.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        actualizarNegocio.setWindowIcon(icon)
        
        self.label_7 = QtWidgets.QLabel(actualizarNegocio)
        self.label_7.setGeometry(QtCore.QRect(40, 10, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.layoutWidget = QtWidgets.QWidget(actualizarNegocio)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 70, 266, 201))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        #CREACION BOTON ACTUALIZAR
        self.btnActualizar = QtWidgets.QPushButton(self.layoutWidget)
        self.btnActualizar.setObjectName("btnActualizar")
        #CREACION ACCION "ACTUALIZAR"
        self.btnActualizar.clicked.connect(self.accionActualizar)
        self.gridLayout_2.addWidget(self.btnActualizar, 1, 0, 1, 1)
        
        #CREACION BOTON CANCELAR
        self.btnCancelar = QtWidgets.QPushButton(self.layoutWidget)
        self.btnCancelar.setObjectName("btnCancelar")
        #CREACION ACCION "CANCELAR"
        self.btnCancelar.clicked.connect(self.accionCancelar)
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
        self.inputEstilo = QtWidgets.QLineEdit(self.layoutWidget)
        self.inputEstilo.setObjectName("inputEstilo")
        self.inputEstilo.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout_3.addWidget(self.inputEstilo, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 2, 0, 1, 1)
        self.inputRut = QtWidgets.QLineEdit(self.layoutWidget)
        self.inputRut.setObjectName("inputRut")
        self.gridLayout_3.addWidget(self.inputRut, 2, 1, 1, 1)
    
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 2)

        #PONER DATOS DEL NEGOCIO PREVIOS A LA ACTUALIZACION
        self.inputNombre_2.setText(str(negocio[1]))
        self.inputEstilo.setText(str(negocio[2]))
        self.inputRut.setText(str(negocio[3]))
        
        #GUARDAR ID DEL NEGOCIO
        self.idUsu = str(negocio[0])
        
        self.retranslateUi(actualizarNegocio)
        QtCore.QMetaObject.connectSlotsByName(actualizarNegocio)
        
    def accionActualizar(self):
        self.nombre = self.inputNombre_2.text()
        self.contra = self.inputEstilo.text()
        self.docu = self.inputRut.text()
        self.nomRol = self.comboBoxRol_2.itemText(self.comboBoxRol_2.currentIndex())
        for rol in self.listaRoles2:
            if rol[1] == self.nomRol:
                self.idRol = rol[0]
        self.nomNegocio = self.comboBoxNegocio_2.itemText(self.comboBoxNegocio_2.currentIndex())
        for negocio in self.listaNegocio2:
            if negocio[1] == self.nomNegocio:
                self.idNegocio = negocio[0]
        self.actualizarNegocio_Controller.actualizarNegocio(self.idUsu,self.nombre,self.contra,self.idRol,self.idNegocio,self.docu,self.actualizarNegocio)
        
    def accionCancelar(self):
        self.actualizarNegocio.close()

    def retranslateUi(self, actualizarNegocio):
        _translate = QtCore.QCoreApplication.translate
        actualizarNegocio.setWindowTitle(_translate("actualizarNegocio", "Foud Court"))
        self.label_7.setText(_translate("actualizarNegocio", "Actualizar Negocio"))
        self.btnActualizar.setText(_translate("actualizarNegocio", "Actualizar"))
        self.btnCancelar.setText(_translate("actualizarNegocio", "Cancelar"))
        self.label_8.setText(_translate("actualizarNegocio", "Nombre: "))
        self.inputNombre_2.setPlaceholderText(_translate("actualizarNegocio", "Nombre del Negocio"))
        self.label_9.setText(_translate("actualizarNegocio", "Estilo: "))
        self.inputEstilo.setPlaceholderText(_translate("actualizarNegocio", "Estilo"))
        self.label_10.setText(_translate("actualizarNegocio", "Rut:"))
        self.inputRut.setPlaceholderText(_translate("actualizarNegocio", "Rut"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    actualizarNegocio = QtWidgets.QWidget()
    ui = Ui_actualizarNegocio()
    ui.setupUi(actualizarNegocio)
    actualizarNegocio.show()
    sys.exit(app.exec_())
