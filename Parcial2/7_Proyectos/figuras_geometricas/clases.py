import os
import math

class Figuras:
    def __init__(self, x, y, visible, mostrar):
        self.x = x
        self.y = y
        self.visible = visible
        

    def getxValor(self):
        return self.x
    
    def getyValor(self):
        return self.y
    
    def setxValor(self, x):
        self.x = x

    def setyValor(self, y):
        self.y = y

    def mostrar(self):
        return self.mostrar
    
    def estaVisible(self):
        return self.visible
   
    def ocultar(self):
        os.system("clear") 

    def calcularArea(self):
        pass

class Rectangulo(Figuras):
    def __init__(self, x, y, visible, alto, ancho):
        super().__init__(x, y, visible)
        self._alto = alto
        self._ancho = ancho
    
    def getAncho(self):
        return self.ancho
    
    def setAncho(self, ancho):
        self.ancho = ancho

    def getAlto(self):
        return self.alto
    
    def setAlto(self, alto):
        self.alto = alto
    
    def calcularArea(self):
        return self.alto * self.ancho
        
    def getInfo(self):
        print(f"x={self.getxValor()}, y={self.getyValor()}, visible={self.estaVisible()}, alto={self.getAlto()}, ancho={self.getAncho()}")

class Circulos(Figuras):
    def __init__(self, x, y, visible, radio):
        super().__init__(x, y, visible)
        self._radio = radio

    def getRadio(self):
        return self.radio
    
    def setRadio(self, radio):
        self.radio = radio

    def calcularArea(self):
        return math.pi * (self.radio ** 2)
    
    def getInfo(self):
        print(f"x={self.getxValor()}, y={self.getyValor()}, visible={self.estaVisible()}, radio={self.getRadio()}")
