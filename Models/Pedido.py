import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

import psycopg2

from datetime import datetime
from Database.baseDatos import DB
from PyQt5.QtWidgets import QMessageBox

fechaActual = datetime.today().strftime('%Y/%m/%d')

class Pedido():
    def __init__(self) -> None:
        pass

    ##purple
    
    #FUNCIONES DAVID
    def pedidosPendientes(self):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT distinct pedido.mesa, usuarios.nombre, pedido.estado FROM pedido INNER JOIN usuarios ON pedido.id_mesero = usuarios.id_usu WHERE pedido.estado = 'Pendiente' AND fecha = '"+str(fechaActual)+"';")
                pedidos = cursor.fetchall()
                if pedidos:
                    return pedidos
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
        
    def pedidosPendientesLocal(self, id_negocio):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT distinct pedido.mesa, usuarios.nombre, pedido.estado FROM pedido INNER JOIN usuarios ON pedido.id_mesero = usuarios.id_usu WHERE pedido.estado = 'Pendiente' AND fecha = '"+str(fechaActual)+"' AND pedido.id_negocio = "+str(id_negocio)+";")
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

    def mesaMayor(self):
        conexion= DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT MAX(mesa) FROM pedido;")
                mesaMax = cursor.fetchone()
                if mesaMax:
                    return mesaMax[0]
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
    
    def cierreMesas(self):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT mesa, valor*cant FROM pedido WHERE estado='Listo' AND fecha = '"+str(fechaActual)+"';")
                ventasMesa = cursor.fetchall()
                if ventasMesa:
                    return ventasMesa
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
                
    def cierreMesasLocal(self,idNegocio):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT mesa, valor*cant FROM pedido WHERE estado='Listo' AND fecha = '"+str(fechaActual)+"' AND id_negocio = "+str(idNegocio)+";")
                ventasMesa = cursor.fetchall()
                if ventasMesa:
                    return ventasMesa
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
    
    def cierreMeseros(self):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT usuarios.nombre, pedido.valor*pedido.cant FROM pedido INNER JOIN usuarios ON pedido.id_mesero = usuarios.id_usu WHERE pedido.estado = 'Listo' AND fecha = '"+str(fechaActual)+"';")
                ventasNegocios = cursor.fetchall()
                if ventasNegocios:
                    return ventasNegocios
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
                
    def cierreMeserosLocal(self,idNegocio):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT usuarios.nombre, pedido.valor*pedido.cant FROM pedido INNER JOIN usuarios ON pedido.id_mesero = usuarios.id_usu WHERE pedido.estado = 'Listo' AND fecha = '"+str(fechaActual)+"' AND pedido.id_negocio = "+str(idNegocio)+";")
                ventasNegocios = cursor.fetchall()
                if ventasNegocios:
                    return ventasNegocios
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
    
    def cierreNegocios(self):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT negocio.nombre, pedido.valor*pedido.cant FROM pedido INNER JOIN negocio ON pedido.id_negocio = negocio.id_negocio WHERE pedido.estado = 'Listo' AND fecha = '"+str(fechaActual)+"';")
                ventasNegocios = cursor.fetchall()
                if ventasNegocios:
                    return ventasNegocios
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
        
    def totalVentasDia(self):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT SUM(cant*valor) FROM pedido WHERE pedido.estado = 'Listo' AND fecha = '"+str(fechaActual)+"';")
                total = cursor.fetchone()
                if total:
                    return total
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
                
    def totalVentasDiaLocal(self, idNegocio):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT SUM(cant*valor) FROM pedido WHERE pedido.estado = 'Listo' AND fecha = '"+str(fechaActual)+"' AND id_negocio = "+str(idNegocio)+";")
                total = cursor.fetchone()
                if total:
                    return total
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
                
    ##
    
    ##yellow
    #FUNCIONES PIEDRA
    def insertPedido(self,ID_pedido,ID_negocio,mesero,mesa,producto,cantidad,estado):
        conexion = DB.conectar()
        try:
            with conexion.cursor()as cursor:
                sql = """INSERT INTO pedido(id_pedido,id_negocio,id_mesero,mesa,id_producto,cant,valor,estado,fecha) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                Valor = Pedido.consultarValor(producto)
                Valor = Valor*cantidad
                cursor.execute(sql,(ID_pedido,ID_negocio,mesero,mesa,producto,cantidad,Valor,estado,datetime.today().strftime('%Y-%m-%d')))
                conexion.commit()
        finally:
            DB.desconectar(conexion)
    
    def consultarValor(id_producto):
        conexion = DB.conectar()
        try:
            with conexion.cursor()as cursor:
                cursor.execute("SELECT valor FROM Pedido WHERE id_producto = "+str(id_producto)+";")
                valor = cursor.fetchone()
                return valor[0]
        finally:
            DB.desconectar(conexion)
            
    def getPedidosP(self):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                sql = """SELECT id_pedido,id_negocio,id_mesero,mesa,id_producto,cant,valor,estado,fecha FROM pedido"""
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
        finally:
            DB.desconectar(conexion)        
    ##
    
    ##blue
    #GAZABON
    def getPedidosG(self):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                sql = "SELECT id_pedido, id_producto, cant, estado FROM pedido WHERE estado = 'Pendiente';"
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
        except psycopg2.Error as e:
            print("Pedido no encontrado, intente nuevamente: ", e)
        finally:
            DB.desconectar(conexion)

    def getPedidosAceptados(self):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                sql = "SELECT id_pedido, id_producto, cant, estado FROM pedido WHERE estado = 'Aceptado';"
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
        except psycopg2.Error as e:
            print("Pedido no encontrado, intente nuevamente: ", e)
        finally:
            DB.desconectar(conexion)

    def updateaceptar(self,id_pedido):
            conexion = DB.conectar()
            try:
                with conexion.cursor() as cursor:
                    consulta = "UPDATE pedido set estado = 'Aceptado' where id_pedido = " + str(id_pedido)
                    cursor.execute(consulta)
                conexion.commit()
            except psycopg2.Error as e:
                mensaje = QMessageBox()
                mensaje.setWindowTitle("Error")
                mensaje.setText(e)
                mensaje.setIcon(QMessageBox.Critical)
                mensaje.setStandardButtons(QMessageBox.Ok)
                mensaje.setDefaultButton(QMessageBox.Ok)
                mensaje.exec_()

    def updatecancelar(self,id_pedido):
            conexion = DB.conectar()
            try:
                with conexion.cursor() as cursor:
                    consulta = "UPDATE pedido set estado = 'Cancelado' where id_pedido = " + str(id_pedido)
                    cursor.execute(consulta)
                conexion.commit()
            except psycopg2.Error as e:
                mensaje = QMessageBox()
                mensaje.setWindowTitle("Error")
                mensaje.setText(e)
                mensaje.setIcon(QMessageBox.Critical)
                mensaje.setStandardButtons(QMessageBox.Ok)
                mensaje.setDefaultButton(QMessageBox.Ok)
                mensaje.exec_()            
                    

    def updateestado(self,id_pedido):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                consulta = "UPDATE pedido set estado = 'Listo' where id_pedido = " + str(id_pedido)
                cursor.execute(consulta)
            conexion.commit()
        except psycopg2.Error as e:
            mensaje = QMessageBox()
            mensaje.setWindowTitle("Error")
            mensaje.setText(e)
            mensaje.setIcon(QMessageBox.Critical)
            mensaje.setStandardButtons(QMessageBox.Ok)
            mensaje.setDefaultButton(QMessageBox.Ok)
            mensaje.exec_()
    ##