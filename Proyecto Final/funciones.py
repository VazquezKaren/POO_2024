from datetime import datetime, timedelta

def borrarPantalla():
  import os  
  os.system("clear")

def esperarTecla():
  print("\n \t \t Oprima cualquier tecla para continuar ...")
  input()  

def fecha():
 fecha_actual = datetime.now()
 fecha_futura = fecha_actual + timedelta(days=30)
 



