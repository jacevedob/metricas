import psycopg2
from Database.baseDatos import DB

class Productos():
    
    def __init__(self) -> None:
        pass
    
    def createProducto(self, nombre, descripcion, precio, id_negocio):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("INSERT INTO producto (nombre,descripcion,precio,id_negocio) "
                               "VALUES ('"+str(nombre)+"','"+str(descripcion)+"',"+str(precio)+","+str(id_negocio)+");")
            conexion.commit()
        except psycopg2.Error as e:
            print(e)
        finally:
            if not conexion:
                print("Error Critico")
            else:
                DB.desconectar(conexion)
    
    def readProductos(self):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT id_producto,producto.nombre,descripcion,precio,negocio.nombre FROM producto "
                               "INNER JOIN negocio ON producto.id_negocio = negocio.id_negocio ;")
                productos = cursor.fetchall()
                if productos:
                    return productos
        except psycopg2.Error as e:
            print("Ocurrio un error al consultar: ",e)
        finally:
            if not conexion:
                print("Error Critico")
            else:
                DB.desconectar(conexion)
                
    def readProducto(self, id_producto):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT id_producto, producto.nombre, descripcion, precio, negocio.nombre FROM producto "
                               "INNER JOIN negocio ON producto.id_negocio = negocio.id_negocio WHERE id_producto = "+str(id_producto)+";")
                producto = cursor.fetchone()
                if producto:
                    return producto
        except psycopg2.Error:
            print(psycopg2.Error)
        finally:
            if not conexion:
                print("Error Critico")
            else:
                DB.desconectar(conexion)
    
    def deleteProducto(self, id_producto):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("DELETE FROM producto WHERE id_producto = "+str(id_producto)+";")
            conexion.commit()
        except psycopg2.Error as e:
            print("Seleccione el id que acompaña al empleado")
        finally:
            if not conexion:
                print("Error Critico")
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
            print("Producto actualizado exitosamente :)")
        except psycopg2.Error as e:
            print("Error")
        finally:
            if not conexion:
                print("Error Critico")
            else:
                DB.desconectar(conexion)

productos = Productos()
print(productos.readProductos())