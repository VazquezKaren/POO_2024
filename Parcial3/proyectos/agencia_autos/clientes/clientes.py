
from conexionBD import *

class clientes:
    def __init__(self,nif,nombre,direccion,ciudad,tel):
       self.nif=nif
       self.nombre=nombre
       self.direccion=direccion
       self.ciudad=ciudad
       self.tel=tel

        
    def insertar(self):
        try:
            cursor.execute(
                "insert into clientes values(%s,%s,%s,%s,%s)",
                (self.nif,self.nombre,self.direccion,self.ciudad,self.tel)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False  

    @staticmethod
    def consultar():
        try:
            cursor.execute(
                "select * from clientes"
        
            )
            return cursor.fetchall()#arreglo asociativo (tipo lista)
        except:
            
            return None    

    @staticmethod
    def actualizar(nif,nombre,direccion,ciudad,tel):
       try:
         cursor.execute(
            "update clientes set nombre=%s,direccion=%s,ciudad=%s,tel=%s where nif=%s ",
            (nombre,direccion,ciudad,tel,nif)
         )
         conexion.commit()
         return True
       except:
         return False  

    @staticmethod
    def eliminar(matricula):
       try:
         cursor.execute(
            "delete from clientes where nif=%s",
            (matricula,)#()
         )
         conexion.commit()
         return True
       except:
         return False  

    def iniciar_sesion(nombre,telefono):
            
        try:
            cursor.execute(
            "select * from clientes where nombre=%s and tel=%s",
            ( nombre,telefono)
        )
        
            usuario=cursor.fetchone()
        
            if usuario:
                return usuario
            else:
                return []   
        except:    
            return []
        
        
