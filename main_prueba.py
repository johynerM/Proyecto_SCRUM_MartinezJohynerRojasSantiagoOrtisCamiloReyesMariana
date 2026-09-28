# Sistema de egecucion 
import modulo_usuarios as mod_usuarios

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
            print("\n[Aquí se conecta el trabajo de los compañeros]")
        elif opcion == "3":
            print("¡Gracias por usar el sistema!")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu_principal()