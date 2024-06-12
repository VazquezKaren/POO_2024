# 3.- 

# Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir el contenido de la lista en mayusculas

listal=[]

if not listal:
    print("La lista esta vacia")

    while True:
        a=(input("Agrega un dato a lo lista"))
        listal.append(a.upper())
        if a=="salir":
            break

        print(listal)




