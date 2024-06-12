
paises=["Mexico","USA","Brasil","Japon"]
numeros=[23,34,12.56,0.100,23]
texto=["Hola",True,23,3.141516]

# Ordenar una lista
# print(paises)
# paises.sort()
# print(paises)

# print(numeros)
# numeros.sort()
# print(numeros)

# # #No se puede
# # print(texto)
# # texto.sort()
# # print(texto)


# Añadir elementos
# print(texto)
# texto.insert(len(texto),"True")
# print(texto)
# texto.insert(len(texto),True)#insertar dato en una posicion especifica
# print(texto)
# texto.append(False)#se pone el dato al final
# print(texto)

# #Eliminar elementos
# print(numeros)
# numeros.remove(23)
# print(numeros)
# numeros.pop(0)
# print(numeros)


#Dar la vuelta a una lista
print(numeros)
numeros.reverse()# cambia del mayor a menor
print(numeros)

#buscar un dato dentro de una lista
respuesta="Brasil"in paises#regresa True 
print(respuesta)

#Cuantas veces aparece un valor dentro de una lista
print(numeros)
numeros.append(23)
cuantos=numeros.count(23)
print(f"El numero 23 se encontro : {cuantos}")

#Unir Listas
print(paises)
paises.extend(numeros)
print(paises)

#otra opcion ordenar
print(numeros)
numeros.sort()
print(numeros)
