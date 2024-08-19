from conexionBD import*

class cuerpo_skin:
    def __init__(self,genero,base,cabello,ojos):
        self.genero=genero
        self.base=base
        self.cabello=cabello
        self.ojos=ojos

    def crear_cuerpo(self):
        try:
            cursor.execute(
                "INSERT INTO cuerpo VALUES (NULL,%s,%s,%s,%s) ",
                (self.genero,self.base,self.cabello,self.ojos)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al crear el realm: {e}")
            return False
        
    def mostrar_cuerpo():
        try:
            cursor.execute(
                "select * from cuerpo"
            )
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al crear el realm: {e}")
            return None
    def editar_cuerpo(id, genero, base, cabello, ojos):
        try:
            cursor.execute(
                "UPDATE cuerpo SET genero=%s, color_base=%s, cabello=%s, ojos=%s WHERE id=%s",
                (genero, base, cabello, ojos, id)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al editar el cuerpo: {e}")
            return False
        
    def eliminar_cuerpo(id):
  
        try:
            cursor.execute(
                "DELETE FROM cuerpo WHERE id=%s",
                (id,)
             )
            conexion.commit()
            return True
        except Exception as e:
            print(e)
            return False

        

    