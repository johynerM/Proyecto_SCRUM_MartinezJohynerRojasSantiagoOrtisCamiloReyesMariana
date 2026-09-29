# INTERFAZ Y MENÚS DE USUARIOS
# ... (tus otras funciones: registrar_usuario, iniciar_sesion, etc.) ...

# Contenido base para logica_usuarios.py

usuarios = {}
usuario_creado = None

def guardar_usuario(id_user, clave, rol, nombre, apellido, direccion, celular, fijo, riesgo, disponibilidad, clases):
    global usuario_creado
    usuarios[id_user] = {
        "id": id_user,
        "clave": clave,
        "rol": rol,
        "nombre": nombre,
        "apellido": apellido,
        "direccion": direccion,
        "celular": celular,
        "fijo": fijo,
        "riesgo": riesgo,
        "disponibilidad": disponibilidad,
        "clases": clases,
        "estado": "Activo"
    }
    usuario_creado = usuarios[id_user]

def validar_usuario(id_ingresado, clave_ingresada):
    global usuario_creado
    if id_ingresado in usuarios and usuarios[id_ingresado]["clave"] == clave_ingresada:
        usuario_creado = usuarios[id_ingresado]
        return True
    return False

def cerrar_sesion_logica():
    global usuario_creado
    usuario_creado = None

