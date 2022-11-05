import psycopg2

class DB():
    #CONEXION A LA BASE DE DATOS
    def conectar():
        try:
            credenciales = {
                "dbname": "foodcourt",
                "user": "postgres",
                "password": "abcd1234",
                "host": "localhost",
                "port": 5432
            }
            conexion = psycopg2.connect(**credenciales) 
            return conexion  
        except psycopg2.Error as e:
            print("\n*************************************")
            print("\nOcurrio un error al conectar a la base de datos\n",e)
            print("*************************************\n")
    
    #CONSULTA DE USUSARIO PARA VALIDAR INICIO DE SESION
    def iniciarSesion(usuario, contrasena):
        conexion = DB.conectar()
        try:
            with conexion.cursor() as cursor:
                query = "SELECT * FROM usuarios WHERE (usuario='"+str(usuario)+"') AND (contrasena='"+str(contrasena)+"');"
                print(query)
                cursor.execute(query)
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