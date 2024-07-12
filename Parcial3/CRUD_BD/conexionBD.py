import mysql.connector

#Conectar con la BD en MySQL
try:
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bd_python'
)
except Exception as e:
    print(f"Error {e}")
    print(f"Tipo de excepcion: {type(e).__name__}")
    print("Error en el servidor...")

# except InterfaceError:
#     print("No es posible conectarse al servidor")

else:
    #es lo mismos que lo de arriba
    # conexion=mysql.connector.conect('localhost','root','','bd_python')

    #verificar si la conexion fue exitosa
    if conexion.is_connected():
        print(f"Se creo la conexion con la bd exitosamente...")

    else:
        print(f"No fre posible conectar con la BD...verifique...")




    