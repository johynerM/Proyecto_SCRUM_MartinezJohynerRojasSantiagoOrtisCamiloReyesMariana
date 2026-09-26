lista_servicios= [ ]
def crear_servicio(id_servicio, nombre, capacidad, instructor):
    nuevo_servicio={
        "id": id_servicio,
        "nombre": nombre,
        "capacidad_max": capacidad,
        "instructor": instructor,
        "clientes_inscritos":[ ]
    }
    lista_servicios.append(nuevo_servicio)
    print(f"servicio {nombre} fue registrado con exito")
def listar_servicios():
    for item in lista_servicios:
        inscritos = len(item["clientes_inscritos"])
        cupos_disponibles = item["capacidad_max"] - inscritos
        print("Datos del servicio")
        print(f"ID: {item["id"]} | Nombre: {item["nombre"]} | Instructor: {item["instructor"]}")
        print(f"Capacidad maxima: {item["capacidad_max"]} | Cupos Disponibles: {cupos_disponibles} | Inscritos: {inscritos} ")
