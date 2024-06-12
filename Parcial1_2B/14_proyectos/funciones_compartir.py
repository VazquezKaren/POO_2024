def solicitarDatos():
   print("\n")
#    global n1,n2,ope
   n1=(input("Numero #1: "))
   n2=(input("Numero #2: "))
   return n1,n2

def esperaTecla():
    print("Presiona cualquier tecla para contiunar") 
    input()



def getCalculadora(num1,num2,operacion):
    
    if operacion=="1" or operacion=="+" or operacion=="SUMA":
        resultado=f"{num1}+{num2}={int(num1)+int(num2)}"
    elif operacion=="2" or operacion=="-" or operacion=="RESTA":
        resultado=f"{num1}-{num2}={int(num1)-int(num2)}"  
    elif operacion=="3" or operacion=="*" or operacion=="MULTIPLICACION":
        resultado=f"{num1}*{num2}={int(num1)*int(num2)}"        
    elif operacion=="4" or operacion=="/" or operacion=="DIVISION":
        resultado=f"{num1}/{num2}={int(num1)/int(num2)}"  
        return resultado
    
    



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