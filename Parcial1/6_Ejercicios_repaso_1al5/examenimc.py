print("Calcular IMC, INGRESA DATOS:")
r=str(input("Desea hacer una captura?"))


while True:
    if r=="si":
        N=int(input("Cuantas personas desea registrar?"))
        for x in range (N):

            peso=int(input("Ingresa peso:"))
            altura=float(input("Ingresa altura: "))

            imc=float((peso)/(altura*altura))
            if imc<18.5:
                print(f"El peso es: {peso}, Tu IMC es:{imc} Normal")
                print(f"Peso inferior al norma: Menos de 18.5, Normal:18.5-24.0, Peso superior al normal: 25.0-29.0, Obesidad: mas de 30.)")

            elif imc>18.5 and imc<24.9:
                print(f"El peso es: {peso}, Tu IMC es:{imc} Normal")
                print(f"Peso inferior al norma: Menos de 18.5, Normal:18.5-24.0, Peso superior al normal: 25.0-29.0, Obesidad: mas de 30.)")
            elif imc>25.0 and imc<29.0:
                print(f"El peso es: {peso}, Tu IMC es:{imc} Normal")
                print(f"Peso inferior al norma: Menos de 18.5, Normal:18.5-24.0, Peso superior al normal: 25.0-29.0, Obesidad: mas de 30.)")
            elif imc>30:
                print(f"El peso es: {peso}, Tu IMC es:{imc} Normal")
                print(f"Peso inferior al norma: Menos de 18.5, Normal:18.5-24.0, Peso superior al normal: 25.0-29.0, Obesidad: mas de 30.)")
            
        print(f"Total de capturas: {N}")
    
   
