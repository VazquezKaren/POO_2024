"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
   1.- Funcion que no recibe parametros y no regresa valor
   2.- Funcion que no recibe parametros y regresa valor
   3.- Funcion que recibe parametros y no regresa valor
   4.- Funcion que recibe parametros y regresa valor

"""

#Ejemplo 1 Crear una funcion para imprimir nombres de personas
#    1.- Funcion que no recibe parametros y no regresa valor 
def solicitarNombres():
   nombre=input("Ingresa el nombre completo: ")


#Ejemplo 2 sumar dos numeros
def suma():
    n1=int(input("Numero #1: "))
    n2=int(input("Numero #2: "))
    suma=n1+n2
    print(f"{n1}+{n2}={suma}")

#Ejemplo 3 sumar dos numeros 
#2.- Funcion que no recibe parametros y regresa valor
def suma():
    n1=int(input("Numero #1: "))
    n2=int(input("Numero #2: "))
    suma=n1+n2
    return suma

resultado_suma=suma()
print(f"La suma es: {resultado_suma}")

#Ejemplo 4 sumar dos numeros 
# 3.- Funcion que recibe parametros y no regresa valor
def suma(num1,num2):
    suma=num1+num2
    print(f"La suma es: {suma}")

n1=int(input("Numero #1: "))
n2=int(input("Numero #2: "))
suma(n1,n2)

#Ejemplo 5 sumar dos numeros 
# 4.- Funcion que recibe parametros y regresa valor
def suma(num1,num2):
    suma=num1+num2
    return suma

n1=int(input("Numero #1: "))
n2=int(input("Numero #2: "))
resultado_suma=suma(n1,n2)
print(f"La suma es: {resultado_suma}")


#Ejemplo 6 Crear un programa que solicite a traves de una funcion la siguiente informacion: Nombre del Paciente, Edad, Estatura, Tipo de Sangre. Utilizar los 4 tipos de funciones

#ejemplo 1
def infoPaciente():
    nombre=input("Ingresa el nombre del paciente: ")
    edad=input("Edad del paciente:")
    estatura=input("Estatura del paciente: ")
    tipoSangre=input("Tipo de sangre del paciente: ")

#ejemplo 2
def infoPciente():
    nombre=input("Ingresa el nombre del paciente: ")
    edad=input("Edad del paciente:")
    estatura=input("Estatura del paciente: ")
    tipoSangre=input("Tipo de sangre del paciente: ")
    return infoPaciente

infodelPaciente=infoPaciente
print(f"El nombre del paciente es: {infoPaciente}")


#ejemplo 3
def infoPaciente(nombre,edad,estatura,tipoSangre):
    infoPaciente=[nombre,edad,estatura,tipoSangre]
    print(f"la informacion del paciente es:{infoPaciente}")

nombre=input("Ingresa el nombre del paciente: ")
edad=input("Edad del paciente:")
estatura=input("Estatura del paciente: ")
tipoSangre=input("Tipo de sangre del paciente: ")

infoPaciente(nombre,edad,estatura,tipoSangre)


#ejemplo 4


nombre=input("Ingresa el nombre del paciente: ")
edad=input("Edad del paciente:")
estatura=input("Estatura del paciente: ")
tipoSangre=input("Tipo de sangre del paciente: ")
info=infoPaciente(nombre,edad,estatura,tipoSangre)
print(f"La info del paciente es :{info}")









