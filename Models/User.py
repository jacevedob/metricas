import psycopg2
from Database.baseDatos import DB

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
                print("Error de conexión")
            else:
                DB.desconectar(conexion)
    
    def createUser(self, usuario, nombre, contrasena, rol, id_negocio, cedula):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("INSERT INTO usuarios (usuario, nombre,contrasena,rol,id_negocio,cedula) VALUES "
                               "('"+str(usuario)+"','"+str(nombre)+"','"+str(contrasena)+"',"+str(rol)+","+str(id_negocio)+","+str(cedula)+");")
            conexion.commit()
        except psycopg2.Error as e:
            print(e)
        finally:
            if not conexion:
                print("Error de conexión")
            else:
                DB.desconectar(conexion)
            
    def getUser(self, usuario, contrasena):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT nombre, cedula, rol, contrasena FROM usuarios WHERE (usuario='"+str(usuario)+"') AND (contrasena='"+str(contrasena)+"');")
                usuario = cursor.fetchone()
                if usuario:
                    return usuario
        except psycopg2.Error as e:
            print("Usuario no encontrado, intente nuevamente: ", e)
        finally:
            if not conexion:
                print("Error de conexión")
            else:
                DB.desconectar(conexion)
            
    def readUsers(self):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT id_usuario, usuarios.nombre, contrasena, roles.rol, negocio.nombre, cedula FROM "
                               "usuarios INNER JOIN roles ON usuarios.rol = roles.id_rol INNER JOIN negocio ON usuarios.id_negocio = negocio.id_negocio ;")
                usuarios = cursor.fetchall()
                if usuarios:
                    return usuarios
        except psycopg2.Error as e:
            print("Ocurrio un error al consultar: ",e)
        finally:
            if not conexion:
                print("Error de conexión")
            else:
                DB.desconectar(conexion)
            
    def readUser(self, cod):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT id_usuario, usuarios.nombre, contrasena, roles.rol, negocio.nombre, cedula FROM usuarios "
                               "INNER JOIN roles ON usuarios.rol = roles.id_rol INNER JOIN negocio ON usuarios.id_negocio = negocio.id_negocio "
                               "WHERE id_usuario = "+str(cod)+";")
                usuario = cursor.fetchone()
                if usuario:
                    return usuario
        except psycopg2.Error:
            print(psycopg2.Error)
        finally:
            if not conexion:
                print("Error de conexión")
            else:
                DB.desconectar(conexion)
            
    def updateUser(self, id_usuario, nombre, contrasena, rol, id_negocio, cedula):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("UPDATE usuarios SET nombre = '"+str(nombre)+
                                "', contrasena = '"+str(contrasena)+
                                "', rol = "+str(rol)+
                                ", id_negocio = "+str(id_negocio)+
                                ", cedula = "+str(cedula)+
                                " WHERE id_usuario = "+str(id_usuario)+";")
            conexion.commit()
        except psycopg2.Error as e:
            print("Error")
        finally:
            if not conexion:
                print("Error de conexión")
            else:
                DB.desconectar(conexion)
            
    def deleteUser(self, id_usuario):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("DELETE FROM usuarios WHERE id_usuario = "+str(id_usuario)+";")
            conexion.commit()
        except psycopg2.Error as e:
            print("Error")
        finally:
            if not conexion:
                print("Error de conexión")
            else:
                DB.desconectar(conexion)