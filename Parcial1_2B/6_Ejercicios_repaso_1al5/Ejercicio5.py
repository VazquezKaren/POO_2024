#  Hacer un programa que muestre todos los numeros entre 2 numeros que diga el usuario

numero1=int(input("Ingresa el primer número:"))
numero2=int(input("Ingresa el segundo número:"))



if numero1>numero2:
    NumMayor=numero1
    NumMenor=numero2
else:
    NumMayor=numero2
    NumMenor=numero1

for num in range (NumMenor+1,NumMayor):
    print(num)
