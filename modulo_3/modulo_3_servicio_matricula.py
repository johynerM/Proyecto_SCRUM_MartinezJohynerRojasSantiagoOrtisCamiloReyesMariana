from datetime import datetime, timedelta

# Diccionario global para almacenar los servicios
lista_servicios = []

# ==========================================
# 1. GESTIÓN DE SERVICIOS
# ==========================================

def crear_servicio(id_servicio, nombre, capacidad, instructor):
    """Crea un nuevo servicio y lo agrega a la lista general."""
    nuevo_servicio = {
        "id": id_servicio,
        "nombre": nombre,
        "capacidad_max": capacidad,
        "instructor": instructor,
        # La lista de inscritos ahora guardará diccionarios con los detalles de la matrícula
        "clientes_matriculados": [] 
    }
    lista_servicios.append(nuevo_servicio)
    print(f"✅ Servicio '{nombre}' registrado con éxito.")

def inicializar_servicios_base():
    """Carga los servicios obligatorios mencionados en el requerimiento."""
    print("Iniciando carga de servicios base...")
    crear_servicio("S01", "Clases de yoga", 15, "Por asignar")
    crear_servicio("S02", "Clases de pilates", 15, "Por asignar")
    crear_servicio("S03", "Entrenamiento personalizado", 5, "Por asignar")
    crear_servicio("S04", "Acceso a la piscina", 20, "Sin instructor (Libre)")
    crear_servicio("S05", "Uso del gimnasio general", 50, "Sin instructor (Libre)")
    print("-" * 40)

"""Muestra la información de todos los servicios y su disponibilidad."""
def listar_servicios():
    print("\n--- LISTADO DE SERVICIOS Y CAPACIDAD ---")
    if not lista_servicios:
        print("No hay servicios registrados en el sistema.")
        return

    for item in lista_servicios:
        inscritos = len(item["clientes_matriculados"])
        cupos_disponibles = item["capacidad_max"] - inscritos
        print(f"ID: {item['id']} | Nombre: {item['nombre']} | Instructor: {item['instructor']}")
        print(f"Capacidad máxima: {item['capacidad_max']} | Cupos Disponibles: {cupos_disponibles} | Inscritos: {inscritos}")
        print("-" * 40)

def asignar_instructor_servicio(id_servicio, nombre_instructor):
    """Vincula o actualiza el instructor encargado de un servicio."""
    for item in lista_servicios:
        if item["id"] == id_servicio:
            item["instructor"] = nombre_instructor
            print(f"✅ Instructor '{nombre_instructor}' asignado exitosamente al servicio '{item['nombre']}'.")
            return
    print(f"❌ Error: El servicio con ID '{id_servicio}' no existe.")

