
class Personas:
    def __init__(self, nombre, edad, tel):
        self.nombre=nombre
        self.edad=edad
        self.tel=tel
    def getInfo(self):
        print(f"Informacion de la persona: {self.getNombre(), self.getEdad(),self.getTel()}")



    def getNombre(self):
        return self.nombre
    
    def setNombre(self,nombre):
        self.nombre=nombre

    def getEdad (self):
        return self.edad
    
    def setEdad (self,edad):
        self.edad=edad

    def getTel (self):
        return self.tel
    
    def setTel (self, tel):
        self.tel=tel

class Estudiantes(Personas):
    def __init__(self, nombre, edad, tel, carrera, matricula):
        super().__init__(nombre, edad, tel)
        self.__carrera=carrera
        self.__matricula=matricula
        
    def getCarreta(self):
        return self.__carrera
    
    def setCarreta(self,carrera):
        self.__carrera=carrera
    
    def getMatricula (self):
        return self.__matricula
    
    def setMatricula (self, matricula):
        self.__matricula=matricula

    def getInfo(self):
        print(f"Informacion de la persona: {self.getNombre(), self.getEdad(),self.getTel()} La carrera es:{self.getCarreta()}, la matricula es:{self.getMatricula()}")


class Docente(Personas):
    def __init__(self, nombre, edad, tel, modalidad, numEmpleado):
        super().__init__(nombre, edad, tel)

        self._modalidad=modalidad
        self._numEmpleado=numEmpleado

    def getModalidad(self):
        return self._modalidad
    def setModalidad(self,modalidad):
        self._modalidad=modalidad
    def getNumEmpleado(self):
        return self._numEmpleado
    def setNumEmpleado(self,numEmpleado):
        self._numEmpleado=numEmpleado

    def informarModalidad(self):
        print (f"Informacion de la persona: {self.getNombre(), self.getEdad(),self.getTel()}La modalidad es:{self.getModalidad()}")
    
        
    


