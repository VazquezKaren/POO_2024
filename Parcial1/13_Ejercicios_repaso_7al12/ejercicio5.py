# 5.- 
# Crear una lista y un diccionario con el contenido de esta tabla: 

#   ACCION              TERROR        DEPORTES
#   MAXIMA VELOCIDAD    LA MONJA       ESPN
#   ARMA MORTAL 4       EL CONJURO     MAS DEPORTE
#   RAPIDO Y FURIOSO I  LA MALDICION   ACCION

peliculasLista=[
    ("Maxima velocidad", "Arma Mortal 4","Rapido y Furioso I"),
    ("La Monja","El conjuro", "La maldicion"),
    ("ESPN","Mas Deporte","Accion")
]

print("Lista de peliculas:")
for fila in peliculasLista:
    print(fila)


diccionarioPeliculas = {
    "Accion": "Maxima velocidad, Arma Mortal 4, Rapido y Furioso I",
    "Terror": "La Monja, El conjuro, La maldicion",
    "Deportes": "ESPN, Mas Deporte, Accion"
}

for i in diccionarioPeliculas:
    print(f"{i} : {diccionarioPeliculas[i]}")