lista_servicios= [ ]
#Aqui creamos un nuevo servicio por si queremos agregar algun servicio luego y de paso tambien creamos el diccionario 
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
#Aqui mostramos la informacion del o los servicios que deseemos
def listar_servicios():
    for item in lista_servicios:
        inscritos = len(item["clientes_inscritos"])
        cupos_disponibles = item["capacidad_max"] - inscritos
        print("Datos del servicio")
        print(f"ID: {item["id"]} | Nombre: {item["nombre"]} | Instructor: {item["instructor"]}")
        print(f"Capacidad maxima: {item["capacidad_max"]} | Cupos Disponibles: {cupos_disponibles} | Inscritos: {inscritos} ")
#Agregamos un cliente al servicio que escogio
def incripcion_cliente(id_servicio, id_cliente):
    for item in lista_servicios:
        if item["id"] == id_servicio:
            if (item["capacidad_max"] - len(item["clientes_inscritos"])) > 0:
                item["clientes_inscritos"].append(id_cliente)
                print(f"😁 Cliente agregado a {id_servicio} con exito ✅✅")
            else:
                print("No hay espacio lo lamento, intentalo en otro momento o consulta otros servicios 🙇‍♂️🙇‍♀️")
            return
    print(f"❌ El servicio {id_servicio} no encontrado, porfavor revisar nuevamente 😕")

