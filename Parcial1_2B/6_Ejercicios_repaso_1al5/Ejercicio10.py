# Crear un programa que solicite la calificacion de 15 alumnos e imprimir en pantalla cuantos aproboron y cuantos no aprobaron
AlumnosA=0
AlumnosN=0

for alum in range (1,16):
    
    califi=float(input(f"Ingresa la calificacion del alumno {alum}: "))

    if califi>=70:
        AlumnosA+=1
    else:
        AlumnosN+=1

print(f"Los alumnos que aprovaron son: {AlumnosA}")
print(f"Los alumnos reprobados son: {AlumnosN}")

    


