# Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for
#


# Cuadrado de los numeros del 1 al 10 con for
print("El cuadrado de los numeros naturales del 1 al 60 son:")
for x in range (1,61):
    resultado=x**2
    print(resultado)
x+=1

print("\n")


# Cuadrado de los numeros del 1 al 10 con while
print("El cuadrado de los numeros naturales del 1 al 60 son:")
x=1 
while x<61:
    resultado2=x**2
    print(resultado2)
    x+=1
