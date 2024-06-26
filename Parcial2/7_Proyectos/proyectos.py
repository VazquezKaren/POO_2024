import os

class Figuras:
    
    def CalcularArea(self):
        pass

class Rectangulo(Figuras):
    def __init__(self, largo, ancho):
        self.ancho = ancho
        self.largo = largo

    def getAncho(self):
        return self.ancho
    
    def setAncho(self, ancho):
        self.ancho = ancho

    def getLargo(self):
        return self.largo
    
    def setLargo(self, largo):
        self.largo = largo
    
    def CalcularArea(self):
        return self.largo * self.ancho
    

class Circulo(Figuras):
    def __init__(self, radio):
        self.radio = radio

    def getRadio(self):
        return self.radio
    
    def setRadio(self, radio):
        self.radio = radio

    def CalcularArea(self):
        import math
        return math.pi * (self.radio ** 2)
    

class Triangulo(Figuras):
    def __init__(self, altura, base):
        self.base = base
        self.altura = altura

    def getBase(self):
        return self.base
    
    def setBase(self, base):
        self.base = base

    def getAltura(self):
        return self.altura
    
    def setAltura(self, altura):
        self.altura = altura
    
    def CalcularArea(self):
        return (self.base * self.altura) / 2
    
def esperaTecla():
    input("Presiona Enter para continuar...")

def CalculadorArea():
    while True:
        os.system("clear")  
        print("Opciones disponibles: \n 1-.Rectangulo \n 2-.Circulo \n 3-.Triangulo \n 4-.Salir")
        opcion = input("Ingresa el número de la figura o su nombre: ")

        if opcion == "1" or opcion.lower() == "rectangulo":
            largo = float(input("Medida del Largo: "))
            ancho = float(input("Medida del Ancho: "))
            rectangulo = Rectangulo(largo, ancho)
            print(f"El área del rectángulo es: {rectangulo.CalcularArea()} ")
            esperaTecla()

        elif opcion == "2" or opcion.lower() == "circulo":
            radio = float(input("Medida del Radio: "))
            circulo = Circulo(radio)
            print(f"El área del círculo es: {circulo.CalcularArea()} ")
            esperaTecla()

        elif opcion == "3" or opcion.lower() == "triangulo":
            base = float(input("Medida de la Base: "))
            altura = float(input("Medida de la Altura: "))
            triangulo = Triangulo(altura, base)
            print(f"El área del triángulo es: {triangulo.CalcularArea()} ")
            esperaTecla()

        elif opcion == "4" or opcion.lower() == "salir":
            break

        else:
            print("Opción no válida. Intenta de nuevo.")
            esperaTecla()

CalculadorArea()
