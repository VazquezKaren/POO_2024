from clientes import clientes
from revisiones import revisiones
import getpass
from funciones import *
from autos import autos



def menu_principal():
    print("""..:::Login:::.""")
    nombre=input("Nombre: ")
    tel=input("Telefono: ")
    obj_usuario=clientes.clientes.iniciar_sesion(nombre,tel)
   
    if len(obj_usuario)>0:
               menu_secundario()
    else:
        print(f"\n\t ** Nombre de usuario y/o contraseña incorrectos, intentalo de nuevo ** ...")
        esperarTecla()  

    
def menu_secundario():
    while True:
        print(""".::::Menu::::.
              1-Clientes
              2-Autos
              3-Revisiones
                        """)
        op=input("Seleciona una opcion: ")
        
        if op=="1":
            while True:
                print(""".::::Clientes::::.
              1-Registrar cliente
              2-actualizar cliente
              3-Ver Registros
              4-Eliminar
                        """)
                op_cliente=input("Selecciona una opcion: ")
                if op_cliente=="1":
                    nif=input("Numero de identifica: ")
                    nombre=input("Nombre: ")
                    direccion=input("Direccion: ")
                    ciudad=input("Ciudad: ")
                    tel=input("Telefono: ")
                    objeto_cliente=clientes.clientes(nif,nombre,direccion,ciudad,tel)
                    resultado=objeto_cliente.insertar()

                    if resultado:
                        print("Se registro cliente")
                    else:
                        print("No se pudo hacer el registro")
                elif op_cliente=="2":
                    nif_n=input("Nif del cliente:")
                    nombre_n=input("Nombre: ")
                    direccion_n=input("Direccion: ")
                    ciudad_n=input("Ciudad: ")
                    tel_n=input("Telefono: ")
                    object_ca=clientes.clientes.actualizar(nif_n,nombre_n,direccion_n,ciudad_n,tel_n)
                    if object_ca:
                        print("Se actualizo cliente")
                    else:
                        print("No se pudo hacer actualizacion")
                

                elif op_cliente=="3":
                   
                    registro=clientes.clientes()
                    if len(registro)>0:
                        for fila in registro:
                            print(f"Nombre: {fila[0]} \n  Direccion: {fila[1]} \n  Ciudad: {fila[3]} tel: {fila[4]} ")
                        else:
                            print("No hay registros")
                elif op_cliente=="4":
                    nif_n=input("Nif del cliente:")
                    resultado=clientes.clientes.eliminar(nif_n)
                    if resultado:
                        print("Se elimino cliente")
                    else:
                        print("No se pudo eliminar")
                else:
                    break

        elif op=="2":
            while True:
                print(""".::::Autos::::.
              1-Registrar auto
              2-actualizar auto
              3-Ver Registros
              4-Eliminar
                        """)
                op_cliente=input("Selecciona una opcion: ")
                if op_cliente=="1":
                    matricula=input("Matricula: ")
                    marca=input("Marca: ")
                    modelo=input("modelo: ")
                    color=input("color: ")
                    nif=input("Nif: ")
                    objeto_auto=autos.Autos(matricula,marca, modelo,color,nif)
                    resultado=objeto_auto.insertar()

                    if resultado:
                        print("Se registro el auto")
                    else:
                        print("No se pudo hacer el registro")

                elif op_cliente=="2":
                    print("Regista los nuevos datos")
                    matricula=input("Matricula: ")
                    marca=input("Marca: ")
                    modelo=input("modelo: ")
                    color=input("color: ")
                    nif=input("Nif: ")
                    object_auto=autos.Autos.actualizar(matricula,marca, modelo,color,nif)
                    if object_auto:
                        print("Se actualizo cliente")
                    else:
                        print("No se pudo hacer actualizacion")


                elif op_cliente=="3":
                   
                    registro=autos.Autos()
                    if len(registro)>0:
                        for fila in registro:
                            print(f"Matricula: {fila[0]} \n  Marca: {fila[1]} \n  Modelo: {fila[3]} \n  color: {fila[4]} \n nif: {fila[5]} ")
                        else:
                            print("No hay registros")

                elif op_cliente=="4":
                    nif_n=input("Matricula del cliente:")
                    resultado=autos.Autos.eliminar(nif_n)
                    if resultado:
                        print("Se elimino el auto")
                    else:
                        print("No se pudo eliminar")
                else:
                    break
        elif op=="3":
            while True:
                print(""".::::Revision::::.
              1-Registrar Revision
              2-actualizar Revision
              3-Ver Registros
              4-Eliminar
                        """)
                op_rev=input("Selecciona una opcion: ")
                if op_rev=="1":
                    no_revision=input("\t Número de revisión: ")
                    cambiofiltro=input("\t Cambio filtro (S/N): ")
                    cambioaceite=input("\t Cambio aceite (S/N): ")
                    cambiofrenos=input("\t Cambio frenos (S/N): ")
                    otros=input("\t Otros: ")
                    matricula=input(("\t Matricula: ")) 
                    objeto_auto=autos.Autos(no_revision,cambiofiltro, cambioaceite,cambiofrenos,otros,matricula)
                    resultado=objeto_auto.insertar()

                    if resultado:
                        print("Se hizo el registro")
                    else:
                        print("No se pudo hacer el registro")

                elif op_rev=="2":
                    print("Regista los nuevos datos")
                    no_revision=input("\t Número de revisión: ")
                    cambiofiltro=input("\t Cambio filtro (S/N): ")
                    cambioaceite=input("\t Cambio aceite (S/N): ")
                    cambiofrenos=input("\t Cambio frenos (S/N): ")
                    otros=input("\t Otros: ")
                    matricula=input(("\t Matricula: ")) 
                    objeto_auto=autos.Autos.actualizar(cambiofiltro, cambioaceite,cambiofrenos,otros,matricula,no_revision)
                    if object_auto:
                        print("Se actualizo el registo")
                    else:
                        print("No se pudo hacer actualizacion")


                elif op_rev=="3":
                   
                    registro=revisiones.Revision.consultar()
                    if len(registro)>0:
                        for fila in registro:
                            print(f"No. Revision: {fila[0]} \n  Cambio de filtros: {fila[1]} \n  cambio de aceite: {fila[3]} \n  cambio de frenos: {fila[4]} \n otros: {fila[5]} \n Matriculas: {fila[6]}")
                        else:
                            print("No hay registros")

                elif op_rev=="4":
                    no_revision=input("Matricula del cliente:")
                    resultado=revisiones.Revision(nif_n)
                    if resultado:
                        print("Se elimino el registro")
                    else:
                        print("No se pudo eliminar")
                else:
                    break
        else:
            break

if __name__ == "__main__":
  menu_principal()
        

    

                
                