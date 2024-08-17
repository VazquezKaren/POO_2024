from conexionBD import*
from funciones import*
from usuarios import usuarios
from datetime import datetime, timedelta
from realm import realm
import getpass
from skin import cuerpo_skin
from skin import estilo_skin
from skin import skin


def menu_principal():
    while True:
        print("""
            .::  Menu Principal ::. 
            1.- Registro
            2.- Login
            3.- Salir 
              
            """)
        opcion=input("Elige una opcion")

        if opcion =="1":
            
            print("""
              ----:::: Registrarse como::::----
                  a.Administrador
                  b.Invitado
            """)
            respuesta=input("selecciona una opcion:").lower()

            if respuesta=="a":
             
                print("\n \t ..:: Inicio de Sesión ::.. ")    
                nombre=input("Ingresa tu Nombre:")
                userName=input("crea un UserName:")
                correo=input("ingresa tu correo:")
                password=input("Crea una contraseña")
                versionReciente=input("Cuenta con la version reciente? si/no").lower()
                suscripcionR=input("Correo de la suscripcion al Realm:")
                obj_admin=usuarios.UsuarioAdmin(nombre,userName,correo,password,versionReciente,suscripcionR)
                respuesta=obj_admin.registrar_admin()

                if respuesta:
                    print(f"\n\t {userName} se registro correctamente")
                else:
                    print(f"No se puede hacer el registro vuelve a intentarlo")

            elif respuesta=='b':
               
                print("\n \t ..:: Inicio de Sesión ::.. ") 
                nombre=input("Ingresa tu Nombre:")
                userName=input("crea un UserName:")
                correo=input("ingresa tu correo:")
                password=input("Crea una contraseña")
                versionReciente=input("Cuenta con la version reciente? si/no").lower()
                id_realm = input("Ingresa el ID del Realm:")

                obj_invitado=usuarios.UsuarioInvitado(nombre,userName,correo,password,versionReciente, id_realm)
                respuestai, fecha_vencimiento=obj_invitado.registrar_invitado()
                
                if respuestai:
                    print(f"\n\t {userName} se registró correctamente.")
                    print(f"La fecha de vencimiento es {fecha_vencimiento.strftime('%Y-%m-%d')}")
                else:
                    print("No se puede hacer el registro, vuelve a intentarlo")
                
    
        elif opcion=="2":
                print("""::::::Inicio de secion::::::
                            soy:
                            a-.Administrador
                            b-.Invitado
                      """)
                resp=input("seleciona una opcion para inciar seción:").lower()
                if resp=="a":

                    email=input("\t Ingresa tu E-mail: ")
                    password=getpass.getpass("\t Ingresa tu Contraseña: ")
                    obj_in_admin=usuarios.UsuarioAdmin("","",email,password,"","")
                    registro=obj_in_admin.secion_admin(email,password)

                    
                    if len(registro)>0:
                        menu_admin(registro[0],registro[1])
                    
                    else:
                     print(f"\n\t ** Nombre de usuario y/o contraseña incorrectos, intentalo de nuevo ** ...")
                    esperarTecla() 

                if resp=="b":
                    email=input("\t Ingresa tu E-mail: ")
                    password=getpass.getpass("\t Ingresa tu Contraseña: ")
                    obj_in=usuarios.UsuarioInvitado("","",email,password,"","")
                    registro=obj_in.secion_invitado(email,password)

                    
                    if len(registro)>0:
                        menu_invitados(registro[0])
                    
                    else:
                     print(f"\n\t ** Nombre de usuario y/o contraseña incorrectos, intentalo de nuevo ** ...")
                    esperarTecla()          
        else:
            print("No se encuentra la opción. Vuelve a")

def menu_admin(id,nombre):
    print(""" 
                ..:::MENU ADMINISTRADORES:::..
                
            1-Realms
            2-Invitados
            3-Editar información Admin
            4-Skin

""")
    op=input("Selecciona una opcion:  ")

    if op =='1':
        print("""::::::::Realms::::::::
                  a-.Crear un Realm
                  b-.Ver Informacion del Realm
                  c-Actualizar informacion del Realm
                  d-.Eliminar
                  
                  """)
        
        realm_op=input("selecciona una opcion: ").lower()
        if realm_op=="a":

            print("---Registro del Realm:---")
            nombre=input("Nombre del Realm :")
            tipo=input("Tipo supervivencia o creativo?: ")
            codigo_Invitacion=input("Crea un codigo para invitar a tus amigos al real:")
            id_admin=input("ID del admin: ")
            
            obj_realm=realm.Realm(nombre,tipo,codigo_Invitacion,id_admin)
            respuesta=obj_realm.crear_realm()

            if respuesta:
                print("***Se creó el REALM con exito***")
            else:
                print("Error vuelve a intentarlo")
                esperarTecla()
        if realm_op=='b':
            registro_realms=realm.Realm.mostrar_realms(id)
            if registro_realms:
                print(f"{nombre} aqui estan tus realms:")

                for fila in registro_realms:
                    print(f"Id del Realm: {fila[0]} \n Nombre del real:{fila[1]}\n Tipo: {fila[2]}\n Codigo Invitacion:{fila[3]}\n Id del Admin{fila[4]}")
                    ('\n')
            else:
                print("No se han creado realms aun")
                esperarTecla()
        if realm_op=="c":
            print("---Actualizacion de Datos del Realm---")
            id_realm=input("id del real que se desea eliminar:")
            nombreN=input("Nuevo nombre del Realm:")
            tipoN=input("Supervivencia o Creativo: ")
            codigo_InvitacionN=input("Nuevo codigo de invitacion:")
            respuestaR =realm.Realm.editar_realm(id_realm, nombreN, tipoN, codigo_InvitacionN)


            if respuestaR:
                print("se hizo el cambio con exito!!")
                esperarTecla()
            else:
                print("No se pudo hacer el cambio")
        if realm_op=="d":
            borrarPantalla()
            id=input("Id del real que se desea eliminar: ")
            eliminr_r=realm.Realm.eliminar_realm(id)

            if eliminr_r:
                print("Se elimino el Realm con exito")
            else:
                print("No se pudo eliminar el realm")
        else:
            print("seleccione una opcion valida")
    

    elif op=="2":
        print(""" ::::Invitados::::
                1-Ver Invitado al Realm
                2-Eliminar Invitado del Realm""")
        op_in=input("selecciona una opcion: ")
        if op_in=="1":
            id=input("Id del Realm: ")
            invitados_realm=usuarios.UsuarioInvitado.mostrar_invitados(id)
            if invitados_realm:
                print(f"Invitados del Realm {nombre[1]}")        
                for fila in invitados_realm:
                    version_reciente = "si" if fila[4] == '1' else "no"
                    
                    print(f" Id:{fila[0]}\n Nombre del Invitado:{fila[1]}\n UserName: {fila[2]}\n correo:{fila[3]}\n version Reciente: {version_reciente} \n Fecha de Caducidad: {fila[6]}")
                else:
                    print("aun no hay invitados en este Realm")
        elif op_in=='2':
            id_realm=input("Id del Realm:")
            id=input("Id del invitado que se desea eliminr: ")


            eliminar_inv=usuarios.UsuarioInvitado.eliminar_invitado(id_realm,id)
            if eliminar_inv:
                print("Se elimino correctamente el invitado")
            else:
                print("No se puedo eliminar el invitado")
    elif op=='3':

            print("""----Datos del Administrador----""")
            id=input("id del admin:")
            nombre_adm=input("Nombre del Admin: ")
            userName=input("Nuevo UserName: ")
            email=input("Email: ")
            password=input("Nuevea contraseña: ")

            obj_Nadmi=usuarios.UsuarioAdmin.actualizar_admim(id,nombre_adm,userName,email,password)
            if obj_Nadmi:
                print(f"\n \t \t .:: La informacion se actualizo con Exito ::. ")
            else:
               print(f"\n \t \t  ** No fue posible actualizar la información, por favor verifique ** ... ")  
            esperarTecla()
    elif op=="4":
        print(""" .:::: Menu de Skin ::::.
                1-cuerpo
                2-Estilo
                3-skin del Administrador """)
        
        op_skin=input("Seleccione una opción: ")

        if op_skin=="1":
            print("""----Cuerpo del Skin----
                  1-Agregar un cuerpo
                  2-Ver cuerpos disponibles 
                  3-actualizar un cuerpo
                  4-eliminar cuerpo
                
                    """)
            op_cuerpo=input("seleciona una opción: ")
            if op_cuerpo=='1':
                verC=cuerpo_skin.cuerpo_skin.mostrar_cuerpo()
                if len(verC)>0:
                    print(":::::Cuerpos disponibles:::::")
                    for fila in verC:
                        print(f"ID: {fila[0]} \nGenero: {fila [1]} \nColor de la base: {fila[2]} \nCabello: {fila [3]} \nColor de ojos: {fila[4]}")
                        esperarTecla()
                    else:
                        print("No hay registro de CuerpoSkin")

                genero=input("Genero del cuerpo (Femenino/Masculino): ")
                color_base=input("Color de piel para tu cuerpo: ")
                cabello=input("Color del cabello: ")
                ojos=input("Color de ojos: ")

                objeto_cuerpo=cuerpo_skin.cuerpo_skin(genero,color_base,cabello,ojos)
                resultado=objeto_cuerpo.crear_cuerpo()

                if resultado:
                    print("Se registro cuerpo con exito")
                else:
                    print("No se pudo hacer el registo")

            if op_cuerpo=='2':
                verC=cuerpo_skin.cuerpo_skin.mostrar_cuerpo()
                if len(verC)>0:
                    print(":::::Cuerpos disponibles:::::")
                    for fila in verC:
                        print(f"ID: {fila[0]} \nGenero: {fila [1]} \nColor de la base: {fila[2]} \nCabello: {fila [3]} \nColor de ojos: {fila[4]}")
                        esperarTecla()
                    else:
                        print("No hay registro de CuerpoSkin")
            if op_cuerpo=='3':
                print(" :::::Cuerpos disponibles:::::")
                verC=cuerpo_skin.cuerpo_skin.mostrar_cuerpo()
                if len(verC)>0:
                    print(":::::Cuerpos disponibles:::::")
                    for fila in verC:
                        print(f"ID: {fila[0]} \nGenero: {fila [1]} \nColor de la base: {fila[2]} \nCabello: {fila [3]} \nColor de ojos: {fila[4]}")
                        esperarTecla()
                 

                id=input("Ingresa el ID del cuerpo que se quiere editar: ") 
                genero=input("Genero del cuerpo (Femenino/Masculino): ")
                color_base=input("Color de piel para tu cuerpo: ")
                cabello=input("Color del cabello: ")
                ojos=input("Color de ojos: ")
                resultado=cuerpo_skin.cuerpo_skin.editar_cuerpo(id,genero,color_base,cabello,ojos)
                if resultado:
                    print("La actualización se hizo con exito")
                else:
                    print("No se pudo hacer la actualización")

            elif op_cuerpo=="4":
                print(" :::::Cuerpos disponibles:::::")
                eliminarC=cuerpo_skin.cuerpo_skin.mostrar_cuerpo()
                if len(eliminarC)>0:
                    print(":::::Cuerpos disponibles:::::")
                    for fila in eliminarC:
                        print(f"ID: {fila[0]} \nGenero: {fila [1]} \nColor de la base: {fila[2]} \nCabello: {fila [3]} \nColor de ojos: {fila[4]}")
                        esperarTecla()
                 

                id=input("Ingresa el ID del cuerpo que se quiere eliminar: ") 
                resultado=cuerpo_skin.cuerpo_skin.eliminar_cuerpo(id)
                if resultado:
                    print("Se elimino con exito el cuerpo de skin")
                else:
                    print("No se pudo eliminar")

        elif op_skin=='2':
            print("""----Estilo del Skin----
                  1-Agregar un Estilo
                  2-Ver Estilos disponibles 
                  3-Actualizar un Estilo
                  4-Eliminar Estilo
                
                    """)
            op_estilo=input("seleciona una opción: ")
            if op_estilo=='1':
                verE=estilo_skin.estilo_skin.mostrar_estilos()
                if len(verE)>0:
                    print(":::::Estilos disponibles:::::")
                    for fila in verE:
                        print(f"ID: {fila[0]} \nPlayera: {fila [1]} \nColor del Pantalón: {fila[2]} \nColor de zapatos: {fila [3]} \nAccesorios extras: {fila[4]} \nArmas: {fila[5]}")
                        esperarTecla()
                    else:
                        print("No hay registro de Estilo Skin")
                playera=input("Color de playera: ")
                pantalon=input("Color de pantalón: ")
                zapatos=input("Color de zapatos: ")
                accesorios=input("Accesorio extra: ")
                armas=input("Arma del skin:")

                objeto_estilo=estilo_skin.estilo_skin(playera,pantalon,zapatos,accesorios,armas)
                resultado=objeto_estilo.crear_estilo()

                if resultado:
                    print("Se registro Estilo con exito")
                else:
                    print("No se pudo hacer el registo")

            if op_estilo=='2':
                verE=estilo_skin.estilo_skin.mostrar_estilos()
                if len(verE)>0:
                    print(":::::Estilos disponibles:::::")
                    for fila in verE:
                        print(f"ID: {fila[0]} \nPlayera: {fila [1]} \nColor del Pantalón: {fila[2]} \nColor de zapatos: {fila [3]} \nAccesorios extras: {fila[4]} \nArmas: {fila[5]}")
                        esperarTecla()
                    else:
                        print("No hay registro de Estilo Skin")

            if op_estilo=='3':
                verC=cuerpo_skin.cuerpo_skin.mostrar_cuerpo()
                if len(verC)>0:
                    print(":::::Cuerpos disponibles:::::")
                    for fila in verC:
                        print(f"ID: {fila[0]} \nGenero: {fila [1]} \nColor de la base: {fila[2]} \nCabello: {fila [3]} \nColor de ojos: {fila[4]}")
                        ("\n")
                        esperarTecla()
                else:
                    print("Cuerpos de skin no disponibles ")
                    ("\n")

                verE=estilo_skin.estilo_skin.mostrar_estilos()
                if len(verE)>0:
                    print(":::::Estilos disponibles:::::")
                    for fila in verE:
                        print(f"ID: {fila[0]} \nPlayera: {fila [1]} \nColor del Pantalón: {fila[2]} \nColor de zapatos: {fila [3]} \nAccesorios extras: {fila[4]} \nArmas: {fila[5]}")
                        ("\n")
                        esperarTecla()
                        ("\n")
                else:
                    print("Estilos no disponibles ")
                    

                id=input("Ingresa el ID del Estilo que se quiere editar: ") 
                playera=input("Color de playera: ")
                pantalon=input("Color de pantalón: ")
                zapatos=input("Color de zapatos: ")
                accesorios=input("Accesorio extra: ")
                armas=input("Arma del skin:")

                resultado=estilo_skin.estilo_skin.editar_estilos(id,playera,pantalon,zapatos,accesorios,armas)
                if resultado:
                    print("La actualización se hizo con exito")
                else:
                    print("No se pudo hacer la actualización")

            elif op_estilo=="4":
                verE=estilo_skin.estilo_skin.mostrar_estilos()
                if len(verE)>0:
                    print(":::::Estilos disponibles:::::")
                    for fila in verE:
                        print(f"ID: {fila[0]} \nPlayera: {fila [1]} \nColor del Pantalón: {fila[2]} \nColor de zapatos: {fila [3]} \nAccesorios extras: {fila[4]} \nArmas: {fila[5]}")
                        esperarTecla()
                 
                 

                id=input("Ingresa el ID del estilo que se quiere eliminar: ") 
                resultado=estilo_skin.estilo_skin.eliminar_estilo(id)
                if resultado:
                    print("Se elimino con exito el Estilo de skin")
                else:
                    print("No se pudo eliminar")

        elif op_skin=="3":
            print(""".:::: Skin ::::.
                    1-Agregar Skin
                    2-Mostrar Skin
                    3-Cambiar Skin
                    4-Eliminar Skin""")
            op_s=input("Selecciona una opción: ")
            if op_s=='1':
                verC=cuerpo_skin.cuerpo_skin.mostrar_cuerpo()
                if len(verC)>0:
                    print(":::::Cuerpos disponibles:::::")
                    for fila in verC:
                        print(f"ID: {fila[0]} \nGenero: {fila [1]} \nColor de la base: {fila[2]} \nCabello: {fila [3]} \nColor de ojos: {fila[4]}")
                        ("\n")
                        esperarTecla()
                else:
                    print("Cuerpos de skin no disponibles ")
                    ("\n")

                verE=estilo_skin.estilo_skin.mostrar_estilos()
                if len(verE)>0:
                    print(":::::Estilos disponibles:::::")
                    for fila in verE:
                        print(f"ID: {fila[0]} \nPlayera: {fila [1]} \nColor del Pantalón: {fila[2]} \nColor de zapatos: {fila [3]} \nAccesorios extras: {fila[4]} \nArmas: {fila[5]}")
                        ("\n")
                        esperarTecla()
                        ("\n")
                else:
                    print("Estilos no disponibles ")
                
                nombre=input("Nombre del Usuario: ")
                UserName=input("UserName del usuario: ")
                id_usuario=input("ID del Admin: ")
                id_cuerpo=input("ID del cuerpo selecionado: ")
                id_estio=input("ID del estilo:")
                obj_skin=skin.Skin(nombre,UserName,id_usuario,id_cuerpo,id_estio)
                resultado=obj_skin.seleccionar_skin()

                if resultado:
                    print("Se hizo el registro de skin correctamente")
                else:
                    print("No se puedo agregar skin")
            if op_s=='2':
                
                verS=skin.Skin.mostrar_skin(id)
                if len(verS)>0:
                    print(":::::Skins Registradas:::::")
                    for fila in verS:
                        print(f"Id skin: {fila[0]} \nNombre del usuario: {fila[1]} \nUserName: {fila[2]} \nId del usuario: {fila[3]} \nId del cuerpo: {fila[4]} \nId del estilo: {fila[5]}")
                        esperarTecla()
                    else:
                        print("No hay registros")
            if op_s=="3":
                
                id=input("id del usuario:")
                verC=cuerpo_skin.cuerpo_skin.mostrar_cuerpo()
                if len(verC)>0:
                    print(":::::Cuerpos disponibles:::::")
                    for fila in verC:
                        print(f"ID: {fila[0]} \nGenero: {fila [1]} \nColor de la base: {fila[2]} \nCabello: {fila [3]} \nColor de ojos: {fila[4]}")
                        esperarTecla()

                verE=estilo_skin.estilo_skin.mostrar_estilos()
                if len(verE)>0:
                    print(":::::Estilos disponibles:::::")
                    for fila in verE:
                        print(f"ID: {fila[0]} \nPlayera: {fila [1]} \nColor del Pantalón: {fila[2]} \nColor de zapatos: {fila [3]} \nAccesorios extras: {fila[4]} \nArmas: {fila[5]}")
                        esperarTecla()

                nombre=input("Nombre del Usuario: ")
                UserName=input("UserName del usuario: ")
                id_cuerpo=input("ID del cuerpo selecionado: ")
                id_estio=input("ID del estilo:")
                obj_skin=skin.Skin(nombre,UserName,id_cuerpo,id_estio,id)
                resultado=obj_skin.actualizar_skin()
                if resultado:
                    print("Skin actualizado exitosamente.")
                else:
                    print("Error al actualizar el Skin.")
            if op_s=="4":
                verS=skin.Skin.mostrar_skinss()
                if len(verS)>0:
                    print(":::::Skins Registradas:::::")
                    for fila in verS:
                        print(f"Id skin: {fila[0]} \nNombre del usuario: {fila[1]} \nUserName: {fila[2]} \nId del usuario: {fila[3]} \nId del cuerpo: {fila[4]} \nId del estilo: {fila[5]}")
                        esperarTecla()
                else:
                    print("No hay registros")

                id_a=input("Id de la skin que se quiere eliminr")
                eliminar=skin.Skin.eliminar_skin(id_a)
                if eliminar:
                    print("Skin eliminada exitosamente.")
                else:
                    print("Error al eliminar el Skin.")



def menu_invitados(id):
    print(""".::::Menu Invitado::::.
          
           1-Ver mi informacion
           2-Actualizar información
           3-skin
           4-Eliminar cuenta """)
    op_menuI=input("Selecciona una opcion: ")
    if op_menuI=='1':
        id=input("Mi ID: ")
        borrarPantalla()
        invitado=usuarios.UsuarioInvitado.mostrar_invitados(id)
        if invitado:
                
            for fila in invitado:
                version_reciente = "si" if fila[4] == '1' else "no"
                print("    Mi informacion:  \n")
                print(f" Id:{fila[0]}\n Nombre del Invitado:{fila[1]}\n UserName: {fila[2]}\n correo:{fila[3]}\n version Reciente: {version_reciente} \n Fecha de Caducidad: {fila[6]}")
        else:
            print("Información no encotrada.Intenta de nuevo")
    if op_menuI=="2":

        nombre=input("Nombre:")
        userName=input("UserName: ")
        email=input("Ingresa tu E-mail: ")
        password=getpass.getpass("\t Ingresa tu Contraseña: ")

        obj_in=usuarios.UsuarioInvitado.actualizar_invitados(id,nombre,userName,email,password)
        if obj_in:
            print("Se realizó la actualización con exito")
        else:
            print("No se pudo actualizar, vuelve a intentarlo")
    if op_menuI=="3":
        print(""".:::: Skin ::::.
                   
                    1-Mostrar Skin
                    2-Cambiar Skin
                    3-Eliminar Skin
                    4-elegir Skin
                    5-salir""")
                    
        op_s=input("Selecciona una opción: ")
        

            
        if op_s=='1':
            print("Skin del usuario Invitado ")
            verS=skin.Skin.mostrar_skin(id)
            if len(verS)>0:
                print(":::::Skins Registradas:::::")
                for fila in verS:
                    print(f"Id skin: {fila[0]} \nNombre del usuario: {fila[1]} \nUserName: {fila[2]} \nId del usuario: {fila[3]} \nId del cuerpo: {fila[4]} \nId del estilo: {fila[5]}")
                    esperarTecla()
                else:
                    print("No hay registros")
        if op_s=="2":
            
            id=input("id del usuario:")
            verC=cuerpo_skin.cuerpo_skin.mostrar_cuerpo()
            if len(verC)>0:
                print(":::::Cuerpos disponibles:::::")
                for fila in verC:
                    print(f"ID: {fila[0]} \nGenero: {fila [1]} \nColor de la base: {fila[2]} \nCabello: {fila [3]} \nColor de ojos: {fila[4]}")
                    esperarTecla()

            verE=estilo_skin.estilo_skin.mostrar_estilos()
            if len(verE)>0:
                print(":::::Estilos disponibles:::::")
                for fila in verE:
                    print(f"ID: {fila[0]} \nPlayera: {fila [1]} \nColor del Pantalón: {fila[2]} \nColor de zapatos: {fila [3]} \nAccesorios extras: {fila[4]} \nArmas: {fila[5]}")
                    esperarTecla()

            nombre=input("Nombre del Usuario: ")
            UserName=input("UserName del usuario: ")
            id_cuerpo=input("ID del cuerpo selecionado: ")
            id_estio=input("ID del estilo:")
            obj_skin=skin.Skin(nombre,UserName,id_cuerpo,id_estio,id)
            resultado=obj_skin.actualizar_skin()
            if resultado:
                print("Skin actualizado exitosamente.")
            else:
                print("Error al actualizar el Skin.")
        if op_s=="3":
            verS=skin.Skin.mostrar_skinss()
            if len(verS)>0:
                print(":::::Skins Registradas:::::")
                for fila in verS:
                    print(f"Id skin: {fila[0]} \nNombre del usuario: {fila[1]} \nUserName: {fila[2]} \nId del usuario: {fila[3]} \nId del cuerpo: {fila[4]} \nId del estilo: {fila[5]}")
                    esperarTecla()
            else:
                print("No hay registros")

            id_a=input("Id de la skin que se quiere eliminr")
            eliminar=skin.Skin.eliminar_skin(id_a)
            if eliminar:
                print("Skin eliminada exitosamente.")
            else:
                print("Error al eliminar el Skin.")
        if op_s:
            verC=cuerpo_skin.cuerpo_skin.mostrar_cuerpo()
            if len(verC)>0:
                print(":::::Cuerpos disponibles:::::")
                for fila in verC:
                    print(f"ID: {fila[0]} \nGenero: {fila [1]} \nColor de la base: {fila[2]} \nCabello: {fila [3]} \nColor de ojos: {fila[4]}")
                    ("\n")
                    esperarTecla()
            else:
                print("Cuerpos de skin no disponibles ")
                ("\n")

            verE=estilo_skin.estilo_skin.mostrar_estilos()
            if len(verE)>0:
                print(":::::Estilos disponibles:::::")
                for fila in verE:
                    print(f"ID: {fila[0]} \nPlayera: {fila [1]} \nColor del Pantalón: {fila[2]} \nColor de zapatos: {fila [3]} \nAccesorios extras: {fila[4]} \nArmas: {fila[5]}")
                    ("\n")
                    esperarTecla()
                    ("\n")
            else:
                print("Estilos no disponibles ")
            
            nombre=input("Nombre del Usuario: ")
            UserName=input("UserName del usuario: ")
            id_usuario=input("Soy:(Administrador/ Invitado) ")
            id_cuerpo=input("ID del cuerpo selecionado: ")
            id_estio=input("ID del estilo:")
            id_realm=input("Id Realm: ")
            obj_skin=skin.Skin(nombre,UserName,id_usuario,id_cuerpo,id_estio,id_realm)
            resultado=obj_skin.seleccionar_skin()

            if resultado:
                print("Se hizo el registro de skin correctamente")
            else:
                print("No se puedo agregar skin")
        
    
    elif op_menuI=='4':
        pregunta=input("Desea eliminar su cuenta? si/no").lower()
        if pregunta=='si':
            eliminar=usuarios.UsuarioInvitado.eliminar_I(id)
            if eliminar:
                print(f"Se eliminó el invitado Id:{id} con exito")
            else:
                print("No se logó eliminar su cuenta. Vuelve a Intentarlo....")
        

if __name__=="__main__":
    menu_principal()






