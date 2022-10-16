import psycopg2

from Database.baseDatos import DB
from PyQt5.QtWidgets import QMessageBox

class Productos():
    
    def __init__(self) -> None:
        pass
    
    def createProducto(self, nombre, descripcion, precio, id_negocio):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("INSERT INTO producto (nombre,descripcion,precio,id_negocio) VALUES ('"+str(nombre)+"','"+str(descripcion)+"',"+str(precio)+","+str(id_negocio)+");")
            conexion.commit()
            mensaje = QMessageBox()
            mensaje.setWindowTitle("Información")
            mensaje.setText("Producto creado exitosamente :)")
            mensaje.setIcon(QMessageBox.Information)
            mensaje.setStandardButtons(QMessageBox.Ok)
            mensaje.setDefaultButton(QMessageBox.Ok)
            mensaje.exec_()
        except psycopg2.Error as e:
            print(e)
        finally:
            if not conexion:
                mensaje = QMessageBox()
                mensaje.setWindowTitle("Error Critico")
                mensaje.setText("No es pudo conectar a la base de datos")
                mensaje.setIcon(QMessageBox.Critical)
                mensaje.setStandardButtons(QMessageBox.Ok)
                mensaje.setDefaultButton(QMessageBox.Ok)
                mensaje.exec_()
            else:
                DB.desconectar(conexion)
    
    def readProductos(self):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT id_producto,producto.nombre,descripcion,precio,negocio.nombre FROM producto INNER JOIN negocio ON producto.id_negocio = negocio.id_negocio ;")
                productos = cursor.fetchall()
                if productos:
                    return productos
        except psycopg2.Error as e:
            print("Ocurrio un error al consultar: ",e)
        finally:
            if not conexion:
                mensaje = QMessageBox()
                mensaje.setWindowTitle("Error Critico")
                mensaje.setText("No es pudo conectar a la base de datos")
                mensaje.setIcon(QMessageBox.Critical)
                mensaje.setStandardButtons(QMessageBox.Ok)
                mensaje.setDefaultButton(QMessageBox.Ok)
                mensaje.exec_()
            else:
                DB.desconectar(conexion)
                
    def readProducto(self, id_producto):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT id_producto,producto.nombre,descripcion,precio,negocio.nombre FROM producto INNER JOIN negocio ON producto.id_negocio = negocio.id_negocio WHERE id_producto = "+str(id_producto)+";")
                producto = cursor.fetchone()
                if producto:
                    return producto
        except psycopg2.Error:
            print(psycopg2.Error)
        finally:
            if not conexion:
                mensaje = QMessageBox()
                mensaje.setWindowTitle("Error Critico")
                mensaje.setText("No es pudo conectar a la base de datos")
                mensaje.setIcon(QMessageBox.Critical)
                mensaje.setStandardButtons(QMessageBox.Ok)
                mensaje.setDefaultButton(QMessageBox.Ok)
                mensaje.exec_()
            else:
                DB.desconectar(conexion)
    
    def deleteProducto(self, id_producto):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("DELETE FROM producto WHERE id_producto = "+str(id_producto)+";")
            conexion.commit()
        except psycopg2.Error as e:
            mensaje = QMessageBox()
            mensaje.setWindowTitle("Aviso")
            mensaje.setText("Seleccione el id que acompaña al empleado")
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.setStandardButtons(QMessageBox.Ok)
            mensaje.setDefaultButton(QMessageBox.Ok)
            mensaje.exec_()
        finally:
            if not conexion:
                mensaje = QMessageBox()
                mensaje.setWindowTitle("Error Critico")
                mensaje.setText("No es pudo conectar a la base de datos")
                mensaje.setIcon(QMessageBox.Critical)
                mensaje.setStandardButtons(QMessageBox.Ok)
                mensaje.setDefaultButton(QMessageBox.Ok)
                mensaje.exec_()
            else:
                DB.desconectar(conexion)
                
    def updateProducto(self,id_producto,nombre,descripcion,precio,id_negocio):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("UPDATE producto SET nombre = '"+str(nombre)+
                                "', descripcion = '"+str(descripcion)+
                                "', id_negocio = "+str(id_negocio)+
                                ", precio = "+str(precio)+
                                " WHERE id_producto ="+str(id_producto)+";")
            conexion.commit()
            mensaje = QMessageBox()
            mensaje.setWindowTitle("Información")
            mensaje.setText("Producto actualizado exitosamente :)")
            mensaje.setIcon(QMessageBox.Information)
            mensaje.setStandardButtons(QMessageBox.Ok)
            mensaje.setDefaultButton(QMessageBox.Ok)
            mensaje.exec_()
        except psycopg2.Error as e:
            mensaje = QMessageBox()
            mensaje.setWindowTitle("Error")
            mensaje.setText(e)
            mensaje.setIcon(QMessageBox.Critical)
            mensaje.setStandardButtons(QMessageBox.Ok)
            mensaje.setDefaultButton(QMessageBox.Ok)
            mensaje.exec_()
        finally:
            if not conexion:
                mensaje = QMessageBox()
                mensaje.setWindowTitle("Error Critico")
                mensaje.setText("No es pudo conectar a la base de datos")
                mensaje.setIcon(QMessageBox.Critical)
                mensaje.setStandardButtons(QMessageBox.Ok)
                mensaje.setDefaultButton(QMessageBox.Ok)
                mensaje.exec_()
            else:
                DB.desconectar(conexion)