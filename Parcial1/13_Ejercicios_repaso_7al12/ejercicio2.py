# Escribir un programa  que añada valores a una lista mientras que su longitud 
#  sea menor a 120, y luego mostrar la lista: Usar un while y for

listv=[]
for i in range(0,120):
    newnum=input(("Numero para agregar a lista"))
    listv.insert(len(listv), newnum)
    print(f"lista:{listv}")

list2=[]
x=0
while len(list2)<120:

    list2.append(input("Numero para agregar"))
    print(list2)

# i=1
# while i<=120:
#     valor=int(input(f"valor{i}"))
#     lista2.apped()
#     print(list2)