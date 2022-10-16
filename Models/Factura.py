import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

import psycopg2

from Database.baseDatos import DB
from PyQt5.QtWidgets import QMessageBox


class Factura():
    def __init__(self) -> None:
        pass
    
    def getFacturaP(self):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                sql = """SELECT id_pedido,mesero,mesa,fecha,total,estado FROM factura"""
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
        finally:
            DB.desconectar(conexion)