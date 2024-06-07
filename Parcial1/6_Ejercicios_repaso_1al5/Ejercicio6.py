# Mostrar todas las tablas del 1 al 10. Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10

for i in range (1,11):
    print("\n")
    print(f"Tabla de multiplicar {i}")
    
    for x in range (1,11):
        Result=i*x

        print(f"{i} x {x} = {Result}")
