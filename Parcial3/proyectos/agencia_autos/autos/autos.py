
from conexionBD import *

class Autos:
    def __init__(self, matriucula,marca,modelo,color,nif):
        self.matricula=matriucula
        self.marca=marca
        self.modelo=modelo
        self.color=color
        self.nif=nif

    def insertar(self):
        try:
            cursor.execute(
                "insert into autos values(%s,%s,%s,%s,%s)",
                (self.matricula,self.marca,self.modelo,self.color,self.nif)
            )
            conexion.commit()
            return True
        except:
            return False   

    @staticmethod
    def consultar():
        try:
            cursor.execute(
                "select * from autos"
        
            )
            return cursor.fetchall()#arreglo asociativo (tipo lista)
        except:
            
            return None    

    @staticmethod
    def actualizar(matricula,marca,modelo,color,nif):
       try:
         cursor.execute(
            "update autos set marca=%s,modelo=%s,color=%s,nif=%s where matricula=%s",
            (matricula,marca,modelo,color,nif)
         )
         conexion.commit()
         return True
       except:
         return False  

    @staticmethod
    def eliminar(matricula):
       try:
         cursor.execute(
            "delete from autos where matricula=%s",
            (matricula,)#()
         )
         conexion.commit()
         return True
       except:
         return False  
        
