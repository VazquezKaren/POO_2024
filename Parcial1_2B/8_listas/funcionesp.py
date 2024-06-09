peliculas=['Shrek','Luca','El Titanic','Harry Potter','Buscando a Nemo','Divergente','Soul']
posicion=0
nonencontre=True
def agregar (nuevaPeli):
    print(peliculas)
    nuevaPeli=input("Nueva Pelicula:")
    peliculas.append(nuevaPeli)
    return peliculas


def borrar (peliBorrar):
    print(peliculas)
    print(f"peliculas disponibles\n {peliculas}")
    peliBorrar=input("Que pelicula deseas borrar?")
    peliculas.remove(peliBorrar)
    return peliculas
        
def buscar (peliBuscar):
    posicion=0
    nonencontre=True
    print(peliculas) 
    peliBuscar=input("Que pelicula quieres buscar?")
    for i in peliculas:
            if peliBuscar==i:
                    print(f"La palabra{i} esta en la posicion{posicion}")
                    nonencontre=False
            posicion=posicion+1

            if nonencontre:
                 print("Esta pelicula no esta disponible")