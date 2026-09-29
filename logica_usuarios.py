<<<<<<< HEAD
# Interfaz y menu de usuario
import logica_usuarios as logica

# funciones registrar_usuario, iniciar_sesion, etc

# Esta es la funcion qu te permine marcar error
def menu_modulo_usuarios():
    while True:
        print("\n==============================")
        print(" Menu de usuarios ")
=======
# INTERFAZ Y MENÚS DE USUARIOS
import logica_usuarios as logica

# ... (tus otras funciones: registrar_usuario, iniciar_sesion, etc.) ...


# ESTA ES LA FUNCIÓN QUE TE MARCA ERROR, ASEGÚRATE DE QUE ESTÉ ESCRITA ASÍ:
def menu_modulo_usuarios():
    while True:
        print("\n==============================")
        print(" MENÚ DE USUARIOS ")
>>>>>>> 3c6a82afa8b5d62501dcdf58ca063390f60c49bf
        print("==============================")

        if logica.usuario_creado != None:
            print(
                "Usuario activo:",
                logica.usuario_creado["nombre"],
                "(",
                logica.usuario_creado["rol"],
                ")",
            )

        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Ver mi perfil")
        print("4. Cerrar sesión")
        print("5. Salir del módulo")

        opcion = input("Elija una opción (1-5): ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            ver_perfil()
        elif opcion == "4":
            cerrar_sesion()
        elif opcion == "5":
            print("Saliendo del módulo...")
            break
        else:
            print("Opción no válida, intente de nuevo.")