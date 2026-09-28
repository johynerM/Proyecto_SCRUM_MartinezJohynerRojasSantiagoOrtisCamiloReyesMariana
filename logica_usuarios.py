# Interfaz y menu de usuario
import logica_usuarios as logica

# funciones registrar_usuario, iniciar_sesion, etc

# Esta es la funcion qu te permine marcar error
def menu_modulo_usuarios():
    while True:
        print("\n==============================")
        print(" Menu de usuarios ")
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