from conexionBD import*
import hashlib
from funciones import*
import hashlib

class Realm:
    def __init__(self, nombre, tipo, codigo_invitacion,id_admin):
        self.__nombre=nombre
        self.__id_admin=id_admin
        self.__tipo=tipo
        self.__codigo_invitacion=codigo_invitacion

    def get_nombre(self):
        return self.__nombre
    
    def get_id_admin(self):
        return self.__id_admin
    
    def get_tipo(self):
        return self.__tipo
    
    def get_codigo_inv(self):
        return self.__codigo_invitacion
    
    def set_nombre(self,nombre):
        self.__nombre=nombre
    
    def set_id_admin(self, id_admin):
        self.__id_admin=id_admin
    
    def set_tipo(self,tipo):
        self.__tipo=tipo
    
    def set_codigo_inv(self, codigo_invitacion):
        self.__codigo_invitacion=codigo_invitacion
    def crear_realm(self):
        try:
            cursor.execute(
                "INSERT INTO realm VALUES (NULL,%s,%s,%s,%s) ",
                (self.get_nombre(), self.get_tipo(), self.get_codigo_inv(),self.get_id_admin())
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al crear el realm: {e}")
            return False
    
    @staticmethod
    def editar_realm(id_realm, nombre, tipo, codigo_invitacion):
        try:
            cursor.execute(
                "UPDATE realm SET nombre=%s, tipo=%s, codigo_inv=%s WHERE id=%s",
                (nombre, tipo, codigo_invitacion, id_realm)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al editar el realm: {e}")
            return False



    def eliminar_realm(id):
        
       try:
         cursor.execute(
            "delete from realm where id=%s",
            (id,)
         )
         conexion.commit()
         return True
       except Exception as e:
            print(e)
            return None 
    def mostrar_realms(id):
        try:
            cursor.execute(
                "SELECT * FROM realm"          
            )
            return cursor.fetchall()
        except Exception as e:
            print(e)
            return None
       
    import mysql.connector

try:
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bd_servidor'
    )
    cursor=conexion.cursor(buffered=True)
    print("se hizo la conexion")
except:
    print("No se pudo hacer la conexion")