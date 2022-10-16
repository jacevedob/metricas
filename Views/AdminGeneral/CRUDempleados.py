import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Views.AdminGeneral.CrearEmpleado import Ui_CrearEmpleado
from Views.AdminGeneral.ActualizarEmpleado import Ui_actualizarEmpleado
from controllers.AdminGeneral.CRUDempleadosController import CRUDempleadosController
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Empleados(object):
    
    def __init__(self):
        self.empleados_controller = CRUDempleadosController(self)
        self.crearEmpleado = Ui_CrearEmpleado
        self.actualizarEmpleado = Ui_actualizarEmpleado
    
    def setupUi(self, Empleados, MenuAdminGeneral):
        #DEFICION DE VARIABLE QUE SE LLAMA A LA MISMA VENTA (SELF)
        self.Empleados = Empleados
        
        #INSTANCIAR EN UNA VARIABLE LA VENTANA DE MENU DEL ADMIN
        self.menuAdminGeneral = MenuAdminGeneral
        
        Empleados.setObjectName("Empleados")
        
        #TAMAÑO DE LA VENTAN NO EDITABLE
        Empleados.setFixedSize(690, 467)
        
        #AGREGAR ICONO A VENTANA
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/image_Emp.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Empleados.setWindowIcon(icon)
        
        self.centralwidget = QtWidgets.QWidget(Empleados)
        self.centralwidget.setObjectName("centralwidget")
        
        #CREACION DE TABLA EMPLEADOS
        self.tableEmpleados = QtWidgets.QTableWidget(self.centralwidget)
        self.tableEmpleados.setGeometry(QtCore.QRect(30, 20, 624, 331))
        self.tableEmpleados.setRowCount(10)
        self.tableEmpleados.setObjectName("tableEmpleados")
        self.tableEmpleados.setColumnCount(6)
        
        #PONER TABLA NO EDITABLE
        self.tableEmpleados.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableEmpleados.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableEmpleados.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableEmpleados.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableEmpleados.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableEmpleados.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableEmpleados.setHorizontalHeaderItem(5, item)
        
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 360, 631, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        #CREACION DE BOTON LISTAR
        self.btnListarEmpleados = QtWidgets.QPushButton(self.layoutWidget)
        self.btnListarEmpleados.setObjectName("btnListarEmpleados")
        #CREACION ACCION BOTON "LISTAR"
        self.btnListarEmpleados.clicked.connect(self.accionListar)
        self.horizontalLayout.addWidget(self.btnListarEmpleados)
        
        #CREACION DE BOTON ACTUALIZAR
        self.btnActualizar = QtWidgets.QPushButton(self.layoutWidget)
        self.btnActualizar.setObjectName("btnActualizar")
        #CREACION ACCION BOTON "ACTUALIZAR"
        self.btnActualizar.clicked.connect(self.accionActualizar)
        self.horizontalLayout.addWidget(self.btnActualizar)
        
        #CREACION DE BOTON CREAR
        self.btnCrearEmpleado = QtWidgets.QPushButton(self.layoutWidget)
        self.btnCrearEmpleado.setObjectName("btnCrearEmpleado")
        #CREACION ACCION BOTON CREAR
        self.btnCrearEmpleado.clicked.connect(self.accionCrear)
        self.horizontalLayout.addWidget(self.btnCrearEmpleado)
        
        #CREACION DE BOTON SALEECIONAR
        self.btnSeleccionar = QtWidgets.QPushButton(self.layoutWidget)
        self.btnSeleccionar.setObjectName("btnSeleccionar")
        #CREACION DE ACCION BORON "SELECCIONAR"
        self.btnSeleccionar.clicked.connect(self.accionSeleccionar)
        self.horizontalLayout.addWidget(self.btnSeleccionar)
        
        #CREACION DE BOTON ELIMINAR
        self.btnEliminar = QtWidgets.QPushButton(self.layoutWidget)
        self.btnEliminar.setObjectName("btnEliminar")
        #CREACION ACCION BOTON "ELIMINAR"
        self.btnEliminar.clicked.connect(self.accionEliminar)
        self.horizontalLayout.addWidget(self.btnEliminar)
        
        #CREACION DE BOTON VOLVER
        self.btnVolver = QtWidgets.QPushButton(self.layoutWidget)
        self.btnVolver.setObjectName("btnVolver")
        #CREACION ACCION BOTON "VOLVER"
        self.btnVolver.clicked.connect(self.accionVolver)
        self.horizontalLayout.addWidget(self.btnVolver)
        
        Empleados.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Empleados)
        self.statusbar.setObjectName("statusbar")
        Empleados.setStatusBar(self.statusbar)

        self.retranslateUi(Empleados)
        QtCore.QMetaObject.connectSlotsByName(Empleados)
        
    def accionListar(self):
        self.empleados_controller.listaEmpleados()
        
    def accionSeleccionar(self):
        self.empleados_controller.seleccionarEmpleado()
        
    def accionActualizar(self):
        self.empleados_controller.abrirActualizarEmpleado(self.actualizarEmpleado)
        
    def accionEliminar(self):
        self.empleados_controller.borrarEmpleado()
        
    def accionCrear(self):
        self.empleados_controller.abrirCrearEmpleado(self.crearEmpleado)
        
    def accionVolver(self):
        self.empleados_controller.ventanaMenuAdminGeneral(self.menuAdminGeneral,self.Empleados)

    def retranslateUi(self, Empleados):
        _translate = QtCore.QCoreApplication.translate
        Empleados.setWindowTitle(_translate("Empleados", "Foud Court"))
        item = self.tableEmpleados.horizontalHeaderItem(0)
        item.setText(_translate("Empleados", "ID"))
        item = self.tableEmpleados.horizontalHeaderItem(1)
        item.setText(_translate("Empleados", "NOMBRE"))
        item = self.tableEmpleados.horizontalHeaderItem(2)
        item.setText(_translate("Empleados", "CONTRASEÑA"))
        item = self.tableEmpleados.horizontalHeaderItem(3)
        item.setText(_translate("Empleados", "ROL"))
        item = self.tableEmpleados.horizontalHeaderItem(4)
        item.setText(_translate("Empleados", "ID NEGOCIO"))
        item = self.tableEmpleados.horizontalHeaderItem(5)
        item.setText(_translate("Empleados", "CEDULA"))
        self.btnListarEmpleados.setText(_translate("Empleados", "Listar"))
        self.btnActualizar.setText(_translate("Empleados", "Actualizar"))
        self.btnCrearEmpleado.setText(_translate("Empleados", "Crear"))
        self.btnSeleccionar.setText(_translate("Empleados", "Seleccionar"))
        self.btnEliminar.setText(_translate("Empleados", "Eliminar"))
        self.btnVolver.setText(_translate("Empleados", "Volver al menú"))
