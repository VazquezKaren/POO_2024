import mysql.connector

try:
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bd_servidor'
    )
    cursor=conexion.cursor(buffered=True)
    print("se hizo la conexion")
except:
    print("No se pudo hacer la conexion")