from conexionBD import*

try:
    micursor=conexion.cursor()

    # sql="select nombre, tel from clientes where id=1"

    sql="select * from clientes"
    micursor.execute(sql)

    #Crar un objeto para envirar el resultado del la ejecucion del execute para posteiormente mostrar con ciclo
    resultado=micursor.fetchall()

except:
    print("Error ")
else:
    for x in resultado:
        print(x)
