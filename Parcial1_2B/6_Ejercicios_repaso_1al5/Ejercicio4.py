#Solicitar 2 numeros al usuario
# y realizar todas las operaciones
# basicas de una calculadora (+,-,*,/)
# y mostrar por pantalla el resultado
# 


print("Ingresa dos números para realizar sus operaciones basicas:")
print("\n")

numero1=int(input("Ingresa el primer numero:"))
numero2=int(input("Ingresa el segundo numero:"))
ResultadoSum=numero1+numero2
ResultadoRest=numero1-numero2
ResultadoMult=numero1*numero2
ResultadoDiv=numero1/numero2
print("\n")

print("Las orperaciones basicas del los dos números ingresados son:")

print(f"{numero1} + {numero2} = {ResultadoSum}")

print(f"{numero1} - {numero2} = {ResultadoRest}")

print(f"{numero1} x {numero2} = {ResultadoMult}")

print(f"{numero1} / {numero2} = {ResultadoDiv}")

