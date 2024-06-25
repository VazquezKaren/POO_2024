#Ejemplo 1 Crear una clase (un molde para crear mas objetos) llamada coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similiares.


from typing import Any


class Coches:
    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #Valores iniciales es posible declarar al principio de una clase

    marca="Ferrari"
    color="rojo"
    modelo="2010"
    velocidad=300
    caballaje=500
    plazas=2


    #Metodos o acciones funciones que hace el objeto

    def acelerar(self):
        self.velocidad+=1

    def frenar(self):
        self.velocidad-=1

    def getColor(self):#da un valor (get)
        return  self.color
    
    def setColor(self,color):#set recibe parametro
        self.color=color

    def getMarca(self):
        return self.marca
    
    def setMarca(self,marca):
        self.marca=marca

    def getModelo(self):
        return self.modelo
    
    def setModelo(self,modelo):
        self.modelo=modelo

    def getVelocidad(self):
        return self.velocidad
    
    def setVelocidad(self, velocidad):
        self.velocidad=velocidad
    
    def getCaballaje(self):
        return self.caballaje
    
    def setCaballaje(self,caballaje):
        self.caballaje=caballaje
    
    def getPlazas(self):
        return self.plazas
    
    def setPlazas(self, plazas):
        self.plazas=plazas 
    
    def getInfo(self):
        print(f" Marca: {self.getMarca()}\n color:{self.getColor()}\n Modelo: {self.Modelo()} \n Velocidad: {self.getVelocidad()}\n Caballaje: {self.getCaballajetCaballaje()}\n Plazas: {self.getPlazas()}")

    
    def setInfo(self, info):
        self.info=info

        





#Fin definir clase

#Crear un objetos o instanciar la clase
print("Objeto 1")
coche1=Coches()
coche1.getInfo()

#Mostrar los valores inicales del objeto o instancia de la clase
# print(f"Marca: {coche1.marca} {coche1.color}, numeros de plazas: {coche1.plazas} \nModelo: {coche1.modelo} con una velocidad de {coche1.velocidad} Km/h y un potencia de {coche1.caballaje} hp")

#Acelerar la velocidad del coche de 300 a 301
coche1.acelerar()
print(f"La nueva velocidad es: {coche1.velocidad}")

#Disminuir la velocidad del coche de 301 a 100

for i in range(1,202):
   coche1.frenar()

print(f"La nueva velocidad del coche es: {coche1.velocidad}")







# Crear los metodos setters y getters: estos metodos son importantes y necesarios en todos clases para que el programador interactue con los valores de los atributos a traves de estos metodos... digamos que es la manera mas adecuada y recomendada para solicitar un valor (get) y /o para ingresar o cmabiar un valor (set) a un atributo en particular de la clase a traves de un objeto.

#En teoria se deberia decrear un metodo Gaetter y Setter por cada atrivuto que contenga la clase
#Los metodos get isempre regresan valor es decir el valor del la propiedad a traves del return 
#Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion

#para crear multiples objetos es necesario hacer  varias instancias de la clase'
print("Objeto 3")
coche3=Coches()

coche3=Coches()
coche3.setColor("Azul")
coche3.setModelo("2024")
coche3.setMarca("Lancer")
coche3.setVelocidad("220")
coche3.setCaballaje("300")
coche3.setPlazas("5")

coche3.getInfo()
