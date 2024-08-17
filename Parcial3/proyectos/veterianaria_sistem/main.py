from funciones import*
from personas import personas
from citas import cita
from servicios import servicios
from personas import mascotas
from servicios import citas

def menu_principal():
    while True:
        borrarPantalla()
        print("""

            >>>>>>> MENU PRINCIPAL<<<<<<<<
        1-Cliente y/o mascota
        2-Empleados
        3-Citas
        4-Servicios
        
                   
        """)

        opcion=input("Elige una opcion")

        if opcion== "1":  
            print("""
                
                  1-Agregar Cliente Nuevo
                  2-Agregar una mascota
                  3-Ver informacion del cliente y mascota
                  4-Actualizar Informacionde Cliente o mascota
                  5-Eliminar Mascota
                """)
            op_reg=input("Elige una opcion:")

            if op_reg=="1":
                print("\n \t \t Datos del cliente:")     
                nombre_cliente=input("Nombre del cliente:")
                direccion_cliente=input("Direccion:")
                telefono_cliente=input("Telefono:")
                tipo_cliente=input("Tipo de cliente")

                obj_cliente=personas.Cliente(nombre_cliente,direccion_cliente,telefono_cliente,tipo_cliente)
                resultado=obj_cliente.agregar_cliente()
                
                if resultado:
                    print(f"\n\t {nombre_cliente} se registro correctamente")
                else:
                    print(f"\n\t ** Por favor intentalo de nuevo, no fue posible insertar el registro ** ...")    
                esperarTecla()
            

            elif op_reg=="2":
                otra_mascota = "si"
                while True:
                    nombre_mascota=input("Nombre de la mascota:")
                    raza_mascota=input("Raza:")
                    edad=input("edad:")
                    historial=input("historial:")
                    id_cliente=input("ID del cliente:")
                        
                    obj_mas=mascotas.Animales(nombre_mascota,raza_mascota,edad,historial,id_cliente)
                    resultado=obj_mas.agregar_mascota()
                    
                    if resultado:
                        print(f"\n\t {nombre_mascota} se registro correctamente")
                        esperarTecla()
                        otra_mascota=input("Desea agregar otra mascota (si/no)?")
                        if otra_mascota=="no":
                            break
                    else:
                        print(f"\n\t ** Por favor intentalo de nuevo, no fue posible insertar el registro ** ...")    
                    esperarTecla()

                    if otra_mascota=="no":
                        break
            
            elif op_reg=="3":
                id = input("Id del cliente:")
                info_cliente=personas.Cliente.mostrar_cliente(id)
                

                if info_cliente:
                    print("Informacion del cliente:")
                    esperarTecla()

                    fila=info_cliente[0]
                    id_cliente=fila[0]
                    print(f"ID del cliente: {fila[0]} \n Nombre: {fila[1]} \n Direccion: {fila[2]} \n Telefono: {fila[3]} \n Tipo: {fila[4]}")
                    esperarTecla()
                    
                    info_mascota=mascotas.Animales.mostrar_mascotas(id_cliente)
                    if info_mascota:
                        print ("Informacion de la mascota")
                        esperarTecla()

                    

                        for mascota in info_mascota:

                            if len (mascota)>=6:
                                print(f"Id de la mascota:{mascota[0]} \n Nombre: {mascota[1]} \n Raza: {mascota[2]} \n Edad: {mascota[3]} \n Historial: {mascota[4]} \n Id del cliente: {mascota[5]}")
                                esperarTecla()
                            else:
                                print("No hay datos de la mascota")
                                esperarTecla()
                    else:
                        print("El cliente no tiene mascotas registradas")
                        esperarTecla()
                    
                else:
                    print(f"Cliente no encontrado")
                    esperarTecla()

            elif op_reg=="4":
                
                actualizar_mas_per=input("Desea Actualizar datos de la Mascota o Cliente?").lower()
                esperarTecla()

                if actualizar_mas_per== "mascota":
                    id=input("Cual es el Id de la mascota que desea actualizar? ")
                    historial=input("Historial de la mascota? ")
                    
                    
                    resultado_m=mascotas.Animales.actualizar_mascota(id,historial)

                    if resultado_m:
                        print(f"\n\t Los datos se actualizaron con exito")
                    else:
                        print(f"\n\t No se pudo hacer la actualizacion vuelva a intentarlo ")

                if actualizar_mas_per== "cliente":
                    id=input("Cual es el Id del cliente que desea actualizar? ")
                    nombre=input("Cual es el nombre del cliente:")
                    direccion=input("Cual es la direccion del cliente:")
                    telefono=input("Telefono del cliente:")

                    resultado_c=personas.Cliente.actualizar_cliente(id,nombre,direccion,telefono)
                    if resultado_c:
                        print(f"\n\t Los datos se actualizaron con exito")
                        esperarTecla()
                    else:
                        print(f"\n\t No se pudo hacer la actualizacion vuelva a intentarlo ")
                        esperarTecla()
                else:
                    print("opcion no disponible")
                    esperarTecla()




                    
            elif op_reg=="5":
                while True:
                    id=input(" id de la mascota a eliminar: ")
                    resultado=mascotas.Animales.eliminar_mascota(id)
                    if resultado:
                        print(f"\n \t \t .:: Se borro el registro con Exito ::. ")
                        eliminar_mascota=input("Desea eliminar una mascota (si/no)?")
                        if eliminar_mascota=="no":
                            break
                            
                    else:
                        print(f"\n \t \t  ** No fue posible borrar el registro ** ... ")  
                        

        elif opcion=="2":
                print("""Empleados:
                      1. Agregar empleado"
                      2. Ver empleados"
                      3. Eliminar empleado""")
                ac_empleado=input("Selecciona una opcion:")
                if ac_empleado=="1":
                    print("Datos del empleado:")     
                    nombre_empleado=input("Nombre del empleado:")
                    direccion_empleado=input("Direccion:")
                    telefono_empleado=input("Telefono:")
                    puesto=input("puesto del empleado")
                    salario=input("Pago por hora")

                    obj_emp=personas.Empleado(nombre_empleado,direccion_empleado,telefono_empleado,puesto,salario)
                    resultado=obj_emp.agregar_empleado()
                    if resultado:
                        print(f"\n\t {nombre_empleado} se registro correctamente")
                    else:
                        print(f"\n\t ** Por favor intentalo de nuevo, no fue posible insertar el registro ** ...")    
                    esperarTecla()
                elif ac_empleado=="2":
                    empleados=personas.Empleado.mostrar_empleados()
                    if empleados:
                        print("\nLista de empleados:")
                        for fila in empleados:
                            print(f"ID: {fila[0]}, Nombre: {fila[1]}, Dirección: {fila[2]}, Teléfono: {fila[3]}, Puesto: {fila[4]}, Salario: {fila[5]}")
                            esperarTecla()
                    else:
                        print("Error al mostrar la lista o no hay empleados registrados")
                        esperarTecla()

                elif ac_empleado == "3":
                    id = input("Ingrese el ID del empleado a eliminar: ")
                    resultado =personas.Empleado.eliminar_empleado(id)
                    if resultado:
                        print(f"\n\t El empleado con ID {id} fue eliminado correctamente")
                    else:
                        print(f" Por favor intentalo de nuevo")
                    esperarTecla()
            

        elif opcion=="3":
            print(""""
                  ..::::::::::Citas::::::::::...
                
                    1-Agendar una cita 
                    2-Mostrar todas las citas
                    3-Eliminar una cita
                  """)
            op_cita=input("Seleccione un numero")
            if op_cita=="1":
                fecha=input("Fecha de la cita en formato YYYY-MM-DD:")
                id_cliente=input("ID del cliente:")
                id_mascota=input("IDde la mascota:")
                id_empleado=input("ID del empleado que atendera la cita:")
                tipo_servicio=input("tipo de servicio:")

                obj_cita=citas.Cita(fecha,id_cliente,id_mascota,id_empleado,tipo_servicio)
                respuesta=obj_cita.agregar_cita()

                if respuesta:
                    print("Se agendo la cita con exito")
                    esperarTecla()
                else:
                    print("No se pudo registrar la cita")
                    esperarTecla()
            if op_cita=="2":
                citas_ver=citas.Cita.mostrar_cita()

                if len(citas_ver)>0:
                    print("Citas Agendadas")
                    num_cita=1
                    for fila in citas_ver:
                        print(f"Numero de consulta: {num_cita}\n Id:{fila[0]}\n Fecha:{fila[1]}\n Id del cliente: {fila[2]}\n Id de la mascota: {fila[3]} \n Id del empleado: {fila[4]}\n Tipo de servicio: {fila[5]}")
                        num_cita+=1
                        esperarTecla()
                else:
                    print("No hay registros de cita")
                    esperarTecla()
            if op_cita=="3":
                id=input("Id de la cita que se quiere eliminar:")
                resultado_e=citas.Cita.eliminar_cita(id)
                if resultado_e:
                    print("La cita se elimino con exito")
                    esperarTecla()
                else:
                    print("No se puedo eliminar la cita, vuelve a intentarlo")


            


            
        elif opcion=="4":
            print("""
                          Servicios
                  
                  Seleccione una opcion:

                  1-Mostrar consultas
                  2-Mostrar vacunas
                  3-Registrar consulta o vacuna
                  4-editar costo consultas
                  5-editar costo vacunas

                  """)
            opcion_ser=input("Elige una opcion:")

            if opcion_ser=="1":
                registro=servicios.Consulta.mostrar_consultas()
                if len(registro)>0:
                    print(f"\n\t\t Consultas disponibles: \n ")
                    num_consulta=1
                    for fila in registro:
                        print(f"\t Consulta {num_consulta} \n \n ID: {fila[0]}.- nombre: {fila[2]}  \n   Descripcion:{fila[4]} \n Costo: {fila[3]} \n Tipo: {fila[4]}\n\n")
                        num_consulta+=1
                else:
                    print(f"\n\t ** No hay registros.")

            elif opcion_ser=="2":
                registro=servicios.Vacunas.mostrar_vacunas()
                if len(registro)>0:
                    print(f"\n\t\t Vacunas disponibles: \n ")
                    num_consulta=1
                    for fila in registro:
                        print(f"\t Consulta {num_consulta} \n \n ID: {fila[0]}.- nombre: {fila[2]}  \n   Descripcion:{fila[4]} \n Costo: {fila[3]} \n Duracion: {fila[4]}\n\n")
                        num_consulta+=1
                else:
                    print(f"\n\t ** No hay registros.")

            elif opcion_ser=="3":
                print("Registro de vacunas o consulta")
                tipo=input("Desea registrar vacuna selecione 1 para consulta seleccione 2?: ")

                if tipo=="1":
                    nombre_vacuna=input("Nombre: ")
                    descripcion_vacuna=input("Descripcion: ")
                    costo_vacuna=input("Costo: ")
                    tipo_vacuna=input("Tipo de vacuna: ")
                    obj_vac=servicios.Vacunas(nombre_vacuna,descripcion_vacuna,costo_vacuna,tipo_vacuna)
                    resultado=obj_vac.administrar_vacunas()

                    if resultado:
                        print(f"La vacuna {nombre_vacuna} se registro correctamente")
                    else:
                      print("Error")
                    
                
                elif tipo=="2":
                    nombre_con=input("Nombre: ")
                    descripcion_con=input("Descripcion: ")
                    costo_con=input("costo: ")
                    duracion_con=input("Duracion en minutos: ")
                    obj_con=servicios.Consulta(nombre_con,descripcion_con,costo_con,duracion_con)
                    resultado=obj_con.agregar_consultas()
                    if resultado:
                        print(f"El registro {nombre_con} se realizo con exito")
                    else:
                        print("error vuelva a intentarlo")
                    


            elif opcion_ser=="4":
                borrarPantalla()
                print("Actualizacion del costo de las consultas")
            
                id = input("\t \t ID de la consulta a actualizar: ")
                costo=input("Nuevo costo: ")
                resultado=servicios.Consulta.actualizar_consultas(id,costo)
                if resultado:
                    print(f"\n \t \t  El costo se actualizo con Exito!! ")
                else:
                    print(f"\n \t \t No se pudo actualizar ")

    

if __name__ == "__main__":
  menu_principal()



                






                


        
