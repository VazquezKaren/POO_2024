"""

List(Array)
son coleciones o conjunto de datos/valores bajo
un mismo nombre, para acceder a los valores se
hace con un indice numerico

Nota:sus valores si son modificables

La lista es una colecion ordenada y modificable. Permite miembros duplicados

"""
import os


# Ejemplo:crear una lista con datos numericos e imprimir el contenido

# lista=[23,34]
# print(lista)


# # recorre la lista con el for

# for i in lista:
#     print(i)

# # recorrer la lista
# i=0
# while i <=len(lista)-1:
#     print(lista[i])
#     i+=1


# # crear una lista de 4 palabras, solicitar una palabra y buscar la coincidendia en la lista e indicar si la encontro o no y en que posicion

# palabras=["UTD","2024","bye","UTD"]
# palabras_buscar=input("Ingresa la palabra")
# posicion=0
# nonencontre=True
# # for i in (palabras):
# #     if palabras_buscar==i:
# #         print (f"La palabra esta en {i}, en la posicion:{posicion}")
# #         nonencontre=False
       

# #     posicion= posicion+1

    

# # if nonencontre:
#     print(f"No encotre la palabra")

# i=0
# while i<len(lista):
#     if palabras_buscar== palabras[i]:
#         print (f"La palabra esta en {palabras_buscar}, en la posicion:{i}")
#         nonencontre=False
    
#     i+=1

    

# if nonencontre:
#     print(f"No encotre la palabra")


#ejemplo 3 Agregar elementos de una lista

# numeros=[23,24]
# print(numeros)

# #agregar un elemento
# numeros.append(100)
# numeros.insert(3,200)
# print(numeros)

# #elimina un elemento
# numeros.remove(100) #indica el elemento a borrar
# print(numeros)
# numeros.pop(2)#indicar la posicion a borrar
# print(numeros)

# # Ejemplo 4 crear una lista multidimensional (matriz) para almacenar los contactos telefonicos

# agenda=[["carlos", 6182334567],
#         ["Karin", 6182334568],
#         ["Leon", 6182334569],
#         ["pedro", 6181234578],
#  ]

# print(agenda)

# for i in agenda:
#     print(f"{agenda.index(i)+1}.-{i}")


#Ejemplo 5 Crear un programa que permita gestionar(administara) peliculas,colocar un menu de opciones para agregar,remover, consultar peliculas.

# 1-Utilizar funciones y mandar llamar desde otro archivo
# 2-Utilizar listas para almacenar los nombres de peliculas


from funcionesp import*
peliculas=['Shrek','Luca','El Titanic','Harry Potter','Buscando a Nemo','Divergente','Soul']
posicion=0
nonencontre=True

# def agregar (nuevaPeli):
#     print(peliculas)
#     nuevaPeli=input("Nueva Pelicula:")
#     peliculas.append(nuevaPeli)
#     return peliculas


# def borrar (peliBorrar):
#     print(peliculas)
#     print(f"peliculas disponibles\n {peliculas}")
#     peliBorrar=input("Que pelicula deseas borrar?")
#     peliculas.remove(peliBorrar)
#     return peliculas
        
# def buscar (peliBuscar):
#     posicion=0
#     nonencontre=True
#     print(peliculas) 
#     peliBuscar=input("Que pelicula quieres buscar?")
#     for i in peliculas:
#             if peliBuscar==i:
#                     print(f"La palabra{i} esta en la posicion{posicion}")
#                     nonencontre=False
#             posicion=posicion+1

#             if nonencontre:
#                  print("Esta pelicula no esta disponible")

def esperaTecla():
    print("Presiona cualquier tecla para contiunar") 
    input()

while peliculas:
    os.system("clear")
    print("\n\t Peliculas Disponibles \n 1-.Shrek\n 2-.Luca \n 3-.Titanic \n 4-.Harry Potter \n 5-. Buscando a Nemo \n 5.Divergente \n 6-.Soul")

    print("\n\t..::: Herramientas :::... \n 1-.Agregar \n 2-.Remover \n 3-.Buscar \n ")

    peli_editar=input("Ingresa herramienta que se quiere usar")
    

    if peli_editar=="Agregar" or peli_editar=="1":
        peliculas=agregar(peliculas)
        print(f"Actualizacion de peliculas \n{peliculas}")
        esperaTecla()
        

    elif peli_editar=="Remover" or peli_editar=="2":
        peliculas=borrar(peliculas)
        print(f"Actualizacion de peliculas\n{peliculas}")
        esperaTecla()

    elif peli_editar=="Buscar" or peli_editar=="3":
        peliculas=buscar(peliculas)
    else:
         print("opcion no encontrada")


         
    
    
        













    
    

