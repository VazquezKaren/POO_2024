from conexionBD import*

class estilo_skin:
    def __init__(self,playera,pantalon,zapatos,accesorios,armas):
        self.playera=playera
        self.pantalon=pantalon
        self.zapatos=zapatos
        self.accesorios=accesorios
        self.armas=armas

    def crear_estilo(self):
        try:
            cursor.execute(
                "INSERT INTO estilos VALUES (NULL,%s,%s,%s,%s,%s) ",
                (self.playera,self.pantalon,self.zapatos,self.accesorios,self.armas)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al crear el realm: {e}")
            return False
        
    def mostrar_estilos():
        try:
            cursor.execute(
                "select * from estilos"
            )
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al crear el realm: {e}")
            return None
        
    def editar_estilos(id, playera,pantalon,zapatos,accesorios,armas):
        try:
            cursor.execute(
                "UPDATE estilos SET playera=%s, pantalon=%s, zapatos=%s, accesorios=%s, armas=%s  WHERE id=%s",
                (playera,pantalon,zapatos,accesorios,armas, id)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al editar el cuerpo: {e}")
            return False
        
    def eliminar_estilo(id):
  
        try:
            cursor.execute(
                "DELETE FROM estilos WHERE id=%s",
                (id,)
             )
            conexion.commit()
            return True
        except Exception as e:
            print(e)
            return False

        

    


