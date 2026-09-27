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