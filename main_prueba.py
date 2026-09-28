# ARCHIVO PRINCIPAL DE EJECUCIÓN
import modulo_usuarios as mod_usuarios
import modulo3_servicios as mod_servicios

def menu_principal():
    while True:
        print("\n========================================")
        print(" GIMNASIO FORCETECH - SISTEMA ")
        print("========================================")
        print("1. Módulo de Usuarios y Autenticación")
        print("2. Módulo de Servicios y Matrículas")
        print("3. Salir del programa")

        opcion = input("Elija una opción (1-3): ")

        if opcion == "1":
            mod_usuarios.menu_modulo_usuarios()  # Llama a la función del módulo
        elif opcion == "2":
            mod_servicios.menu_modulo_3()
        elif opcion == "3":
            print("¡Gracias por usar el sistema!")
            break
        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    menu_principal()