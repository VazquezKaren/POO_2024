import mysql.connector

try:
    #Conectar con la BD en MySQL
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bd_veterinaria'
    )
    #Crear un objeto de tipo cursor que tenga un parametro que permita reutilizar el objeto 
    cursor=conexion.cursor(buffered=True)
    print("se hizo la conexion")
except:
     print(f"Ocurrio un error con el Sistema por favor verifique ...")    