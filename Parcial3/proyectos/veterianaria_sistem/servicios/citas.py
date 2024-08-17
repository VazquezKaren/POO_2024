from conexionBD import*
class Cita():
    def __init__(self, fecha, id_cliente, id_animal, id_empleado, tipo_servicio):
        self.__fecha = fecha
        self.__id_cliente = id_cliente
        self.__id_animal = id_animal
        self.__id_empleado = id_empleado
        self.__tipo_servicio = tipo_servicio
    
   
    def get_fecha(self):
        return self.__fecha

    def get_id_cliente(self):
        return self.__id_cliente

    def get_id_animal(self):
        return self.__id_animal

    def get_id_empleado(self):
        return self.__id_empleado

    def get_tipo_servicio(self):
        return self.__tipo_servicio

    # Métodos setter
    def set_fecha(self, fecha):
        self.__fecha = fecha

    def set_id_cliente(self, id_cliente):
        self.__id_cliente = id_cliente

    def set_id_animal(self, id_animal):
        self.__id_animal = id_animal

    def set_id_empleado(self, id_empleado):
        self.__id_empleado = id_empleado

    def set_id_servicio(self, tipo_servicio):
        self.__tipo_servicio= tipo_servicio

    
    def agregar_cita(self):
        try:
            cursor.execute(
                "INSERT INTO citas VALUES(null,%s,%s,%s,%s,%s)",
                (self.get_fecha(),self.get_id_cliente(), self.get_id_animal(), self.get_id_empleado(), self.get_tipo_servicio())
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"El error es:{e}")
            return False
    @staticmethod  
    def mostrar_cita():
        try:
            cursor.execute(
                "select * from citas"
            )
            return cursor.fetchall()
        except:
            
            return None
       
    def eliminar_cita(id):
        try:
            cursor.execute(
                "delete from citas where id=%s",
                (id,)
            )
            conexion.commit()
            return True
        except:
            return False  
    



        