import psycopg2

from Database.baseDatos import DB
from PyQt5.QtWidgets import QMessageBox

class Negocios():
    def __init__(self):
        pass
        
    def readNegocios(self):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM negocio;")
                negocios = cursor.fetchall()
                if negocios:
                    return negocios
        except psycopg2.Error as e:
            print("ocurrio un error",e)
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
            
    def createNegocio(self, nombre,estilo_comida,rut):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("INSERT INTO negocio (nombre,estilo_comida,rut) VALUES ('"+str(nombre)+"','"+str(estilo_comida)+"',"+str(rut)+");")
            conexion.commit()
            mensaje = QMessageBox()
            mensaje.setWindowTitle("Información")
            mensaje.setText("Negocio creado exitosamente :)")
            mensaje.setIcon(QMessageBox.Information)
            mensaje.setStandardButtons(QMessageBox.Ok)
            mensaje.setDefaultButton(QMessageBox.Ok)
            mensaje.exec_()
        except psycopg2.Error as e:
            print("Ocurrio un error",e)
        finally:
            if not conexion:
                mensaje = QMessageBox()
                mensaje.setWindowTitle("Error Critico")
                mensaje.setText("No se pudo conectar a la base de datos")
                mensaje.setIcon(QMessageBox.Critical)
                mensaje.setStandardButtons(QMessageBox.Ok)
                mensaje.setDefaultButton(QMessageBox.Ok)
                mensaje.exec_()
            else:
                DB.desconectar(conexion)

    def readNegocio(self, id_negocio):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT id_negocio,nombre,estilo_comida,rut FROM negocio WHERE id_negocio = "+str(id_negocio)+";")
                negocio = cursor.fetchone()
                if negocio:
                    return negocio
        except psycopg2.Error as e:
            print("Ocurrio un error",e)
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
            
    def updateNegocio(self, id_negocio, nombre, estilo_comida, rut):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("UPDATE negocio SET nombre = '"+str(nombre)+
                                "', estilo_comida = '"+str(estilo_comida)+
                                "', rut = "+str(rut)+
                                " WHERE id_negocio = "+str(id_negocio)+";")
            conexion.commit()
            mensaje = QMessageBox()
            mensaje.setWindowTitle("Información")
            mensaje.setText("Negocio actualizado exitosamente :)")
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
            
    def deleteNegocio(self, id_negocio):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("DELETE FROM negocio WHERE id_negocio = "+str(id_negocio)+";")
            conexion.commit()
            mensaje = QMessageBox()
            mensaje.setWindowTitle("Información")
            mensaje.setText("Negocio eliminado exitosamente :)")
            mensaje.setIcon(QMessageBox.Information)
            mensaje.setStandardButtons(QMessageBox.Ok)
            mensaje.setDefaultButton(QMessageBox.Ok)
            mensaje.exec_()
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