from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from conexionBD import conexion, cursor
from usuarios import usuarios

class Login:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("1000x700")
        self.ventana.iconbitmap("/Users/karen/archivos/Proyecto final/img.png")
        self.ventana.title("LOGIN")

        fondo = "#76C7C0"
        self.frame_superior = Frame(self.ventana)
        self.frame_superior.configure(width=1000, height=300, bg=fondo)
        self.frame_superior.pack(fill="both", expand=True)

        self.frame_inferior = Frame(self.ventana)
        self.frame_inferior.configure(bg=fondo)
        self.frame_inferior.pack(fill="both", expand=True)

        self.frame_inferior.columnconfigure(0, weight=1)
        self.frame_inferior.columnconfigure(1, weight=1)
        self.frame_inferior.columnconfigure(2, weight=1)
        self.frame_inferior.columnconfigure(3, weight=1)
        self.frame_inferior.columnconfigure(4, weight=1)

        # Parte de imágenes
        self.mine = Image.open("/Users/karen/archivos/Proyecto final/mine.png")
        self.mine = self.mine.resize((400, 190))
        self.render_mine = ImageTk.PhotoImage(self.mine)

        self.label_mine = Label(self.frame_superior, image=self.render_mine, bg=fondo)
        self.label_mine.pack(side="top", pady=0, anchor="n")

        self.img = Image.open("/Users/karen/archivos/Proyecto final/img.png")
        self.img = self.img.resize((150, 165))
        self.render = ImageTk.PhotoImage(self.img)

        self.fondo = Label(self.frame_superior, image=self.render, bg=fondo)
        self.fondo.pack(side="top", pady=0, anchor="n")

        # Texto "Login Usuarios"
        self.titulo = Label(self.frame_superior,
                            text="M E N U",
                            font=("Clisto MT", 36, "bold"),
                            bg=fondo)
        self.titulo.pack(side="top", pady=10)

        # Botones
        self.boton_registro = Button(self.frame_inferior, 
                                     text="Registro", 
                                     font=("Clisto MT", 40, "bold"),
                                     bg="#A9A9A9", 
                                     fg="#000000", 
                                     command=self.abrir_ventana_registro)  
        self.boton_registro.grid(row=0, column=1, padx=20, pady=10, sticky="ew")

        self.boton_login = Button(self.frame_inferior, 
                                  text="Login", 
                                  font=("Clisto MT", 40, "bold"),
                                  bg="#A9A9A9",  
                                  fg="#000000", 
                                  command=self.login)  # Reemplazar comando aquí
        self.boton_login.grid(row=0, column=2, padx=20, pady=10, sticky="ew")
        
        self.boton_salir = Button(self.frame_inferior, 
                                  text="Salir", 
                                  font=("Clisto MT", 40, "bold"),
                                  bg="#A9A9A9",  
                                  fg="#000000", 
                                  command=self.ventana.quit)  
        self.boton_salir.grid(row=0, column=3, padx=20, pady=10, sticky="ew")
    def mostrar_formulario_login(self):
        # Limpiar la parte inferior y mostrar el formulario de login
        self.limpiar_frame_inferior()

        Label(self.frame_inferior, text="Correo", font=("Clisto MT", 16, "bold")).grid(row=0, column=0, padx=20, pady=10)
        self.correo_entry = Entry(self.frame_inferior)
        self.correo_entry.grid(row=0, column=1, padx=20, pady=10)

        Label(self.frame_inferior, text="Contraseña", font=("Clisto MT", 16, "bold")).grid(row=1, column=0, padx=20, pady=10)
        self.password_entry = Entry(self.frame_inferior, show="*")
        self.password_entry.grid(row=1, column=1, padx=20, pady=10)

        Button(self.frame_inferior, text="Login", command=self.login).grid(row=2, column=1, padx=20, pady=10)

    def login(self):
        if hasattr(self, 'correo_entry') and hasattr(self, 'password_entry'):
            correo = self.correo_entry.get()
            contraseña = self.password_entry.get()

            print(f"Correo ingresado: {correo}")
            print(f"Contraseña ingresada: {contraseña}")

            tipo_usuario = messagebox.askquestion("Login", "¿Eres Administrador? (Sí para Admin, No para Invitado)")
            print(f"Tipo de usuario seleccionado: {tipo_usuario}")

            if tipo_usuario == 'yes':
                admin = usuarios.UsuarioAdmin.secion_admin(correo, contraseña)  # Asegúrate de que el método existe y es correcto
                if admin:
                    print(f"Administrador encontrado: {admin}")
                    self.mostrar_opciones_admin()
                else:
                    print("No se encontró un administrador con las credenciales proporcionadas.")
                    self.mostrar_ventana_error("Credenciales de administrador incorrectas")
            elif tipo_usuario == 'no':
                inv = usuarios.UsuarioInvitado.secion_invitado(correo, contraseña)  # Asegúrate de que el método existe y es correcto
                if inv:
                    print("Opción de Invitado seleccionada")
                    self.mostrar_opciones_invitado()
                else:
                    print("No se encontró un invitado con las credenciales proporcionadas.")
                    self.mostrar_ventana_error("Credenciales de invitado incorrectas")
            else:
                print("Opción inválida seleccionada")
                self.mostrar_ventana_error("Opción de usuario inválida")
        else:
            print("Formulario de login no encontrado")
            self.mostrar_formulario_login()  # Mostrar formulario de login si no existe

    def mostrar_opciones_admin(self):
        # Mover imágenes a la derecha
        self.label_mine.pack(side="right", padx=10, pady=10)
        self.fondo.pack(side="right", padx=10, pady=10)

        # Limpiar la parte inferior para mostrar las opciones de Admin
        self.limpiar_frame_inferior()

        Button(self.frame_inferior, text="Crear un Realm", command=self.crear_realm).grid(row=0, column=0, padx=20, pady=10)
        Button(self.frame_inferior, text="Ver Información del Realm", command=self.ver_info_realm).grid(row=0, column=1, padx=20, pady=10)
        Button(self.frame_inferior, text="Actualizar Información del Realm", command=self.actualizar_info_realm).grid(row=0, column=2, padx=20, pady=10)
        Button(self.frame_inferior, text="Eliminar", command=self.eliminar_realm).grid(row=0, column=3, padx=20, pady=10)
        Button(self.frame_inferior, text="Salir", command=self.regresar_a_inicio).grid(row=0, column=4, padx=20, pady=10)

    def mostrar_opciones_invitado(self):
        # Mover imágenes a la derecha
        self.label_mine.pack(side="right", padx=10, pady=10)
        self.fondo.pack(side="right", padx=10, pady=10)

        # Limpiar la parte inferior para mostrar las opciones de Invitado
        self.limpiar_frame_inferior()

        Button(self.frame_inferior, text="Mostrar Skin", command=self.mostrar_skin).grid(row=0, column=0, padx=20, pady=10)
        Button(self.frame_inferior, text="Cambiar Skin", command=self.cambiar_skin).grid(row=0, column=1, padx=20, pady=10)
        Button(self.frame_inferior, text="Eliminar Skin", command=self.eliminar_skin).grid(row=0, column=2, padx=20, pady=10)
        Button(self.frame_inferior, text="Elegir Skin", command=self.elegir_skin).grid(row=0, column=3, padx=20, pady=10)
        Button(self.frame_inferior, text="Salir", command=self.ventana.quit).grid(row=0, column=4, padx=20, pady=10)

    def abrir_ventana_registro(self):
        ventana_registro = VentanaRegistro(self)

    def limpiar_frame_inferior(self):
        for widget in self.frame_inferior.winfo_children():
            widget.destroy()

    def crear_realm(self):
        pass

    def ver_info_realm(self):
        pass

    def actualizar_info_realm(self):
        pass

    def eliminar_realm(self):
        pass

    def mostrar_skin(self):
        pass

    def cambiar_skin(self):
        pass

    def eliminar_skin(self):
        pass

    def elegir_skin(self):
        pass
    
    

    
        
    def abrir_ventana_registro(self):
        ventana_registro = VentanaRegistro(self)

    def mostrar_formulario(self, tipo_usuario):
        # Mover imágenes a la esquina superior
        self.label_mine.pack_forget()
        self.label_mine.pack(side="left", padx=10, pady=10)
        self.fondo.pack_forget()
        self.fondo.pack(side="right", padx=10, pady=10)

        # Limpiar la parte inferior para mostrar el formulario
        self.limpiar_frame_inferior()

        # Crear los campos dependiendo del tipo de usuario
        if tipo_usuario == 'admin':
            self.mostrar_formulario_admin()
        elif tipo_usuario == 'invitado':
            self.mostrar_formulario_invitado()

    def mostrar_formulario_admin(self):
        Label(self.frame_inferior, text="Nombre", font=("Clisto MT", 16, "bold")).grid(row=0, column=0, padx=20, pady=10)
        self.nombre_entry = Entry(self.frame_inferior)
        self.nombre_entry.grid(row=0, column=1, padx=20, pady=10)

        Label(self.frame_inferior, text="UserName", font=("Clisto MT", 16, "bold")).grid(row=1, column=0, padx=20, pady=10)
        self.username_entry = Entry(self.frame_inferior)
        self.username_entry.grid(row=1, column=1, padx=20, pady=10)

        Label(self.frame_inferior, text="Correo", font=("Clisto MT", 16, "bold")).grid(row=2, column=0, padx=20, pady=10)
        self.correo_entry = Entry(self.frame_inferior)
        self.correo_entry.grid(row=2, column=1, padx=20, pady=10)

        Label(self.frame_inferior, text="Contraseña", font=("Clisto MT", 16, "bold")).grid(row=3, column=0, padx=20, pady=10)
        self.password_entry = Entry(self.frame_inferior, show="*")
        self.password_entry.grid(row=3, column=1, padx=20, pady=10)

        Label(self.frame_inferior, text="Versión Reciente (si/no)", font=("Clisto MT", 16, "bold")).grid(row=4, column=0, padx=20, pady=10)
        self.version_entry = Entry(self.frame_inferior)
        self.version_entry.grid(row=4, column=1, padx=20, pady=10)

        Label(self.frame_inferior, text="Suscripción", font=("Clisto MT", 16, "bold")).grid(row=5, column=0, padx=20, pady=10)
        self.suscripcion_entry = Entry(self.frame_inferior)
        self.suscripcion_entry.grid(row=5, column=1, padx=20, pady=10)

        Button(self.frame_inferior, text="Registrar", command=self.registrar_admin).grid(row=6, column=1, padx=20, pady=10)

    def mostrar_formulario_invitado(self):
        Label(self.frame_inferior, text="Nombre", font=("Clisto MT", 16, "bold")).grid(row=0, column=0, padx=20, pady=10)
        self.nombre_entry = Entry(self.frame_inferior)
        self.nombre_entry.grid(row=0, column=1, padx=20, pady=10)

        Label(self.frame_inferior, text="UserName", font=("Clisto MT", 16, "bold")).grid(row=1, column=0, padx=20, pady=10)
        self.username_entry = Entry(self.frame_inferior)
        self.username_entry.grid(row=1, column=1, padx=20, pady=10)

        Label(self.frame_inferior, text="Correo", font=("Clisto MT", 16, "bold")).grid(row=2, column=0, padx=20, pady=10)
        self.correo_entry = Entry(self.frame_inferior)
        self.correo_entry.grid(row=2, column=1, padx=20, pady=10)

        Label(self.frame_inferior, text="Contraseña", font=("Clisto MT", 16, "bold")).grid(row=3, column=0, padx=20, pady=10)
        self.password_entry = Entry(self.frame_inferior, show="*")
        self.password_entry.grid(row=3, column=1, padx=20, pady=10)

        Label(self.frame_inferior, text="Versión Reciente (si/no)", font=("Clisto MT", 16, "bold")).grid(row=4, column=0, padx=20, pady=10)
        self.version_entry = Entry(self.frame_inferior)
        self.version_entry.grid(row=4, column=1, padx=20, pady=10)

        Label(self.frame_inferior, text="ID Realm", font=("Clisto MT", 16, "bold")).grid(row=5, column=0, padx=20, pady=10)
        self.realm_entry = Entry(self.frame_inferior)
        self.realm_entry.grid(row=5, column=1, padx=20, pady=10)

        Button(self.frame_inferior, text="Registrar", command=self.registrar_invitado).grid(row=6, column=1, padx=20, pady=10)

    def registrar_admin(self):
        nombre = self.nombre_entry.get()
        correo = self.correo_entry.get()
        suscripcion = self.suscripcion_entry.get()

        usuario = usuarios.UsuarioAdmin(nombre, correo, correo, 'password', 'si', suscripcion)
        exito = usuario.registrar_admin()

        if exito:
            self.mostrar_ventana_exito("Registro de Administrador exitoso")
        else:
            self.mostrar_ventana_error("No se pudo completar el registro de Administrador")

    def registrar_invitado(self):
        nombre = self.nombre_entry.get()
        correo = self.correo_entry.get()
        realm = self.realm_entry.get()

        usuario = usuarios.UsuarioInvitado(nombre, correo, correo, 'password', 'si', realm)
        exito, _ = usuario.registrar_invitado()

        if exito:
            self.mostrar_ventana_exito("Registro de Invitado exitoso")
        else:
            self.mostrar_ventana_error("No se pudo completar el registro de Invitado")

    def mostrar_ventana_exito(self, mensaje):
        ventana_exito = Toplevel(self.ventana)
        ventana_exito.geometry("300x200")
        Label(ventana_exito, text=mensaje, font=("Clisto MT", 16, "bold")).pack(pady=20)
        Button(ventana_exito, text="Continuar", command=lambda: [ventana_exito.destroy(), self.regresar_a_inicio()]).pack(pady=10)

    def mostrar_ventana_error(self, mensaje):
        ventana_error = Toplevel(self.ventana)
        ventana_error.geometry("300x200")
        Label(ventana_error, text=mensaje, font=("Clisto MT", 16, "bold")).pack(pady=20)
        Button(ventana_error, text="Continuar", command=lambda: [ventana_error.destroy(), self.regresar_a_inicio()]).pack(pady=10)

    def regresar_a_inicio(self):
        # Restaurar la vista inicial de la ventana
        self.label_mine.pack(side="top", pady=0, anchor="n")
        self.fondo.pack(side="top", pady=0, anchor="n")

        # Limpiar la parte inferior y restaurar los botones iniciales
        self.limpiar_frame_inferior()

        # Reinstanciar los botones
        self.boton_registro = Button(self.frame_inferior, 
                                    text="Registro", 
                                    font=("Clisto MT", 40, "bold"),
                                    bg="#A9A9A9", 
                                    fg="#000000", 
                                    command=self.abrir_ventana_registro)
        self.boton_registro.grid(row=0, column=1, padx=20, pady=10, sticky="ew")

        self.boton_login = Button(self.frame_inferior, 
                                text="Login", 
                                font=("Clisto MT", 40, "bold"),
                                bg="#A9A9A9",  
                                fg="#000000")  # Puedes agregar funcionalidad de login si la necesitas
        self.boton_login.grid(row=0, column=2, padx=20, pady=10, sticky="ew")
        
        self.boton_salir = Button(self.frame_inferior, 
                                text="Salir", 
                                font=("Clisto MT", 40, "bold"),
                                bg="#A9A9A9",  
                                fg="#000000", 
                                command=self.ventana.quit)
        self.boton_salir.grid(row=0, column=3, padx=20, pady=10, sticky="ew")

    def limpiar_frame_inferior(self):
        for widget in self.frame_inferior.winfo_children():
            widget.destroy()


class VentanaRegistro:
    def __init__(self, master):
        self.master = master
        self.ventana = Toplevel(master.ventana)
        self.ventana.geometry("400x200")
        self.ventana.title("Registro")

        self.label = Label(self.ventana, text="¿Registrar como Admin o Invitado?", font=("Clisto MT", 16, "bold"))
        self.label.pack(pady=20)

        self.boton_admin = Button(self.ventana, text="Administrador", command=lambda: self.master.mostrar_formulario('admin'))
        self.boton_admin.pack(pady=10)

        self.boton_invitado = Button(self.ventana, text="Invitado", command=lambda: self.master.mostrar_formulario('invitado'))
        self.boton_invitado.pack(pady=10)


if __name__ == "__main__":
    login_app = Login()
    login_app.ventana.mainloop()