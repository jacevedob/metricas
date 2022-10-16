import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Views.AdminGeneral.CrearNegocio import Ui_crearNegocio
from Views.AdminGeneral.ActualizarNegocio import Ui_actualizarNegocio
from controllers.AdminGeneral.CRUDnegociosController import CRUDnegociosController
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Negocios(object):
    
    def __init__(self):
        self.negocios_controller = CRUDnegociosController(self)
        self.crearNegocio = Ui_crearNegocio
        self.actualizarNegocio = Ui_actualizarNegocio
    
    def setupUi(self, Negocios, MenuAdminGeneral):
        #DEFICION DE VARIABLE QUE SE LLAMA A LA MISMA VENTA (SELF)
        self.Negocios = Negocios
        
        #INSTANCIAR EN UNA VARIABLE LA VENTANA DE MENU DEL ADMIN
        self.MenuAdminGeneral = MenuAdminGeneral
        
        Negocios.setObjectName("Negocios")
        
        #TAMAÑO DE LA VENTAN NO EDITABLE
        Negocios.setFixedSize(690, 467)
        
        #AGREGAR ICONO A VENTANA
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/image_Emp.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Negocios.setWindowIcon(icon)
        
        self.centralwidget = QtWidgets.QWidget(Negocios)
        self.centralwidget.setObjectName("centralwidget")
        
        #CREACION DE TABLA NEGOCIOS
        self.tableNegocios = QtWidgets.QTableWidget(self.centralwidget)
        self.tableNegocios.setGeometry(QtCore.QRect(130, 20, 426, 331))
        self.tableNegocios.setRowCount(10)
        self.tableNegocios.setObjectName("tableNegocios")
        self.tableNegocios.setColumnCount(4)
        self.tableNegocios.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        item = QtWidgets.QTableWidgetItem()
        self.tableNegocios.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableNegocios.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableNegocios.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableNegocios.setHorizontalHeaderItem(3, item)
        
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 360, 631, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        #CREACION DE BOTON LISTAR
        self.btnListarNegocios = QtWidgets.QPushButton(self.layoutWidget)
        self.btnListarNegocios.setObjectName("btnListarEmpleados")
        #CREACION ACCION BOTON "LISTAR"
        self.btnListarNegocios.clicked.connect(self.accionListar)
        self.horizontalLayout.addWidget(self.btnListarNegocios)
        
        #CREACION DE BOTON ACTUALIZAR
        self.btnActualizarNegocios = QtWidgets.QPushButton(self.layoutWidget)
        self.btnActualizarNegocios.setObjectName("btnActualizarNegocios")
        #CREACION ACCION BOTON "ACTUALIZAR"
        self.btnActualizarNegocios.clicked.connect(self.accionActualizar)
        self.horizontalLayout.addWidget(self.btnActualizarNegocios)
        
        #CREACION DE BOTON CREAR
        self.btnCrearNegocios = QtWidgets.QPushButton(self.layoutWidget)
        self.btnCrearNegocios.setObjectName("btnCrearNegocio")
        #CREACION ACCION BOTON CREAR
        self.btnCrearNegocios.clicked.connect(self.accionCrear)
        self.horizontalLayout.addWidget(self.btnCrearNegocios)
        
        #CREACION DE BOTON SALEECIONAR
        self.btnSeleccionarNegocios = QtWidgets.QPushButton(self.layoutWidget)
        self.btnSeleccionarNegocios.setObjectName("btnSeleccionarNegocios")
        #CREACION DE ACCION BORON "SELECCIONAR"
        self.btnSeleccionarNegocios.clicked.connect(self.accionSeleccionar)
        self.horizontalLayout.addWidget(self.btnSeleccionarNegocios)
        
        #CREACION DE BOTON ELIMINAR
        self.btnEliminarNegocios = QtWidgets.QPushButton(self.layoutWidget)
        self.btnEliminarNegocios.setObjectName("btnEliminarNegocios")
        #CREACION ACCION BOTON "ELIMINAR"
        self.btnEliminarNegocios.clicked.connect(self.accionEliminar)
        self.horizontalLayout.addWidget(self.btnEliminarNegocios)
        
        #CREACION DE BOTON VOLVER
        self.btnVolver = QtWidgets.QPushButton(self.layoutWidget)
        self.btnVolver.setObjectName("btnVolver")
        #CREACION ACCION BOTON "VOLVER"
        self.btnVolver.clicked.connect(self.accionVolver)
        self.horizontalLayout.addWidget(self.btnVolver)
        
        Negocios.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Negocios)
        self.statusbar.setObjectName("statusbar")
        Negocios.setStatusBar(self.statusbar)

        self.retranslateUi(Negocios)
        QtCore.QMetaObject.connectSlotsByName(Negocios)
        
    def accionListar(self):
        self.negocios_controller.listaNegocios()
    
    def accionSeleccionar(self):
        self.negocios_controller.seleccionarNegocio()
    
    def accionActualizar(self):
        self.negocios_controller.abrirActualizarNegocios(self.actualizarNegocio)
    
    def accionEliminar(self):
        self.negocios_controller.borrarNegocio()
        
    def accionCrear(self):
        self.negocios_controller.abrirCrearNegocios(self.crearNegocio)

    def accionVolver(self):
        self.negocios_controller.ventanaMenuAdminGeneral(self.MenuAdminGeneral,self.Negocios)
        
    def retranslateUi(self, Negocios):
        _translate = QtCore.QCoreApplication.translate
        Negocios.setWindowTitle(_translate("Negocios", "Foud Court"))
        item = self.tableNegocios.horizontalHeaderItem(0)
        item.setText(_translate("Negocios", "ID"))
        item = self.tableNegocios.horizontalHeaderItem(1)
        item.setText(_translate("Negocios", "NOMBRE"))
        item = self.tableNegocios.horizontalHeaderItem(2)
        item.setText(_translate("Negocios", "ESTILO COMIDA"))
        item = self.tableNegocios.horizontalHeaderItem(3)
        item.setText(_translate("Negocios", "RUT"))
        self.btnListarNegocios.setText(_translate("Negocios", "Listar"))
        self.btnActualizarNegocios.setText(_translate("Negocios", "Actualizar"))
        self.btnCrearNegocios.setText(_translate("Negocios", "Crear"))
        self.btnSeleccionarNegocios.setText(_translate("Negocios", "Seleccionar"))
        self.btnEliminarNegocios.setText(_translate("Negocios", "Eliminar"))
        self.btnVolver.setText(_translate("Negocios", "Volver al menú"))
