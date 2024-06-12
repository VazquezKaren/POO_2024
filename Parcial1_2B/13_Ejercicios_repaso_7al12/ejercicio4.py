# 4.- 

#  Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
#   y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones



def variable():
    lista=[1,4,6,8]
    cadena="Ejercicios de Repaso"
    numentero=2
    logico=True
    return lista,cadena,numentero,logico


def tipo_variable (variable):
    return type(variable)

def imprimir (lista, cadena,numentero,logico):
    print(f"La variable {lista} es de tipo: {tipo_variable(lista)}")
    print(f"La variable {cadena} es de tipo: {tipo_variable(cadena)}")
    print(f"La variable {numentero} es de tipo: {tipo_variable(numentero)}")
    print(f"La variable {logico} es de tipo: {tipo_variable(logico)}")
    
lista, cadena, numentero, logico = variable()
imprimir(lista, cadena, numentero, logico)
    
    

