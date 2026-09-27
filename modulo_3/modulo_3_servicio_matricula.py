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

def listar_matriculados_por_servicio(id_servicio):
    """Función de apoyo para el módulo 4 (Reportes) para ver el detalle de inscritos."""
    for item in lista_servicios:
        if item["id"] == id_servicio:
            print(f"\n--- MATRICULADOS EN: {item['nombre']} ---")
            if not item["clientes_matriculados"]:
                print("No hay clientes inscritos en este servicio aún.")
                return
            
            for matricula in item["clientes_matriculados"]:
                print(f"Cliente ID: {matricula['id_cliente']} | Inicio: {matricula['fecha_inicio']} | Instructor: {matricula['instructor_encargado']}")
            return
    print(f"❌ Servicio '{id_servicio}' no encontrado.")

# ==========================================
# PRUEBAS DEL MÓDULO (Para validar el funcionamiento)
# ==========================================
if __name__ == "__main__":
    # 1. Cargar servicios obligatorios
    inicializar_servicios_base()
    
    # 2. Asignar instructores
    asignar_instructor_servicio("S01", "María López")
    asignar_instructor_servicio("S02", "Carlos Ruiz")
    
    # 3. Listar servicios para ver el estado inicial
    listar_servicios()
    
    # 4. Matricular clientes
    print("\n--- INICIANDO MATRÍCULAS ---")
    matricular_cliente("S01", "C-1001", 3) # Cliente C-1001 a Yoga por 3 meses
    matricular_cliente("S01", "C-1002", 1) # Cliente C-1002 a Yoga por 1 mes
    matricular_cliente("S09", "C-1003", 2) # Servicio que no existe (prueba de error)
    
    # 5. Forzar el límite de capacidad en Entrenamiento Personalizado (capacidad 5)
    print("\n--- PRUEBA DE LÍMITE DE CAPACIDAD ---")
    asignar_instructor_servicio("S03", "Andrés Camilo")
    for i in range(6):
        matricular_cliente("S03", f"C-200{i}", 1)
        
    # 6. Listado detallado para reportes (Conexión con Módulo 4)
    listar_matriculados_por_servicio("S01")