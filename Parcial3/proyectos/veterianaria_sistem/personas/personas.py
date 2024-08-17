from conexionBD import*
from funciones import*


class Persona:
    def __init__(self,nombre,direccion,telefono):
        
        self.__nombre=nombre
        self.__direccion=direccion
        self.__telefono=telefono
    
    def actualizarDatos(self,id_persona,nombre,direccion,telefono):
        pass

    # Getters
    def get_id(self):
        return self.__id_persona

    def get_nombre(self):
        return self.__nombre
    
    def get_direccion(self):
        return self.__direccion
    
    def get_telefono(self):
        return self.__telefono

    # Setters
    def ser_id (self,id_persona):
        self.__id_persona=id_persona

    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def set_direccion(self, direccion):
        self.__direccion = direccion
    
    def set_telefono(self, telefono):
        self.__telefono = telefono


class Cliente(Persona):
    def __init__(self, nombre, direccion, telefono,tipo):
        super().__init__( nombre, direccion, telefono)
        self.__tipo=tipo

        #getter
    def get_tipo(self):
        return self.__tipo
    
      # Setters
    def set_tipo(self, tipo):
        self.__tipo = tipo


    def agregar_cliente(self):
        try:
           
            cursor.execute(
                "INSERT INTO clientes VALUES (null,%s,%s,%s,%s)",
                (self.get_nombre(), self.get_direccion(), self.get_telefono(), self.get_tipo())
            )
            conexion.commit()
           
            return True
            
        except:
            return False
    @staticmethod
    def mostrar_cliente(id):
        try:
            cursor.execute(
                "SELECT * FROM clientes WHERE id = %s",
                (id,)
            )
            return cursor.fetchall()
        except:
            
            return None
    def actualizar_cliente(id,nombre,direccion,telefono):
        try:
            cursor.execute(
                "UPDATE clientes SET nombre=%s, direccion=%s, telefono=%s WHERE id=%s",
                (nombre,direccion,telefono, id)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False

    

class Empleado(Persona):
    def __init__(self, nombre, direccion, telefono,puesto, salario):
        super().__init__(nombre, direccion, telefono)
        self.__puesto=puesto
        self.__salario=salario

    #getter
    def get_puesto (self):
        return self.__puesto
    
    def get_salario(self):
        return self.__salario
    
    #setter

    def set_puesto(self,puesto):
        self.__puesto=puesto
    
    def set_salario(self,salario):
        self.__salario=salario

    
    def agregar_empleado(self):
        try:
            cursor.execute(
                "INSERT INTO empleados VALUES (null,%s,%s,%s,%s,%s)",
                (self.get_nombre(),self.get_direccion(), self.get_telefono(),self.get_puesto(),self.get_salario())

            )
            conexion.commit()

            return True
        except:
            return False
    def mostrar_empleado(id):
        try:
            cursor.execute(
                "select * from empleados where id=%s",
                (id)
            )
            return cursor.fetchall()
        except:
            
            return None
        
    @staticmethod
    def mostrar_empleados():
        try:
            cursor.execute("SELECT * FROM empleados")
            return cursor.fetchall()
        except Exception as e:
            print(e)
            return None
        
    def eliminar_empleado(id):
        try:
            cursor.execute(
                "DELETE FROM empleados WHERE id=%s",
                (id,)
             )
            conexion.commit()
            return True
        except Exception as e:
            print(e)
            return False
