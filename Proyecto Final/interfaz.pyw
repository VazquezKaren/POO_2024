import os
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from conexionBD import conexion, cursor
from usuarios import usuarios
from realm import realm

from conexionBD import *
import tkinter as tk
from tkinter import ttk

class Login:
    
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("1200x900")

        icon_path = os.path.join(os.path.dirname(__file__), 'img.png')
        self.ventana.iconbitmap(icon_path)
        self.ventana.title("LOGIN")

        fondo = "#76C7C0"
        self.frame_superior = Frame(self.ventana, width=1000, height=300, bg=fondo)
        self.frame_superior.pack(fill="both", expand=True)

        self.frame_inferior = Frame(self.ventana, bg=fondo)
        self.frame_inferior.pack(fill="both", expand=True)

        for i in range(5):
            self.frame_inferior.columnconfigure(i, weight=1)

        self.load_images()

        self.titulo = Label(self.frame_superior, text="M E N U", font=("Clisto MT", 36, "bold"), bg=fondo)
        self.titulo.pack(side="top", pady=10)

        self.create_buttons()

    def load_images(self):
        mine_path = os.path.join(os.path.dirname(__file__), 'mine.png')
        self.mine = Image.open(mine_path).resize((400, 190))
        self.render_mine = ImageTk.PhotoImage(self.mine)

        img_path = os.path.join(os.path.dirname(__file__), 'img.png')
        self.img = Image.open(img_path).resize((150, 165))
        self.render = ImageTk.PhotoImage(self.img)

        self.label_mine = Label(self.frame_superior, image=self.render_mine, bg="#76C7C0")
        self.label_mine.pack(side="top", pady=0, anchor="n")

        self.fondo = Label(self.frame_superior, image=self.render, bg="#76C7C0")
        self.fondo.pack(side="top", pady=0, anchor="n")

    def create_buttons(self):
        Button(self.frame_inferior, text="Registro", font=("Clisto MT", 40, "bold"), bg="#A9A9A9", fg="#000000", command=self.abrir_ventana_registro).grid(row=0, column=1, padx=20, pady=10, sticky="ew")
        Button(self.frame_inferior, text="Login", font=("Clisto MT", 40, "bold"), bg="#A9A9A9", fg="#000000", command=self.mostrar_formulario_login).grid(row=0, column=2, padx=20, pady=10, sticky="ew")
        Button(self.frame_inferior, text="Salir", font=("Clisto MT", 40, "bold"), bg="#A9A9A9", fg="#000000", command=self.ventana.quit).grid(row=0, column=3, padx=20, pady=10, sticky="ew")

    def inicio(self):
        self.limpiar_frame_inferior()
        for widget in self.frame_superior.winfo_children():
            widget.destroy()

        fondo = "#76C7C0"
        self.load_images()

        self.titulo = Label(self.frame_superior, text="M E N U", font=("Clisto MT", 36, "bold"), bg=fondo)
        self.titulo.pack(side="top", pady=10)

        self.create_buttons()

    def mostrar_formulario_login(self):
        
        self.limpiar_frame_inferior()

        Label(self.frame_inferior, text="Correo", font=("Clisto MT", 30, "bold")).grid(row=0, column=0, padx=20, pady=10)
        self.correo_entry = Entry(self.frame_inferior)
        self.correo_entry.grid(row=0, column=1, padx=20, pady=10)

        Label(self.frame_inferior, text="Contraseña", font=("Clisto MT", 30, "bold")).grid(row=1, column=0, padx=20, pady=10)
        self.password_entry = Entry(self.frame_inferior, show="*")
        self.password_entry.grid(row=1, column=1, padx=20, pady=10)

        Button(self.frame_inferior, text="Login", command=self.login).grid(row=2, column=1, padx=20, pady=10)

    def login(self):
        if hasattr(self, 'correo_entry') and hasattr(self, 'password_entry'):
            correo = self.correo_entry.get()
            contraseña = self.password_entry.get()

            tipo_usuario = messagebox.askquestion("Login", "¿Eres Administrador? (Sí para Admin, No para Invitado)")

            if tipo_usuario == 'yes':
                admin = usuarios.UsuarioAdmin("", "", correo, contraseña, "", "")
                registro = admin.secion_admin(correo, contraseña)
                if registro:
                    self.mostrar_opciones_admin()
                else:
                    self.mostrar_ventana_error("Correo o contraseña de administrador incorrectas")
            elif tipo_usuario == 'no':
                inv = usuarios.UsuarioInvitado("", "", correo, contraseña, "", "")
                registro = inv.secion_invitado(correo, contraseña)
                if registro:
                    self.mostrar_opciones_invitado()
                else:
                    self.mostrar_ventana_error("Datos de invitado incorrectas")
            else:
                self.mostrar_ventana_error("Opción de usuario inválida")
        else:
            self.mostrar_formulario_login()

    def mostrar_opciones_admin(self):
        self.limpiar_frame_inferior()
        Button(self.frame_inferior, text="Crear un Realm", font=("Clisto MT", 30, "bold"), command=self.crear_realm).grid(row=0, column=1, padx=20, pady=10)
        Button(self.frame_inferior, text="Ver Realms", font=("Clisto MT", 30, "bold"), command=self.ver_info_realm).grid(row=0, column=2, padx=20, pady=10)
        Button(self.frame_inferior, text="Actualizar Realm", font=("Clisto MT", 30, "bold"), command=self.actualizar_info_realm).grid(row=0, column=3, padx=20, pady=10)
        
        Button(self.frame_inferior, text="Eliminar", font=("Clisto MT", 30, "bold"), command=self.eliminar_realm).grid(row=1, column=1, padx=20, pady=10)
        Button(self.frame_inferior, text="Salir", font=("Clisto MT", 30, "bold"), command=self.regresar_a_inicio).grid(row=1, column=2, padx=20, pady=10)
        Button(self.frame_inferior, text="Invitados", font=("Clisto MT", 30, "bold"), command=self.ver_info_invitado).grid(row=1, column=3, padx=20, pady=10)
        Button(self.frame_inferior, text="Crear cuerpo", font=("Clisto MT", 30, "bold"), command=self.ver_info_invitado).grid(row=2, column=1, padx=20, pady=10)
        Button(self.frame_inferior, text="Eliminar cuerpo", font=("Clisto MT", 30, "bold"), command=self.ver_info_invitado).grid(row=2, column=3, padx=20, pady=10)

    def mostrar_opciones_invitado(self):
        self.move_images(side="right")
        self.limpiar_frame_inferior()
        Button(self.frame_inferior, text="Mostrar Skin", font=("Clisto MT", 30, "bold"), command=self.mostrar_skin).grid(row=0, column=0, padx=20, pady=10)
        Button(self.frame_inferior, text="Crear Skin", font=("Clisto MT", 30, "bold"), command=self.cambiar_skin).grid(row=0, column=1, padx=20, pady=10)
        Button(self.frame_inferior, text="Eliminar Skin", font=("Clisto MT", 30, "bold"), command=self.eliminar_skin).grid(row=0, column=2, padx=20, pady=10)
        Button(self.frame_inferior, text="Elegir Skin", font=("Clisto MT", 30, "bold"), command=self.elegir_skin).grid(row=1, column=0, padx=20, pady=10)
        Button(self.frame_inferior, text="Salir", font=("Clisto MT", 30, "bold"), command=self.inicio).grid(row=1, column=1, padx=20, pady=10)

    def move_images(self, side):
        self.label_mine.pack_forget()
        self.fondo.pack_forget()
        self.label_mine.pack(side=side, padx=10, pady=10)
        self.fondo.pack(side=side, padx=10, pady=10)

    def crear_realm(self):
        self.move_images(side="left")
        self.limpiar_frame_inferior()

        Label(self.frame_inferior, text="Nombre del Realm", font=("Clisto MT", 16, "bold")).grid(row=0, column=1, padx=20, pady=10)
        self.nombre_realm_entry = Entry(self.frame_inferior)
        self.nombre_realm_entry.grid(row=0, column=2, padx=20, pady=10)

        Label(self.frame_inferior, text="Tipo", font=("Clisto MT", 16, "bold")).grid(row=1, column=1, padx=20, pady=10)
        self.tipo_realm_entry = Entry(self.frame_inferior)
        self.tipo_realm_entry.grid(row=1, column=2, padx=20, pady=10)

        Label(self.frame_inferior, text="Crea un código para invitados", font=("Clisto MT", 16, "bold")).grid(row=2, column=1, padx=20, pady=10)
        self.codigo_invitado_entry = Entry(self.frame_inferior)
        self.codigo_invitado_entry.grid(row=2, column=2, padx=20, pady=10)

        
        Label(self.frame_inferior, text="ID del admin", font=("Clisto MT", 16, "bold")).grid(row=3, column=1, padx=20, pady=10)
        self.id_admin_entry = Entry(self.frame_inferior)
        self.id_admin_entry.grid(row=3, column=2, padx=20, pady=10)

        Button(self.frame_inferior, text="Guardar", command=self.guardar_realm).grid(row=4, column=2, padx=20, pady=10)
        Button(self.frame_inferior, text="Salir", command=self.regresar_al_menu_admin).grid(row=4, column=1, padx=20, pady=10)

    def guardar_realm(self):
        nombre_realm = self.nombre_realm_entry.get()
        tipo = self.tipo_realm_entry.get()
        cod = self.codigo_invitado_entry.get()
        id_admin = self.id_admin_entry.get()

        if not nombre_realm or not tipo or not cod or not id_admin:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
            return

        try:
            realm_obj = realm.Realm(nombre_realm, tipo, cod, id_admin)
            registro = realm_obj.crear_realm()
            
            if registro:
                messagebox.showinfo("Éxito", "Realm creado exitosamente.")
                self.limpiar_frame_inferior() 
            else:
                messagebox.showerror("Error", "No se pudo crear el realm. Inténtelo de nuevo.")
        
        except Exception as e:
            messagebox.showerror("Error", f"Se produjo un error al guardar el realm: {e}")

        self.regresar_al_menu_admin() 

    def mostrar_tabla_realm(self):
        self.limpiar_frame_inferior()

       
        tabla_frame = Frame(self.frame_inferior)
        tabla_frame.grid(row=0, column=0, padx=20, pady=20, columnspan=5, sticky='nsew')

        self.tree = ttk.Treeview(tabla_frame, columns=("ID", "Nombre", "Tipo", "Código", "ID Admin"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Tipo", text="Tipo")
        self.tree.heading("Código", text="Código")
        self.tree.heading("ID Admin", text="ID Admin")
        
        
        vsb = ttk.Scrollbar(tabla_frame, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(tabla_frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        
        self.tree.grid(row=0, column=0, sticky='nsew')
        vsb.grid(row=0, column=1, sticky='ns')
        hsb.grid(row=1, column=0, sticky='ew')

        tabla_frame.grid_rowconfigure(0, weight=1)
        tabla_frame.grid_columnconfigure(0, weight=1)

        cursor.execute("SELECT * FROM realm")
        rows = cursor.fetchall()

        for row in rows:
            self.tree.insert("", "end", values=row)

        
        self.tree.update()



    def ver_info_realm(self):
        cursor.execute("SELECT * FROM realm")
        realms = cursor.fetchall()

        print(realms)  

      
        ventana = tk.Toplevel()
        ventana.title("Información de Realms")

  
        ventana.geometry("800x600") 

       
        tree = ttk.Treeview(ventana, columns=("ID", "Nombre", "Tipo"), show='headings')

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 25, "bold"))  
        style.configure("Treeview", font=("Arial", 20))  
        style.configure("Treeview", rowheight=40)  

        tree.column("ID", anchor=tk.CENTER, width=80)
        tree.column("Nombre", anchor=tk.W, width=200)
        tree.column("Tipo", anchor=tk.W, width=150)

        
        tree.heading("ID", text="ID", anchor=tk.CENTER)
        tree.heading("Nombre", text="Nombre", anchor=tk.W)
        tree.heading("Tipo", text="Tipo", anchor=tk.W)

      
        for realm in realms:
            tree.insert("", "end", values=(realm[0], realm[1], realm[2]))

        tree.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        scrollbar = ttk.Scrollbar(ventana, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        tree.pack_propagate(False)  
    def actualizar_info_realm(self):
        self.limpiar_frame_inferior()
        self.ver_info_realm()

        tk.Label(self.frame_inferior, text="ID del Realm", font=("Clisto MT", 16, "bold")).grid(row=0, column=1, padx=20, pady=10)
        self.id_realm_entry = tk.Entry(self.frame_inferior)
        self.id_realm_entry.grid(row=0, column=2, padx=20, pady=10)

        tk.Label(self.frame_inferior, text="Nuevo Nombre", font=("Clisto MT", 16, "bold")).grid(row=1, column=1, padx=20, pady=10)
        self.nuevo_nombre_realm_entry = tk.Entry(self.frame_inferior)
        self.nuevo_nombre_realm_entry.grid(row=1, column=2, padx=20, pady=10)

        tk.Label(self.frame_inferior, text="Nuevo Tipo", font=("Clisto MT", 16, "bold")).grid(row=2, column=1, padx=20, pady=10)
        self.nuevo_tipo_realm_entry = tk.Entry(self.frame_inferior)
        self.nuevo_tipo_realm_entry.grid(row=2, column=2, padx=20, pady=10)

        tk.Button(self.frame_inferior, text="Actualizar", command=self.guardar_cambios_realm).grid(row=3, column=2, padx=20, pady=10)
        tk.Button(self.frame_inferior, text="Salir", command=self.regresar_al_menu_admin).grid(row=3, column=1, padx=20, pady=10)

    def guardar_cambios_realm(self):
        id_realm = self.id_realm_entry.get()
        nuevo_nombre = self.nuevo_nombre_realm_entry.get()
        nuevo_tipo = self.nuevo_tipo_realm_entry.get()


        try:
            cursor.execute("UPDATE realm SET nombre=%s, tipo=%s WHERE id=%s", (nuevo_nombre, nuevo_tipo, id_realm))
            conexion.commit()
            messagebox.showinfo("Información", "Realm actualizado exitosamente")
            self.registrar_admin()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al actualizar el Realm: {err}")

    def limpiar_frame_inferior(self):
        for widget in self.frame_inferior.winfo_children():
            widget.destroy()
    def eliminar_realm(self):
        self.limpiar_frame_inferior()

        tk.Label(self.frame_inferior, text="ID del Realm a Eliminar", font=("Clisto MT", 16, "bold")).grid(row=0, column=1, padx=20, pady=10)
        self.id_eliminar_realm_entry = tk.Entry(self.frame_inferior)
        self.id_eliminar_realm_entry.grid(row=0, column=2, padx=20, pady=10)

        tk.Button(self.frame_inferior, text="Mostrar Registros", command=self.mostrar_registros).grid(row=1, column=0, padx=20, pady=10)
        tk.Button(self.frame_inferior, text="Eliminar", command=self.confirmar_eliminacion_realm).grid(row=1, column=1, padx=20, pady=10)
        tk.Button(self.frame_inferior, text="Regresar", command=self.regresar_al_menu_admin).grid(row=1, column=2, padx=20, pady=10)

    def mostrar_registros(self):
        self.limpiar_frame_inferior()
    
        registros = self.obtener_registros_realm()
    
        if registros:
            tk.Label(self.frame_inferior, text="Registros Actuales", font=("Clisto MT", 16, "bold")).grid(row=0, column=0, columnspan=4, padx=20, pady=10)
            for index, registro in enumerate(registros):
                tk.Label(self.frame_inferior, text=f"ID: {registro[0]} - Nombre: {registro[1]}").grid(row=index+1, column=0, columnspan=4, padx=20, pady=5)
        else:
            tk.Label(self.frame_inferior, text="No hay registros en la base de datos.", font=("Clisto MT", 16, "bold")).grid(row=0, column=0, columnspan=4, padx=20, pady=10)

        tk.Button(self.frame_inferior, text="Volver", command=self.eliminar_realm).grid(row=len(registros)+1, column=0, columnspan=4, padx=20, pady=10)

    def confirmar_eliminacion_realm(self):
        app=self.mostrar_registros
        id_realm = self.id_eliminar_realm_entry.get()
        
        if id_realm:
            confirm = messagebox.askyesno("Confirmación", f"¿Está seguro de que desea eliminar el Realm con ID {id_realm}?")
            if confirm:
                self.eliminar_realm_db(id_realm)
                messagebox.showinfo("Éxito", "El Realm ha sido eliminado con éxito.")
                self.eliminar_realm()  
            else:
                messagebox.showinfo("Cancelado", "Eliminación cancelada.")
        else:
            messagebox.showwarning("Advertencia", "Por favor ingrese el ID del Realm.")

    

    def eliminar_realm_db(self, id_realm):
        try:
            connection = realm.get_connection()  
            cursor = connection.cursor()
            
            cursor.execute("DELETE FROM realm WHERE id = %s", (id_realm,))
            connection.commit()
        
        except Exception as e:
            print(f"Error: {e}")
            
        finally:
            if 'cursor' in locals():  
                cursor.close()
            if 'connection' in locals():  
                connection.close()

    def mostrar_tabla_invitado(self):
        self.limpiar_frame_inferior()

        tabla_frame = Frame(self.frame_inferior)
        tabla_frame.grid(row=0, column=0, padx=20, pady=20, columnspan=5, sticky='nsew')

        self.tree = ttk.Treeview(tabla_frame, columns=("ID", "Nombre", "UserName", "Correo", "Contraseña", "Versión Reciente", "Caducidad", "ID Realm"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("UserName", text="UserName")
        self.tree.heading("Correo", text="Correo")
        self.tree.heading("Contraseña", text="Contraseña")
        self.tree.heading("Versión Reciente", text="Versión Reciente")
        self.tree.heading("Caducidad", text="Caducidad")
        self.tree.heading("ID Realm", text="ID Realm")
        
        vsb = ttk.Scrollbar(tabla_frame, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(tabla_frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        
        self.tree.grid(row=0, column=0, sticky='nsew')
        vsb.grid(row=0, column=1, sticky='ns')
        hsb.grid(row=1, column=0, sticky='ew')

        tabla_frame.grid_rowconfigure(0, weight=1)
        tabla_frame.grid_columnconfigure(0, weight=1)

        cursor.execute("SELECT * FROM invitados")
        rows = cursor.fetchall()

        for row in rows:
            self.tree.insert("", "end", values=row)

        self.tree.update()
        
    def ver_info_invitado(self):
        
        cursor.execute("SELECT * FROM invitados")
        invitados = cursor.fetchall()

        
        print(invitados)  

        ventana = tk.Toplevel()
        ventana.title("Información de Invitados")

        tree = ttk.Treeview(ventana, columns=("ID", "Nombre", "UserName", "Correo", "Contraseña", "Versión Reciente", "Caducidad", "ID Realm"), show='headings')
        
        tree.column("#0", width=0, stretch=tk.NO) 
        tree.column("ID", anchor=tk.CENTER, width=80)
        tree.column("Nombre", anchor=tk.W, width=150)
        tree.column("UserName", anchor=tk.W, width=100)
        tree.column("Correo", anchor=tk.W, width=150)
        tree.column("Contraseña", anchor=tk.W, width=100)
        tree.column("Versión Reciente", anchor=tk.W, width=120)
        tree.column("Caducidad", anchor=tk.W, width=120)
        tree.column("ID Realm", anchor=tk.W, width=80)

        
        tree.heading("#0", text="", anchor=tk.W)
        tree.heading("ID", text="ID", anchor=tk.CENTER)
        tree.heading("Nombre", text="Nombre", anchor=tk.W)
        tree.heading("UserName", text="UserName", anchor=tk.W)
        tree.heading("Correo", text="Correo", anchor=tk.W)
        tree.heading("Contraseña", text="Contraseña", anchor=tk.W)
        tree.heading("Versión Reciente", text="Versión Reciente", anchor=tk.W)
        tree.heading("Caducidad", text="Caducidad", anchor=tk.W)
        tree.heading("ID Realm", text="ID Realm", anchor=tk.W)

       
        for invitado in invitados:
            tree.insert("", "end", values=(invitado[0], invitado[1], invitado[2], invitado[3], invitado[4], invitado[5], invitado[6], invitado[7]))

       
        tree.pack(padx=10, pady=10)

       
        scrollbar = ttk.Scrollbar(ventana, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

    def regresar_al_menu_admin(self):
        
        
        self.mostrar_opciones_admin()  
    def regresar_a_inicio(self):
        self.load_images()
        self.create_buttons()
        Login()

    def limpiar_frame_inferior(self):
        for widget in self.frame_inferior.winfo_children():
            widget.destroy()

    def mostrar_ventana_error(self, mensaje):
        messagebox.showerror("Error", mensaje)

    
    def limpiar_frame_inferior(self):
        for widget in self.frame_inferior.winfo_children():
            widget.destroy()

    def elegir_skin(self):
        self.move_images(side="left")  
        self.limpiar_frame_inferior()  

        tk.Label(self.frame_inferior, text="Nombre del Usuario", font=("Clisto MT", 16, "bold")).grid(row=0, column=1, padx=20, pady=10)
        self.nombre_usuario_entry = tk.Entry(self.frame_inferior)
        self.nombre_usuario_entry.grid(row=0, column=2, padx=20, pady=10)

        tk.Label(self.frame_inferior, text="Username", font=("Clisto MT", 16, "bold")).grid(row=1, column=1, padx=20, pady=10)
        self.username_entry = tk.Entry(self.frame_inferior)
        self.username_entry.grid(row=1, column=2, padx=20, pady=10)

        tk.Label(self.frame_inferior, text="Tipo de Usuario", font=("Clisto MT", 16, "bold")).grid(row=2, column=1, padx=20, pady=10)
        self.tipo_usuario_entry = tk.Entry(self.frame_inferior)
        self.tipo_usuario_entry.grid(row=2, column=2, padx=20, pady=10)

        tk.Label(self.frame_inferior, text="Cuerpo", font=("Clisto MT", 16, "bold")).grid(row=3, column=1, padx=20, pady=10)
        self.cuerpo_entry = tk.Entry(self.frame_inferior)
        self.cuerpo_entry.grid(row=3, column=2, padx=20, pady=10)

        tk.Label(self.frame_inferior, text="Estilo", font=("Clisto MT", 16, "bold")).grid(row=4, column=1, padx=20, pady=10)
        self.estilo_entry = tk.Entry(self.frame_inferior)
        self.estilo_entry.grid(row=4, column=2, padx=20, pady=10)

        tk.Label(self.frame_inferior, text="Realm", font=("Clisto MT", 16, "bold")).grid(row=5, column=1, padx=20, pady=10)
        self.realm_entry = tk.Entry(self.frame_inferior)
        self.realm_entry.grid(row=5, column=2, padx=20, pady=10)

        tk.Button(self.frame_inferior, text="Guardar", command=self.guardar_skin).grid(row=6, column=2, padx=20, pady=10)

        tk.Button(self.frame_inferior, text="Salir", command=self.regresar_al_menu_admin).grid(row=6, column=1, padx=20, pady=10)

    def guardar_skin(self):
        nombre_usuario = self.nombre_usuario_entry.get()
        username = self.username_entry.get()
        tipo_usuario = self.tipo_usuario_entry.get()
        cuerpo = self.cuerpo_entry.get()
        estilo = self.estilo_entry.get()
        realm = self.realm_entry.get()

        try:
            cursor.execute("""
                INSERT INTO skin (nombre_usuario, userName, tipo_usuario, id_cuerpo, id_estilo, id_realm)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (nombre_usuario, username, tipo_usuario, cuerpo, estilo, realm))
            conexion.commit()
            messagebox.showinfo("Información", "Skin creado exitosamente")
            self.mostrar_tabla_skin()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al crear el skin: {err}")

    def regresar_al_menu_admin(self):
        self.limpiar_frame_inferior()
        self.mostrar_tabla_skin()

    def mostrar_tabla_skin(self):
        self.limpiar_frame_inferior()

        tabla_frame = Frame(self.frame_inferior)
        tabla_frame.grid(row=0, column=0, padx=20, pady=20, columnspan=5, sticky='nsew')

        # Adjusted columns to match your table attributes
        self.tree_skin = ttk.Treeview(tabla_frame, columns=("ID", "Nombre Usuario", "userName", "Tipo Usuario", "Cuerpo", "Estilo", "Realm"), show='headings')
        
        self.tree_skin.heading("ID", text="ID")
        self.tree_skin.heading("Nombre Usuario", text="Nombre Usuario")
        self.tree_skin.heading("userName", text="Username")
        self.tree_skin.heading("Tipo Usuario", text="Tipo Usuario")
        self.tree_skin.heading("Cuerpo", text="Cuerpo")
        self.tree_skin.heading("Estilo", text="Estilo")
        self.tree_skin.heading("Realm", text="Realm")
        
        vsb = ttk.Scrollbar(tabla_frame, orient="vertical", command=self.tree_skin.yview)
        hsb = ttk.Scrollbar(tabla_frame, orient="horizontal", command=self.tree_skin.xview)
        self.tree_skin.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        self.tree_skin.grid(row=0, column=0, sticky='nsew')
        vsb.grid(row=0, column=1, sticky='ns')
        hsb.grid(row=1, column=0, sticky='ew')

        tabla_frame.grid_rowconfigure(0, weight=1)
        tabla_frame.grid_columnconfigure(0, weight=1)

        cursor.execute("SELECT id, nombre_usuario, userName, tipo_usuario, id_cuerpo, id_estilo, id_realm FROM skin")  
        rows = cursor.fetchall()

        for row in rows:
            self.tree_skin.insert("", "end", values=row)

        self.tree_skin.update()


    def mostrar_skin(self):
        cursor.execute("SELECT id, nombre_usuario, userName, tipo_usuario, id_cuerpo, id_estilo, id_realm FROM skin")  
        skins = cursor.fetchall()

        ventana = tk.Toplevel()
        ventana.title("Información de Skin")
        ventana.geometry("800x600")

        tree = ttk.Treeview(ventana, columns=("ID", "Nombre Usuario", "Username", "Tipo Usuario", "Cuerpo", "Estilo", "Realm"), show='headings')

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 25, "bold"))
        style.configure("Treeview", font=("Arial", 20))
        style.configure("Treeview", rowheight=40)

        tree.column("ID", anchor=tk.CENTER, width=80)
        tree.column("Nombre Usuario", anchor=tk.W, width=200)
        tree.column("Username", anchor=tk.W, width=150)
        tree.column("Tipo Usuario", anchor=tk.W, width=150)
        tree.column("Cuerpo", anchor=tk.CENTER, width=100)
        tree.column("Estilo", anchor=tk.CENTER, width=100)
        tree.column("Realm", anchor=tk.CENTER, width=100)

        tree.heading("ID", text="ID", anchor=tk.CENTER)
        tree.heading("Nombre Usuario", text="Nombre Usuario", anchor=tk.W)
        tree.heading("Username", text="Username", anchor=tk.W)
        tree.heading("Tipo Usuario", text="Tipo Usuario", anchor=tk.W)
        tree.heading("Cuerpo", text="Cuerpo", anchor=tk.CENTER)
        tree.heading("Estilo", text="Estilo", anchor=tk.CENTER)
        tree.heading("Realm", text="Realm", anchor=tk.CENTER)

        for skin in skins:
            tree.insert("", "end", values=(skin[0], skin[1], skin[2], skin[3], skin[4], skin[5], skin[6]))

        tree.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        scrollbar = ttk.Scrollbar(ventana, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        tree.pack_propagate(False)


    def cambiar_skin(self):
        self.limpiar_frame_inferior()

        selected_item = self.tree_skin.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un skin para modificar.")
            return

        item = self.tree_skin.item(selected_item)
        skin_data = item['values']

        tk.Label(self.frame_inferior, text="ID", font=("Clisto MT", 16, "bold")).grid(row=0, column=1, padx=20, pady=10)
        self.id_entry = tk.Entry(self.frame_inferior)
        self.id_entry.grid(row=0, column=2, padx=20, pady=10)
        self.id_entry.insert(0, skin_data[0])
        self.id_entry.config(state="readonly")

        tk.Label(self.frame_inferior, text="Nombre Usuario", font=("Clisto MT", 16, "bold")).grid(row=1, column=1, padx=20, pady=10)
        self.nombre_usuario_entry = tk.Entry(self.frame_inferior)
        self.nombre_usuario_entry.grid(row=1, column=2, padx=20, pady=10)
        self.nombre_usuario_entry.insert(0, skin_data[1])

        tk.Label(self.frame_inferior, text="Username", font=("Clisto MT", 16, "bold")).grid(row=2, column=1, padx=20, pady=10)
        self.username_entry = tk.Entry(self.frame_inferior)
        self.username_entry.grid(row=2, column=2, padx=20, pady=10)
        self.username_entry.insert(0, skin_data[2])

        tk.Label(self.frame_inferior, text="Tipo Usuario", font=("Clisto MT", 16, "bold")).grid(row=3, column=1, padx=20, pady=10)
        self.tipo_usuario_entry = tk.Entry(self.frame_inferior)
        self.tipo_usuario_entry.grid(row=3, column=2, padx=20, pady=10)
        self.tipo_usuario_entry.insert(0, skin_data[3])

        tk.Label(self.frame_inferior, text="Cuerpo", font=("Clisto MT", 16, "bold")).grid(row=4, column=1, padx=20, pady=10)
        self.cuerpo_entry = tk.Entry(self.frame_inferior)
        self.cuerpo_entry.grid(row=4, column=2, padx=20, pady=10)
        self.cuerpo_entry.insert(0, skin_data[4])

        tk.Label(self.frame_inferior, text="Estilo", font=("Clisto MT", 16, "bold")).grid(row=5, column=1, padx=20, pady=10)
        self.estilo_entry = tk.Entry(self.frame_inferior)
        self.estilo_entry.grid(row=5, column=2, padx=20, pady=10)
        self.estilo_entry.insert(0, skin_data[5])

        tk.Label(self.frame_inferior, text="Realm", font=("Clisto MT", 16, "bold")).grid(row=6, column=1, padx=20, pady=10)
        self.realm_entry = tk.Entry(self.frame_inferior)
        self.realm_entry.grid(row=6, column=2, padx=20, pady=10)
        self.realm_entry.insert(0, skin_data[6])

        tk.Button(self.frame_inferior, text="Actualizar", command=self.guardar_cambios_skin).grid(row=7, column=2, padx=20, pady=10)

        tk.Button(self.frame_inferior, text="Salir", command=self.regresar_al_menu_admin).grid(row=7, column=1, padx=20, pady=10)

    def guardar_cambios_skin(self):
        id_skin = self.id_entry.get()
        nuevo_nombre_usuario = self.nombre_usuario_entry.get()
        nuevo_username = self.username_entry.get()
        nuevo_tipo_usuario = self.tipo_usuario_entry.get()
        nuevo_cuerpo = self.cuerpo_entry.get()
        nuevo_estilo = self.estilo_entry.get()
        nuevo_realm = self.realm_entry.get()

        try:
            cursor.execute("""
                UPDATE skin 
                SET nombre_usuario=%s, userName=%s, tipo_usuario=%s, id_cuerpo=%s, id_estilo=%s, id_realm=%s 
                WHERE id=%s
            """, (nuevo_nombre_usuario, nuevo_username, nuevo_tipo_usuario, nuevo_cuerpo, nuevo_estilo, nuevo_realm, id_skin))
            conexion.commit()
            messagebox.showinfo("Información", "Skin actualizado exitosamente")
            self.mostrar_tabla_skin()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al actualizar el skin: {err}")

    def regresar_al_menu_admin(self):
        self.limpiar_frame_inferior()
        self.mostrar_tabla_skin()

    
        
    def abrir_ventana_registro(self):
        ventana_registro = VentanaRegistro(self)

    def mostrar_formulario(self, tipo_usuario):
       
        self.label_mine.pack_forget()
        self.label_mine.pack(side="left", padx=10, pady=10)
        self.fondo.pack_forget()
        self.fondo.pack(side="right", padx=10, pady=10)

        
        self.limpiar_frame_inferior()

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
        Button(ventana_exito, text="Continuar", command=lambda: [ventana_exito.destroy(), self.inicio()]).pack(pady=10)

    def mostrar_ventana_error(self, mensaje):
        ventana_error = Toplevel(self.ventana)
        ventana_error.geometry("300x200")
        Label(ventana_error, text=mensaje, font=("Clisto MT", 16, "bold")).pack(pady=20)
        Button(ventana_error, text="Continuar", command=lambda: [ventana_error.destroy(), self.inicio()]).pack(pady=10)

    def regresar_a_inicio(self):
       
        self.label_mine.pack(side="top", pady=0, anchor="n")
        self.fondo.pack(side="top", pady=0, anchor="n")

        self.limpiar_frame_inferior()

     

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