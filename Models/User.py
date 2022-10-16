import psycopg2

from Database.baseDatos import DB
from PyQt5.QtWidgets import QMessageBox

class User():
    
    def __init__(self) -> None:
        pass
    
    def getMeseros(self):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT nombre FROM usuarios WHERE rol = 3;")
                meseros = cursor.fetchall()
                if meseros:
                    return meseros
        except psycopg2.Error as e:
            print("Usuario no encontrado, intente nuevamente: ", e)
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
    
    def createUser(self, nombre, contrasena, rol, id_negocio,cedula):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("INSERT INTO usuarios (nombre,contraseña,rol,id_negocio,cedula) VALUES ('"+str(nombre)+"','"+str(contrasena)+"',"+str(rol)+","+str(id_negocio)+","+str(cedula)+");")
            conexion.commit()
            mensaje = QMessageBox()
            mensaje.setWindowTitle("Información")
            mensaje.setText("Usuario creado exitosamente :)")
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
            
    def getUser(usuario, contrasena):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT nombre,cedula,rol,contraseña FROM usuarios WHERE (nombre='"+str(usuario)+"') AND (contraseña='"+str(contrasena)+"');")
                usuario = cursor.fetchone()
                if usuario:
                    return usuario
        except psycopg2.Error as e:
            print("Usuario no encontrado, intente nuevamente: ", e)
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
            
    def readUsers(self):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT id_usu,usuarios.nombre,contraseña,roles.rol,negocio.nombre,cedula FROM usuarios INNER JOIN roles ON usuarios.rol = roles.id_rol INNER JOIN negocio ON usuarios.id_negocio = negocio.id_negocio ;")
                usuarios = cursor.fetchall()
                if usuarios:
                    return usuarios
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
            
    def readUser(self, cod):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT id_usu,usuarios.nombre,contraseña,roles.rol,negocio.nombre,cedula FROM usuarios INNER JOIN roles ON usuarios.rol = roles.id_rol INNER JOIN negocio ON usuarios.id_negocio = negocio.id_negocio WHERE id_usu = "+str(cod)+";")
                usuario = cursor.fetchone()
                if usuario:
                    return usuario
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
            
    def updateUser(self, id_usu, nombre, contraseña, rol, id_negocio, cedula):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("UPDATE usuarios SET nombre = '"+str(nombre)+
                                "', contraseña = '"+str(contraseña)+
                                "', rol = "+str(rol)+
                                ", id_negocio = "+str(id_negocio)+
                                ", cedula = "+str(cedula)+
                                " WHERE id_usu = "+str(id_usu)+";")
            conexion.commit()
            mensaje = QMessageBox()
            mensaje.setWindowTitle("Información")
            mensaje.setText("Usuario actualizado exitosamente :)")
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
            
    def deleteUser(self, id_usu):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("DELETE FROM usuarios WHERE id_usu = "+str(id_usu)+";")
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