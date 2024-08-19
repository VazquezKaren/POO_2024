from conexionBD import*
import hashlib
from funciones import*
import hashlib


class Usuario:
    def __init__(self, nombre, userName, correo, password, versionReciente):
        self.nombre = nombre
        self.userName = userName
        self.correo=correo
        self.contrasena = self.hash_password(password)
        self.versionReciente = versionReciente
        
    def registrar_usuario(self):
        pass
    
        
    def actualizar_usuario(self):
        pass
    
   
    def secion_usuarios(self,contrasena):
        pass
        
    def verificarVersion(self, versionReciente):
        pass

    
   
    def hash_password(self,password):
        return hashlib.sha256(password.encode()).hexdigest()
   

class UsuarioAdmin(Usuario):
    def __init__(self, nombre, userName, correo, password, versionReciente,suscripcionC):
        versionReciente_bool = versionReciente == "si"
        super().__init__(nombre, userName, correo, password, versionReciente_bool)
        self.__suscripcionC=suscripcionC
        

    def get_suscripcionC(self):
        return self.__suscripcionC
    
    def set_suscripcionR(self,suscripcionC):
        self.__suscripcionC=suscripcionC


    def registrar_admin(self):
        try:
            versionReciente_int = 1 if self.versionReciente else 0
            cursor.execute(
                "INSERT INTO administradores  VALUES (null, %s, %s, %s, %s, %s, %s)",
                (self.nombre, self.userName, self.correo, self.contrasena, versionReciente_int, self.get_suscripcionC())
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al registrar administrador: {e}")
            return False


    def actualizar_admim(id,nombre,userName,email,password):
        try:
            cursor.execute(
                "UPDATE administradores set nombre=%s, userName=%s, correo=%s, password=%s WHERE id=%s",
                (nombre,userName,email,password,id)

            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False

        
    def secion_admin(self, correo, contrasena):
        contrasena = hashlib.sha256(contrasena.encode()).hexdigest()
        try:
            cursor.execute(
                "SELECT * FROM administradores WHERE correo=%s AND password=%s",
                (correo, contrasena)
            )
            admin = cursor.fetchone()
            if admin:
                print(f"Administrador encontrado: ")
                return admin
            else:
                print("No se encontró un administrador con las credenciales proporcionadas.")
                return None
        except Exception as e:
            print(f"Error al iniciar sesión: {e}")
            return []


    

class UsuarioInvitado(Usuario):
    def __init__(self, nombre, userName, correo, password, versionReciente, id_realm):
        versionReciente_bool = versionReciente == "si"
        super().__init__(nombre, userName, correo, password, versionReciente_bool)
        self.__caducidad_invitacion = datetime.now() + timedelta(days=30)
        self.__id_realm = id_realm

    def get_caducidad(self):
        return self.__caducidad_invitacion
    
    def set_caducidad(self,caducidad_invitacion):
        self.__caducidad_invitacion=caducidad_invitacion

    def get_idrealm(self):
        return self.__id_realm
    
    def set_idrealm(self,id_admin):
        self.__id_realm=id_admin

    def registrar_invitado(self):
        try:
            versionReciente_int = 1 if self.versionReciente else 0
            
            cursor.execute(
                "INSERT INTO invitados VALUES (NULL, %s, %s, %s, %s, %s, %s, %s) ",
                (self.nombre, self.userName, self.correo, self.contrasena, versionReciente_int, self.get_caducidad(), self.get_idrealm())
            )
            conexion.commit()
            return True, self.get_caducidad()
        except Exception as e:
            print(f"Error al intentar registrar el invitado: {e}")
            return False, None

        
    def actualizar_invitados(id,nombre,userName,email,contrasena):
        try:
            contrasena = hashlib.sha256(contrasena.encode()).hexdigest()
            cursor.execute(
                "UPDATE invitados set nombre=%s, userName=%s, correo=%s, contraseña=%s WHERE id=%s",
                (nombre,userName,email,contrasena,id)

            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False
        
    def secion_invitado(self, correo, contrasena):
        contrasena = hashlib.sha256(contrasena.encode()).hexdigest()
        try:
            cursor.execute(
                "SELECT * FROM invitados WHERE correo=%s AND contraseña=%s",
                (correo, contrasena)
            )
            invitado = cursor.fetchone()
            if invitado:
                print(f"Invitado encontrado: {invitado}")
                return invitado
            else:
                print("No se encontró un invitado con las credenciales proporcionadas.")
                return None
        except Exception as e:
            print(f"Error al iniciar sesión: {e}")
            return []
        
    def mostrar_invitados(id):
        try:
            cursor.execute(
                "SELECT * FROM invitados where id=%s",
                (id,)          
            )
            return cursor.fetchall()
        except Exception as e:
            print(e)
            return None
        
    def eliminar_invitado(id_realm, id):
      
        try:
            
            print(f"Parameters: id_realm={id_realm}, id={id}")

            cursor.execute(
                "DELETE FROM invitados WHERE id_realm=%s AND id=%s",
                (id_realm, id)
            )
            
           
            rows_affected = cursor.rowcount
            conexion.commit()
            
            if rows_affected > 0:
                return True
            else:
                return False

        except Exception as e:
            print(f"Error al eliminar el invitado: {e}")
            return False

    def eliminar_I(id):
        try:
            

            cursor.execute(
                "DELETE FROM invitados WHERE id=%s",
                ( id,)
            )
            
           
            rows_affected = cursor.rowcount
            conexion.commit()
            
            if rows_affected > 0:
                return True
            else:
                return False

        except Exception as e:
            print(f"Error al eliminar el invitado: {e}")
            return False
       
    


        
    



        
            

            



        


        
        



    