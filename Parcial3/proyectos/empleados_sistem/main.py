import mysql.connector
from mysql.connector import Error

class ConexionBD:
    def _init_(self, host='localhost', database='mi_empresa', user='root', password=''):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.conexion = None

    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.conexion.is_connected():
                print("Conexión exitosa a la base de datos")
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def cerrar(self):
        if self.conexion.is_connected():
            self.conexion.close()
            print("Conexión cerrada")

class Empleado:
    def _init_(self, conexion):
        self.conexion = conexion

    def crear(self, nombre, puesto, salario):
        cursor = self.conexion.cursor()
        query = "INSERT INTO empleados (nombre, puesto, salario) VALUES (%s, %s, %s)"
        valores = (nombre, puesto, salario)
        cursor.execute(query, valores)
        self.conexion.commit()
        print("Empleado creado exitosamente")

    def leer(self):
        cursor = self.conexion.cursor()
        query = "SELECT * FROM empleados"
        cursor.execute(query)
        resultados = cursor.fetchall()
        for fila in resultados:
            print(f"ID: {fila[0]}, Nombre: {fila[1]}, Puesto: {fila[2]}, Salario: {fila[3]}")

    def actualizar(self, id, nombre, puesto, salario):
        cursor = self.conexion.cursor()
        query = "UPDATE empleados SET nombre = %s, puesto = %s, salario = %s WHERE id = %s"
        valores = (nombre, puesto, salario, id)
        cursor.execute(query, valores)
        self.conexion.commit()
        print("Empleado actualizado exitosamente")

    def eliminar(self, id):
        cursor = self.conexion.cursor()
        query = "DELETE FROM empleados WHERE id = %s"
        valor = (id,)
        cursor.execute(query, valor)
        self.conexion.commit()
        print("Empleado eliminado exitosamente")

class Menu:
    def _init_(self):
        self.conexion_bd = ConexionBD()
        self.empleado = None

    def iniciar(self):
        self.conexion_bd.conectar()
        self.empleado= Empleado(self.conexion_bd.conexion)
        if self.conexion_bd.conexion:
            while True:
                print("\n--- Menú de Opciones ---")
                print("1. Crear empleado")
                print("2. Leer empleados")
                print("3. Actualizar empleado")
                print("4. Eliminar empleado")
                print("5. Salir")
                opcion = input("Elige una opción: ")

                if opcion == '1':
                    nombre = input("Nombre: ")
                    puesto = input("Puesto: ")
                    salario = input("Salario: ")
                    self.empleado.crear(nombre, puesto, salario)
                elif opcion == '2':
                    self.empleado.leer()
                elif opcion == '3':
                    id = input("ID del empleado a actualizar: ")
                    nombre = input("Nuevo nombre: ")
                    puesto = input("Nuevo puesto: ")
                    salario = input("Nuevo salario: ")
                    self.empleado.actualizar(id, nombre, puesto, salario)
                elif opcion == '4':
                    id = input("ID del empleado a eliminar: ")
                    self.empleado.eliminar(id)
                elif opcion == '5':
                    self.conexion_bd.cerrar()
                    break
                else:
                    print("Opción no válida. Inténtalo de nuevo.")

menu = Menu()
menu.iniciar()