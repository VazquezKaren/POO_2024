#Los errores de excepciones en un lenguaje de programacion no es otrea cosa que los errores en tiempo de ejecucion. Cuando se manejan los errores mediante la excepcione en realidad se dice que se evita que se presenten esos errores en programa en tiempo de ejecucion 


# Ejemplo se presenta un error cuando no es generada una variable


# try:
    
#     nombre=input("Dame el nombre completo de una persona")
#     if len (nombre)>0:
#         nombre_ususario="El nombre del usuario del sistema es: "+nombre

#     print(nombre_ususario)
# except:
#     print("Es necesario introducir un Nombre de una persona ")

#Ejemplo 2 : Cuando se solicita un numero y se ingresa otra cosa



# try:
#     numero=int(input("Dame un numero: "))

#     if numero>0:
#         print("soy un numero entero positivo")

#     else:
#         print("soy un numero negativo")
# except ValueError:
#     print("No es posible convertir una letra a un numero: ")


#Ejemplo 3 Cuando se genera multiples excepciones
try:
    numero=int(input("Dame un numero: "))

    print("El cuadrado del numero es: "+ str(numero*numero))

except TypeError:
    print("Es necesario convertir el numero a entero: ")

except ValueError:
    print("No es posible convertir una letra a un numero: ")
else:#siempre y cundo no hay error en el try
    print("todo se ejecuato sin errores")

finally:
    print("Ya termino")

