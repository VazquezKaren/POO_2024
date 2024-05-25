"""
Exite una estructura de condicion llamada "if"
la cual evalua una condicion para encontrar el valor "True" o se cumple la condicion se ejecuta la linea o lineas codigo

Tienes 4 variantes del if

1.-if simple
2.-if compuesto
3.-if anidado
4.-if y elif

"""

#Ejemplo 1 if simple

color="rojo"
if color=="rojo":
  print("soy el color rojo")


#Ejemplo 2 if compuesto

color="rojo"
if color=="rojo":
  print("soy el color rojo")
else:
  print("No soy el color rojo")


#Ejemplo 3 if anidado if dentro de if

color="rojo"
if color=="rojo":
  print("soy el color rojo")
  if color!="rojo":
    print("soy otro color")

else:
  print("No soy el color rojo")
  if color!="rojo":
    print("soy otro color")

#Ejemplo 4 if con elif

color="rojo"
if color=="rojo":
  print("soy el color rojo")
elif color=="negro":
  print("Soy el color negro")
elif color=="azul":
  print("Soy el color azul")
else:
  print("No soy rojo, negro o azul")
  
  