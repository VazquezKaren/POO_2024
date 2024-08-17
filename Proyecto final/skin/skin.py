from conexionBD import*


class Skin:
    def __init__(self,nombre, userName, id_usuario,id_cuerpo, id_estilo, id_realm):
        self.__id_usuario=id_usuario
        self.__nombre=nombre
        self.__userName=userName
        self.__id_cuerpo=id_cuerpo
        self.__id_estilo=id_estilo
        self.__id_realm=id_realm

    def get_id_usuario(self):
        return self.__id_usuario
    def get_nombre(self):
        return self.__nombre
    def get_userName(self):
        return self.__userName
    def get_id_cuerpo(self):
        return self.__id_cuerpo
    def get_id_estilo(self):
        return self.__id_estilo
    def get_id_realm(self):
        return self.__id_realm
    

    def set_id_usuario(self, id_usuario):
        self.__id_usuario=id_usuario
    def set_nombre(self, nombre):
        self.__nombre=nombre
    def set_userName(self, userName):
        self.__userName=userName
    def set_id_cuerpo(self, id_cuerpo):
        self.__id_cuerpo=id_cuerpo
    def set_id_estilo(self, id_estilo):
        self.__id_estilo = id_estilo
    def set_id_realm(self, id_realm):
        self.__id_realm=id_realm


    def seleccionar_skin(self):
        try:
            cursor.execute(
                "INSERT INTO skin VALUES (NULL,%s,%s,%s,%s,%s,%s) ",
                (self.get_nombre(), self.get_userName(), self.get_id_usuario(),self.get_id_cuerpo(),self.get_id_estilo(),self.get_id_realm())
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False 
        
    def actualizar_skin(self):
        try:
            cursor.execute(
                "UPDATE skin SET nombre_usuario=%s, userName=%s, id_cuerpo=%s, id_estilo=%s WHERE id_usuario=%s",
                (self.__nombre, self.__userName, self.__id_cuerpo, self.__id_estilo, self.__id_usuario)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False
        
                
        
    def mostrar_skin(id):
        try:
            cursor.execute(
                "select * from skin where userName=%s",
                (id,)
            )
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al crear el realm: {e}")
            return None
    def mostrar_skinss():
        try:
            cursor.execute(
                "select * from skin"
            )
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al crear el realm: {e}")
            return None
        
    def eliminar_skin(id):
  
        try:
            cursor.execute(
                "DELETE FROM skin WHERE id=%s",
                (id,)
             )
            conexion.commit()
            return True
        except Exception as e:
            print(e)
            return False
    

      