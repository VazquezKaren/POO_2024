# Hacer un programa que resuelva lo siguiente. ¿Cuanto es el X por ciento de X numero?

Numero=float(input("Ingresa un numero: "))
Porcentaje=float(input("Ingresa el porcentaje que quieres conocer: "))

PorcentajeC=(Porcentaje/100)
Total=Numero*(PorcentajeC)

print(f"El {Porcentaje} del número {Numero} es: ")
print(Total)

