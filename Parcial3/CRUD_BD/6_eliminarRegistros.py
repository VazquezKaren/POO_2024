from conexionBD import *

try:
    micursor=conexion.cursor()

    sql="DELETE FROM clientes WHERE id=1"
    micursor.execute(sql)

    conexion.commit()
except:
    print("Ocurrio un error ")
else:

    print(f"Registro eliminado exitosamente")