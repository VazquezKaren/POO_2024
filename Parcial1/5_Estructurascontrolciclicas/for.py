# Es un ciclo interactivo que se ejecuta x veces deacuerdo a los valores numericos enteros establecidos
# Sintaxis:
# for variable in elemento_iterable(lista,rando,etc):
# bloque de instrucciones


# ejemplo 1 crear un programa que imprima 5 veces el caracter @

# contador=1
#imprime 5 veces el @ pq es del 1 al atntes del 6
for contador in range(1,6):
    print("@")

#Ejemplo 2 crear n jprograma que imprima los numeros del al 5, los sume y al final imprima la suma

suma=0
for numero in range(1,6):
    print(numero)
    suma+=numero
print(f"La suma es:{suma}")

# Ejemplo 3 crear un programa que solicite un numero entero y a continuacion imprima la tabla de multiplicar correspondiente


numero=int(input("Ingresa un numero:"))
multi=0
for i in range(1,11):
    multi=i*numero
    print(f"{numero} X {i} = {multi}")

    
 

