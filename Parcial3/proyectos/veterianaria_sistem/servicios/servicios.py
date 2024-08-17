from conexionBD import*
from funciones import*

class Servicios:
    def __init__(self,nombre,descripcion,costo):
        self.__nombre=nombre
        self.__descripcion=descripcion
        self.__costo=costo
    
    def get_nombre(self):
        return self.__nombre
    
    def get_descripcion(self):
        return self.__descripcion
    
    def get_costo(self):
        return self.__costo
    
    def set_nombre(self,nombre):
        self.__nombre=nombre

    def set_descripcion(self,descripcion):
        self.__descripcion=descripcion
    
    def set_costo(self,costo):
        self.__costo=costo

    def actualizar_costo(self):
        pass
    



class Vacunas(Servicios):
    def __init__(self, nombre, descripcion, costo, tipo):
        super().__init__(nombre, descripcion, costo)
        self.__tipo=tipo

    def get_tipo(self):
        return self.__tipo
    
    def set_tipo(self,tipo):
        self.__tipo=tipo

    def administrar_vacunas(self):
        try:
            cursor.execute(
                "INSERT INTO vacunas VALUES (null,%s,%s,%s,%s)",
                (self.get_nombre(),self.get_descripcion(),self.get_costo(),self.get_tipo())
            )
        
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod   
    def mostrar_vacunas():
        try:
            cursor.execute(
                "select * from vacunas"
            )
            return cursor.fetchall()
        except:
            
            return None
    def actualizar_vacunas(id,costo):
   
       try:
         cursor.execute(
            "update vacunas set costo=%s where id=%s",
            (costo,id)
         )
         conexion.commit()
         return True
       except:
         return False
        

class Consulta(Servicios):
    def __init__(self, nombre, descripcion, costo, duracion):
        super().__init__(nombre, descripcion, costo)
        self.__duracion=duracion

    def get_duracion(self):
        return self.__duracion
    
    def set_duracion(self,duracion):
        self.__duracion=duracion

    def agregar_consultas(self):
        try:
            cursor.execute(
                "INSERT INTO consultas VALUES (null,%s,%s,%s,%s)",
                (self.get_nombre(),self.get_descripcion(),self.get_costo(),self.get_duracion())
            )  
            conexion.commit()
            return True
        except:
            return False  
        
    def actualizar_consultas(id,costo):
   
       try:
         cursor.execute(
            "update consultas set costo=%s where id=%s",
            (costo,id)
         )
         conexion.commit()
         return True
       except:
         return False 
    @staticmethod  
    def mostrar_consultas():
        try:
            cursor.execute(
                "select * from consultas"
            )
            return cursor.fetchall()
        except:
            
            return None
    






