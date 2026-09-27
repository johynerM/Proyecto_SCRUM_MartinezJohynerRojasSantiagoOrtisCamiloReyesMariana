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

    

