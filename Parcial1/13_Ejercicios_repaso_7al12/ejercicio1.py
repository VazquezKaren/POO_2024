# 1.- 

#  Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

#  a.- Recorrer la lista y mostrarla
#  b.- hacer una funcion que recorra la lista de numeros y devuelva un string
#  c.- ordenarla y mostrarla
#  d.- mostrar su longitud
#  e.- buscar algun elemento que el usuario pida por teclado



listanum=[9,20,2,6,7,6,90,5]


for i in listanum:
    print(i)




def num_str (lista):
    x=""
    for i in lista:
        x += str(i) + " "

    return x.strip()

numeros_enstr=num_str(listanum)
print(f"Numeos en str: {numeros_enstr}")

listanum.sort()
print(f"La lista ordenada del menor al menor: {listanum}")

longitud=len(listanum)
print(f"la longitud de la lista es de: {longitud} numeros")


posicion=0
noesta=True
numbuscar=input("que numero quieres buscar: ")
for i in listanum:
    if numbuscar==i:
        print(f"el numero {i} si esta en la lista y esta en la posicion{posicion}")
        noesta=False
      
    posicion += 1
    
    if noesta:
            print("El numero no esta")





        






