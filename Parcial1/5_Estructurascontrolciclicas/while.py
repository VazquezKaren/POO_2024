#El ciclo while es una estructura de control que itera o repite la ejecuciòn de una serie de una serie de instrucciones tantas veces co o la condicion se cumpla 'True'
# Sintaxi:
# While condicion
#     bloque de instruccion

# Ejemplo 2 crear n jprograma que imprima los numeros del al 5, los sume y al final imprima la suma


contador=1
while contador<5:
    print("@")
    contador+=1

# Ejemplo 3 crear un programa que solicite un numero entero y a continuacion imprima la tabla de multiplicar correspondiente

contador=1
while contador<=5:
    print(contador)
    suma=+contador
    contador+=1
print(f"La suma es:{suma}")

# Ejemplo 3 crear un programa que solicite un numero entero y a continuacion imprima la tabla de multiplicar correspondiente

numero=int(input("Ingresa un numero:"))
multi=0
i=1
while i<11:
    multi=i*numero
    print(f"{numero} X {i} = {multi}")
    i+=1
