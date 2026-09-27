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
def inscripcion_cliente(id_servicio, id_cliente):
    for item in lista_servicios:
        if item["id"] == id_servicio:
            if (item["capacidad_max"] - len(item["clientes_inscritos"])) > 0:
                item["clientes_inscritos"].append(id_cliente)
                print(f"😁 Cliente agregado a {id_servicio} con exito ✅✅")
            else:
                print("No hay espacio lo lamento, intentalo en otro momento o consulta otros servicios 🙇‍♂️🙇‍♀️")
            return
    print(f"❌ El servicio {id_servicio} no encontrado, porfavor revisar nuevamente 😕")
#Cancela la subscripcion de un cliente a un servicio
def cancelar_inscripcion(id_servicio, id_cliente):
    for item in lista_servicios:
        if item["id"] == id_servicio:
            if id_cliente in item["clientes_inscritos"]:
                item["clientes_inscritos"].remove(id_cliente)
                print(f"Has cancelado el servicio con exito 👌") 
            else:
                print(f"Este id {id_cliente} de cliente no estaba inscrito en la lista")
            return
    print(f"❌ Este servicio {id_servicio} no existe en el sistema ❌")
#Ahora vamos a hacer el menu para hacer que el cliente pueda escoger lo que desee hacer
while True:
    print("="*40)
    print("     🎽Services ForceTech💪      ")
    print("="*40)
    print("1.Crear servicio \n2. Informacion de Servicio \n3. Inscribirse a un servicio \n4. Cancelar Servicio \n5. Volver al menú anterior")
    opcion = int(input("Escoge una opcion (1-5): "))
    if opcion == 1:
        id_serv=input("Ingresa el id del servicio: ").lower()
        nomb=input("Ingrese el nombre del servicio: ").lower()
        instruc=input("Ingresa el nombre del instructor: ").lower()
        cap_max=int(input("Ingresa el cupo máximo: "))        
        crear_servicio(id_serv,nomb,instruc,cap_max)
    if opcion == 2:
        listar_servicios()
    if opcion == 3:
        id_serv=input("Ingresa el id del servicio: ").lower()
        id_client=input("Ingresa tu id: ").lower()
        inscripcion_cliente(id_serv,id_client)
    if opcion == 4:
        id_serv=input("Ingresa el id del servicio: ").lower()
        id_client=input("Ingresa tu id: ").lower()
        cancelar_inscripcion(id_serv,id_client)
    if opcion == 5:
        break