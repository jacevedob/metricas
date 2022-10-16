import psycopg2

class DB():
    #CONEXION A LA BASE DE DATOS
    def conectar():
        try:
            credenciales = {
                "dbname": "grupo01",
                "user": "postgres",
                "password": "abcd1234",
                "host": "poogrupo01.cqozrgcn8atr.us-east-1.rds.amazonaws.com",
                "port": 5432
            }
            conexion = psycopg2.connect(**credenciales) 
            return conexion  
        except psycopg2.Error as e:
            print("\n*************************************")
            print("\nOcurrio un error al conectar a la base de datos\n",e)
            print("*************************************\n")
    
    #CONSULTA DE USUSARIO PARA VALIDAR INICIO DE SESION
    def iniciarSesion(usuario, constrasena):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT nombre,cedula,rol,contraseña,id_negocio FROM usuarios WHERE (nombre='"+str(usuario)+"') AND (contraseña='"+str(constrasena)+"');")
                usuario = cursor.fetchone()
                if usuario:
                    return usuario
        except psycopg2.Error as e:
            print("Ocurrio un error, intente nuevamente: ", e)
        finally:
            conexion.close()

    #DESCONEXION A LA BASE DE DATOS
    def desconectar(conexion):
        conexion.close()

