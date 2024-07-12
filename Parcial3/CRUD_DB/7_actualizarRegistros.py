from conexionBD import *

try:
    micursor=conexion.cursor()

    sql="update clientes set direccion='Col. Nueva Vizcaya', where id=2"
    micursor.execute(sql)

    conexion.commit()
except:
    print("Ocurrio un error ")
else:

    print(f"Registro actualizado exitosamente")

