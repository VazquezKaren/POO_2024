from conexion import*
from empleados import empleados
from funciones import*

def menu_principal():
    while True:
                print("\n Menú de Opciones ")
                print("1. Crear empleado")
                print("2. ver empleados")
                print("3. Actualizar empleado")
                print("4. Eliminar empleado")
                print("5. Salir")
                opcion = input("Elige una opción: ")

                if opcion == '1':
                    nombre = input("Nombre: ")
                    direccion = input("Dirección: ")
                    telefono = input("Teléfono: ")
                    puesto = input("Puesto: ")
                    salario = input("Salario: ")
                    empleado1=empleados.Empleado(nombre, direccion, telefono, puesto, salario)
                    empleado1.agregar_empleado()
                    esperarTecla()
                    if empleado1:
                         print("Se hizo el registro con exito")
                         esperarTecla()
                    else:
                         print("No se puedo hacer el registro")
                         esperarTecla()

                elif opcion == '2':
                    id=input("Id del empleado que se quiere buscar: ")
                    empleado1 =empleados.Empleado.buscar_empleado(id)
                    if empleado1:
                        fila=empleado1[0]
                        id=fila[0]
                        print(f"ID: {fila[0]}, Nombre: {fila[1]}, Dirección: {fila[2]}, Teléfono: {fila[3]}, Puesto: {fila[4]}, Salario: {fila[5]}")
                        esperarTecla()
                    else:
                         print("No hay registros")

                elif opcion == '3':
                    id = input("ID del empleado a actualizar: ")
                    nombre = input("Nuevo nombre: ")
                    puesto = input("Nuevo puesto: ")
                    salario = input("Nuevo salario: ")
                    actualizacion=empleados.Empleado.actualizar_empleado(id, nombre, puesto, salario)
                  
                    if actualizacion:
                         print("Se actualizo la informacion con exito")
                         esperarTecla()
                    else:
                         print("No se pudo actualizar la informacion")
                         esperarTecla()

                elif opcion == '4':
                    id = input("ID del empleado a eliminar: ")
                    empleado=empleados.Empleado.eliminar_empleado(id)
                    if empleado:
                         print("Se elimino el registro con exito")
                         esperarTecla()
                    else:
                         print("No se logro eliminar el registro")
                         esperarTecla()
                elif opcion == '5':
                    print("Usted esta saliendo del programa")
                
                    break
                else:
                    print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    menu_principal()