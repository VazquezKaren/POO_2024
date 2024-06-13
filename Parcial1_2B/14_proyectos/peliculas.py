from funciones_compartir import*
import os
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

    print("\n\t..::: Herramientas :::... \n 1-.Agregar \n 2-.Remover \n 3-.Buscar \n 4-.Consultar")

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
        esperaTecla()

    elif peli_editar=="Consultar" or peli_editar=="4":
        peliculas=Consultar(peliculas)
        esperaTecla()
    
    else:
         print("opcion no encontrada")


         
    
    
        













    
    

