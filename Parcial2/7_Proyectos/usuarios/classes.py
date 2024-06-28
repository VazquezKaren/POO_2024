
class Usuario:
    def __init__(self, nombre, direccion,telefono):
        self.nombre=nombre
        self.direccion=direccion
        self.telefono=int(telefono)

    def getNombre(self):
        return self.nombre
    
    def setNombre(self,nombre):
        self.nombre=nombre

    def getDireccion(self):
        return self.direccion
    
    def setDireccion(self,direccion):
        self.direccion=direccion

    def getTelefono (self):
        return self.telefono
    
    def setTelefon (self,telefono):
        self.telefono=telefono
    
    def getInfoUsuario (self):
        return print (f"Informacion del Usuario:\n Nombre:{self.getNombre()} \n Direccion: {self.getDireccion()}\n Telefono: {self.getTelefono()} ")
    

class Clientes(Usuario):
    def __init__(self, nombre, direccion, telefono, numCliente):
        super().__init__(nombre, direccion, telefono)
        
        self.__numCliente=int(numCliente)

    def getNumCliente(self):
        return self.__numCliente
    
    def setNumeroCliente(self, numCliente):
        self.__numCliente=numCliente

    def getInfoUsuario (self):
        return print (f"Informacion del Usuario:\n Nombre:{self.getNombre()} \n Direccion: {self.getDireccion()}\n Telefono: {self.getTelefono()} \n Numero de Cliente:{self.getNumCliente()}\n ")
    
class Empleados(Usuario):
    def __init__(self, nombre, direccion, telefono,salario,numeroEmpleado,tipo):
        super().__init__(nombre, direccion, telefono)
        self._salario_empleado=salario
        self._numero_Empleado=int(numeroEmpleado)
        self._tipo_empleado=tipo

    def getSalario(self):
        return self._salario_empleado
    def setSalario(self,salario):
        self._salario_empleado=salario

    def getNumeroEmpleado(self):
        return self._numero_Empleado
    def setNumeroEmpleado(self,numeroEmpleado):
        self._numero_Empleado=numeroEmpleado

    def getTipo(self):
        return self._tipo_empleado
    def setTipo(self,tipo):
        self._tipo_empleado=tipo
        
    def getInfoUsuario (self):
        return print (f"Informacion del Usuario: \n Nombre:{self.getNombre()} \n Direccion: {self.getDireccion()}\n Telefono: {self.getTelefono()} \n Salario:{self.getSalario()}\n Numero Empleado: {self.getNumeroEmpleado()}\n Tipo:{self.getTipo()}\n ")
            
    
    
