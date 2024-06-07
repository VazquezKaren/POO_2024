# Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario

Numero1=int(input("Ingresa el numero 1: "))
Numero2=int(input("Ingresa el numero 2: "))

if Numero1>Numero2:
    Mayor=Numero1
    Menor=Numero2
else:
    Mayor=Numero2
    Menor=Numero1

for num in range (Menor+1,Mayor):
   if num%2 !=0:
       print(f"Los numeros pares entre {Menor} y {Mayor} son {num}:")
        

