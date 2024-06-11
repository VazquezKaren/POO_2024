r=str(input("Desea hacer una captura?"))


if r.lower()== "si":
  N=int(input("Cuantos alumnos desea registrar?"))
  promediofina=0
  cont=0

  for x in range(N):
    for y in range(N):
        nombre=input("Nombre del Alumno: ")
        carrera=input("En que carrera esta: ")
        calif1=float(input("Calificacion del primer parcial: "))
        calif2=float(input("Calificacion del segundo parcial"))
        calif3=float(input("Calificacion del tercer parcial"))
        califproyecto=float(input("Calificacion del proyecto: "))

    promediopar=float((calif1+calif2+calif3)/3)
    califfinal=float((promediopar+califproyecto)/2)

  
    

  if califfinal>80:
      
      print(f"Alumno: {nombre}")
      print(f"El promedio de los 3 parciales es: {promediopar} ")
      print(f"La calificacion final es:{promediofina} ")
      print(f"Calificacion del proyecto: {califproyecto}")
      
    
  elif califfinal<80 and califproyecto>50:
      print(f"Alumno: {nombre}")
      print(f"El promedio de los 3 parciales es: {promediopar} ")
      print(f"La calificacion final es: ")
      print(f"Calificacion del proyecto: {califproyecto}")
      print("####presenta examen extraodinario") 
      

    
  promediof = promediofina / N
  print(f"El promedio final de los {N} alumnos es: {promediof}")
    
else:
  print("No hacer captura")


      
      



