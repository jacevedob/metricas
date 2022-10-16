import psycopg2

from Database.baseDatos import DB

class Roles():
    def __init__(self) -> None:
        pass
        
    def readRoles(self):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM roles;")
                roles = cursor.fetchall()
                if roles:
                    return roles
        except psycopg2.Error as e:
            print(e)
        finally:
            DB.desconectar(conexion)