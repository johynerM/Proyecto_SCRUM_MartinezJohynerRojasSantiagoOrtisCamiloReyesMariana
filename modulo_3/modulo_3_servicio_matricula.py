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

# ==========================================
# 2. MÓDULO DE MATRÍCULAS Y ASIGNACIÓN
# ==========================================

def matricular_cliente(id_servicio, id_cliente, meses_duracion):
    """
    Asigna un cliente a un servicio validando la capacidad máxima.
    Registra fecha de inicio, duración y relaciona al instructor encargado.
    """
    for item in lista_servicios:
        if item["id"] == id_servicio:
            # Validación de capacidad
            inscritos_actuales = len(item["clientes_matriculados"])
            if inscritos_actuales >= item["capacidad_max"]:
                print(f"⚠️ No hay espacio en '{item['nombre']}'. Capacidad máxima ({item['capacidad_max']}) alcanzada. 🙇‍♂️")
                return
            
            # Generación de datos de matrícula requeridos
            fecha_inicio = datetime.now()
            fecha_fin = fecha_inicio + timedelta(days=30 * meses_duracion)
            
            # Creando el registro de matrícula completo
            nueva_matricula = {
                "id_cliente": id_cliente,
                "fecha_inicio": fecha_inicio.strftime("%Y-%m-%d"),
                "fecha_fin": fecha_fin.strftime("%Y-%m-%d"),
                "duracion_meses": meses_duracion,
                "instructor_encargado": item["instructor"]
            }
            
            item["clientes_matriculados"].append(nueva_matricula)
            print(f"😁 Cliente '{id_cliente}' matriculado en '{item['nombre']}' con éxito ✅✅")
            print(f"   📅 Inicio: {nueva_matricula['fecha_inicio']} | Fin: {nueva_matricula['fecha_fin']} | Instructor: {nueva_matricula['instructor_encargado']}")
            return
            
    print(f"❌ El servicio '{id_servicio}' no fue encontrado. Por favor revisar nuevamente 😕")

