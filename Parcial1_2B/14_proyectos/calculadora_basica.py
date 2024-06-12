
import os
from funciones_compartir import*
# def solicitarDatos():

#    print("\n")
#    global n1,n2,ope
#    n1=(input("Numero #1: "))
#    n2=(input("Numero #2: "))
   

# def esperaTecla():
#     print("Presiona cualquier tecla para contiunar") 
#     input()


# def getCalculadora(num1,num2,operacion):
    
#     if operacion=="1" or operacion=="+" or operacion=="SUMA":
#         resultado=f"{num1}+{num2}={int(num1)+int(num2)}"
#     elif operacion=="2" or operacion=="-" or operacion=="RESTA":
#         resultado=f"{num1}-{num2}={int(num1)-int(num2)}"  
#     elif operacion=="3" or operacion=="*" or operacion=="MULTIPLICACION":
#         resultado=f"{num1}*{num2}={int(num1)*int(num2)}"        
#     elif operacion=="4" or operacion=="/" or operacion=="DIVISION":
#         resultado=f"{num1}/{num2}={int(num1)/int(num2)}"  
#     return resultado


opcion=True
while opcion:
    os.system("clear")
    print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.-Multiplicacion \n 4.- División \n 5.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()

    if opcion!='5':
        n1,n2=solicitarDatos()
        print(getCalculadora(n1,n2,opcion))
        esperaTecla()
    else:
        opcion=False
        print("gracias por utilizar el sistema")


        



    

