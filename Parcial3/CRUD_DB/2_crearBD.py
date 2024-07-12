import mysql.connector

try:
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bd_python'
    )


except:
    print(f"Ocurrio un error con el servidor, verifique mas tarde")

else:
 #Crear un objeto de tipo cursor que permita ejecutar instrucciones SQL
    micursor=conexion.cursor()

# sql="create.database bd_python"
 
#ejecutar la consulta

    if micursor:
        print(f"se creo bd exitosamente")

#Mostrar bases de datos que existen en el SGBD Mysql
    micursor.execute("SHOW DATABASES")

    for x in micursor:
        print(x)