# INTERFAZ Y MENÚS DE USUARIOS
import logica_usuarios as logica


# Pedir datos para registrar un usuario
def registrar_usuario():
    print("\n--- REGISTRO DE USUARIO ---")
    id_user = input("Ingrese el ID: ")
    clave = input("Ingrese la contraseña: ")
    rol = input("Tipo de usuario (Cliente/Instructor/Administrador): ")
    nombre = input("Nombres: ")
    apellido = input("Apellidos: ")
    direccion = input("Dirección: ")
    celular = input("Número de celular: ")
    fijo = input("Teléfono fijo: ")

    # Pedir datos extra segun el rol
    if rol == "Cliente":
        riesgo = input("Nivel de riesgo (alto/medio/bajo): ")
        disponibilidad = "N/A"
        clases = "N/A"
    elif rol == "Instructor":
        riesgo = "N/A"
        disponibilidad = input("Disponibilidad horaria (Ej: Mañanas/Tardes): ")
        clases = "Spinning, Funcional"
    else:
        riesgo = "N/A"
        disponibilidad = "N/A"
        clases = "N/A"

    # Enviamos los datos a la logica para guardarlos
    logica.guardar_usuario(
        id_user,
        clave,
        rol,
        nombre,
        apellido,
        direccion,
        celular,
        fijo,
        riesgo,
        disponibilidad,
        clases,
    )
    print("¡Usuario guardado con éxito!")


# Pedir datos para iniciar sesion
def iniciar_sesion():
    print("\n--- INICIO DE SESIÓN ---")
    id_ingresado = input("Ingrese su ID: ")
    clave_ingresada = input("Ingrese su contraseña: ")

    if logica.validar_usuario(id_ingresado, clave_ingresada) == True:
        u = logica.usuario_creado
        print("Bienvenido", u["nombre"], "(", u["rol"], ")")
    else:
        print("Usuario o contraseña incorrectos.")

# Cerrar la sesion en pantalla
def cerrar_sesion():
    if logica.usuario_creado != None:
        print("Sesión cerrada para", logica.usuario_creado["nombre"])
        logica.cerrar_sesion_logica()
    else:
        print("No hay ninguna sesión activa.")

# Mostrar los datos en pantalla
def ver_perfil():
    u = logica.usuario_creado
    if u == None:
        print("Primero debes iniciar sesión.")
    else:
        print("\n--- PERFIL DE USUARIO ---")
        print("ID:", u["id"])
        print("Nombre completo:", u["nombre"], u["apellido"])
        print("Rol:", u["rol"])
        print("Dirección:", u["direccion"])
        print("Celular:", u["celular"])
        print("Teléfono Fijo:", u["fijo"])

        if u["rol"] == "Cliente":
            print("Estado:", u["estado"])
            print("Riesgo:", u["riesgo"])
        elif u["rol"] == "Instructor":
            print("Disponibilidad:", u["disponibilidad"])
            print("Clases asignadas:", u["clases"])
        elif u["rol"] == "Administrador":
            print("Permisos: Control total del gimnasio")

# Menu del modulo de usuarios
def menu_modulo_usuarios():
    while True:
        print("\n==============================")
        print(" MENÚ DE USUARIOS ")
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