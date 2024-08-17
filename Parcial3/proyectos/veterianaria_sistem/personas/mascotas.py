from conexionBD import*

class Animales():
    def __init__(self,id,nombre,raza,edad,historial,id_cliente):
        self.__id=id
        self.__nombre=nombre
        self.__raza=raza
        self.__edad=edad
        self.__historial=historial
        self.__id_cliente=id_cliente
    
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre
    
    def get_raza(self):
        return self.__raza
    
    def get_edad(self):
        return self.__edad
    
    def get_historial(self):
        return self.__historial
    
    def get_id_cliente(self):
        return self.__id_cliente
    
    def set_id (self, id):
        self.__id=id
    
    def set_nombre(self,nombre):
        self.__nombre=nombre

    def set_raza(self,raza):
        self.__raza=raza
    
    def set_edad(self,edad):
        self.__edad=edad
    
    def set_historial(self,historial):
        self.__historial=historial

    def set_id_cliente(self,id_cliente):
        self.__id_cliente=id_cliente


    def agregar_mascota(self):
        try:
            cursor.execute(
                "INSERT INTO mascotas VALUES (null,%s,%s,%s,%s,%s)",
                (self.get_nombre(),self.get_raza(), self.get_edad(),self.get_historial(),self.get_id_cliente())

            )
            conexion.commit()

            return True
        except:
            return False
    
    def eliminar_mascota(self):
        
       try:
         cursor.execute(
            "delete from mascotas where id=%s",
            (id,)
         )
         conexion.commit()
         return True
       except:
         return False  
       
    def mostrar_mascotas(id_cliente):
        try:
            cursor.execute(
                "select * from mascotas where id_cliente=%s",
                (id_cliente,)
            )
            return cursor.fetchall()
        except:
            
            return None
        
    def actualizar_mascota(id,historial):
        try:
            cursor.execute(
                "UPDATE mascotas SET historial=%s WHERE id=%s",
                (historial, id)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False

    
    
        

    