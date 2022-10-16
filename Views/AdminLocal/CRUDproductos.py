import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from Views.AdminLocal.CrearProducto import Ui_CrearProducto
from Views.AdminLocal.ActualizarProducto import Ui_ActualizarProducto
from controllers.AdminLocal.CRUDProductosController import CRUDproductosController

class Ui_Productos(object):
    
    def __init__(self) -> None:
        self.productos_controller = CRUDproductosController(self)
        self.crearProducto = Ui_CrearProducto
        self.actualizarProducto = Ui_ActualizarProducto
    
    def setupUi(self, Productos, MenuAdminLocal):
        #DEFICION DE VARIABLE QUE SE LLAMA A LA MISMA VENTA (SELF)
        self.productos = Productos
        
        #INSTANCIAR EN UNA VARIABLE LA VENTANA DE MENU DEL ADMIN
        self.menuAdminLocal = MenuAdminLocal
        
        Productos.setObjectName("Productos")
        
        #TAMAÑO DE LA VENTANA NO EDITABLE
        Productos.setFixedSize(693, 439)
        
        #AGREGAR ICONO A VENTANA
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/image_Emp.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Productos.setWindowIcon(icon)
        
        self.centralwidget = QtWidgets.QWidget(Productos)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(82, 22, 531, 371))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        #CREACION DE LA TABLA PRODUCTOS
        self.tableProductos = QtWidgets.QTableWidget(self.widget)
        self.tableProductos.setRowCount(10)
        self.tableProductos.setObjectName("tableProductos")
        self.tableProductos.setColumnCount(5)
        
        #PONER TABLA NO EDITABLE
        self.tableProductos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableProductos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableProductos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableProductos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableProductos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableProductos.setHorizontalHeaderItem(4, item)
        self.gridLayout.addWidget(self.tableProductos, 0, 0, 1, 6)
        
        #CREACION BOTON LISTAR
        self.btnListar = QtWidgets.QPushButton(self.widget)
        self.btnListar.setObjectName("btnListar")
        #CREACION ACCION "LISTAR"
        self.btnListar.clicked.connect(self.accionListar)
        self.gridLayout.addWidget(self.btnListar, 1, 0, 1, 1)
        
        #CREACION BOTON ACTUALIZAR
        self.btnActualizar = QtWidgets.QPushButton(self.widget)
        self.btnActualizar.setObjectName("btnActualizar")
        #CREACION ACCION "ACTUALIZAR"
        self.btnActualizar.clicked.connect(self.accionActualizar)
        self.gridLayout.addWidget(self.btnActualizar, 1, 1, 1, 1)
        
        #CREACION BOTON CREAR
        self.btnCrear = QtWidgets.QPushButton(self.widget)
        self.btnCrear.setObjectName("btnCrear")
        #CREAACION ACCION "CREAR"
        self.btnCrear.clicked.connect(self.accionCrear)
        self.gridLayout.addWidget(self.btnCrear, 1, 2, 1, 1)
        
        #CREACION BOTON SELECCIONAR
        self.btnSeleccionar = QtWidgets.QPushButton(self.widget)
        self.btnSeleccionar.setObjectName("btnSeleccionar")
        #CREACCIN ACCION "SELECCIONAR"
        self.btnSeleccionar.clicked.connect(self.accionSeleccionar)
        self.gridLayout.addWidget(self.btnSeleccionar, 1, 3, 1, 1)
        
        #CREACION BOTON ELIMINAR
        self.btnEliminar = QtWidgets.QPushButton(self.widget)
        self.btnEliminar.setObjectName("btnEliminar")
        #CREACION ACCCION "ELIMINAR"
        self.btnEliminar.clicked.connect(self.accionEliminar)
        self.gridLayout.addWidget(self.btnEliminar, 1, 4, 1, 1)
        
        #CREACION BOTON VOLVER
        self.btnVolver = QtWidgets.QPushButton(self.widget)
        self.btnVolver.setObjectName("btnVolver")
        #CREACCION ACCION "VOLVER"
        self.gridLayout.addWidget(self.btnVolver, 1, 5, 1, 1)
        self.btnVolver.clicked.connect(self.accionVolver)
        Productos.setCentralWidget(self.centralwidget)

        self.retranslateUi(Productos)
        QtCore.QMetaObject.connectSlotsByName(Productos)

    def accionListar(self):
        self.productos_controller.listaProductos()
        
    def accionActualizar(self):
        self.productos_controller.abrirActualizarProducto(self.actualizarProducto)
    
    def accionCrear(self):
        self.productos_controller.abrirCrearProducto(self.crearProducto)
    
    def accionSeleccionar(self):
        self.productos_controller.seleccionarProducto()
    
    def accionEliminar(self):
        self.productos_controller.borrarProducto()
    
    def accionVolver(self):
        self.productos_controller.ventanaMenuAdminlocal(self.menuAdminLocal,self.productos)

    def retranslateUi(self, Productos):
        _translate = QtCore.QCoreApplication.translate
        Productos.setWindowTitle(_translate("Productos", "Foud Court"))
        item = self.tableProductos.horizontalHeaderItem(0)
        item.setText(_translate("Productos", "ID"))
        item = self.tableProductos.horizontalHeaderItem(1)
        item.setText(_translate("Productos", "NOMBRE"))
        item = self.tableProductos.horizontalHeaderItem(2)
        item.setText(_translate("Productos", "DESCRIPCIÓN"))
        item = self.tableProductos.horizontalHeaderItem(3)
        item.setText(_translate("Productos", "PRECIO"))
        item = self.tableProductos.horizontalHeaderItem(4)
        item.setText(_translate("Productos", "NEGOCIO"))
        self.btnListar.setText(_translate("Productos", "Listar"))
        self.btnActualizar.setText(_translate("Productos", "Actualizar"))
        self.btnCrear.setText(_translate("Productos", "Crear"))
        self.btnSeleccionar.setText(_translate("Productos", "Seleccionar"))
        self.btnEliminar.setText(_translate("Productos", "Eliminar"))
        self.btnVolver.setText(_translate("Productos", "Volver al menú"))
