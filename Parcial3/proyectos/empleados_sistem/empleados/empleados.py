from conexion import*



class Empleado:
    def __init__(self, nombre, direccion, telefono, puesto, salario):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__puesto = puesto
        self.__salario = salario
       
       

    def get_nombre(self):
        return self.__nombre

    def get_direccion(self):
        return self.__direccion

    def get_telefono(self):
        return self.__telefono

    def get_puesto(self):
        return self.__puesto

    def get_salario(self):
        return self.__salario

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_direccion(self, direccion):
        self.__direccion = direccion

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def set_puesto(self, puesto):
        self.__puesto = puesto

    def set_salario(self, salario):
        self.__salario = salario

    def agregar_empleado(self):
        try:
            cursor.execute(
                "INSERT INTO empleados VALUES (null,%s, %s, %s, %s, %s)",
                (self.get_nombre(), self.get_direccion(), self.get_telefono(), self.get_puesto(), self.get_salario())
            )
            conexion.commit()
            print("Empleado agregado exitosamente")
            return True
        except Exception as e:
            print(f"Error al agregar empleado: {e}")
            return False

    def buscar_empleado(id):
        try:
            cursor.execute(
                "SELECT * FROM empleados WHERE id=%s",
                (id,)
            )
            conexion.commit
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al buscar empleado: {e}")
            return None

    @staticmethod
    def actualizar_empleado(id, nombre, puesto, salario):
        try:
            cursor.execute(
                "UPDATE empleados SET nombre=%s, puesto=%s, salario=%s WHERE id=%s",
                (nombre, puesto, salario, id)
            )
            conexion.commit()
            print("Empleado actualizado exitosamente")
            return True
        except Exception as e:
            print(f"Error al actualizar empleado: {e}")
            return False

  
    @staticmethod
    def eliminar_empleado(id):
        try:
            cursor.execute(
                "DELETE FROM empleados WHERE id=%s",
                (id,)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar empleado: {e}")
            return False