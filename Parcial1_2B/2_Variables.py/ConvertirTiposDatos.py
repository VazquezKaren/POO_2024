"""
Comentario de varias lineas
Nota:Cuando se imprime en pantalla una cadena de caracteres
se trabaja por default con "cadenas", es decir python no
puede concatenar ota cosa que no sea un String (str)

"""

texto="soy una caden de caracteres"
numero=23

#Concatenar str con str

print("soy otra cadena y "+texto)

#Concatenar str con int

numero_str=str(numero)
print("El numero: "+numero_str)

print("El numero: "+str(numero))

#Concatener int con str

n1=int('23')
n2=33

suma=(n1+n2)
 
print("La suma es: "+str(suma))

print(f"La suma es: ,{suma}")

#Concatener float y int con str
#Int puede estar en un float pero no un float en int

n1=23.99
n2=33.0

suma=float(n1)+n2
 
print(f"La suma es: ,{suma}")
