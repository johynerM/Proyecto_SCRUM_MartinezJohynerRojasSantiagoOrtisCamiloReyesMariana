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
    if not lista_servicios:
        print("No hay ningun registro de servicior aún")
        return
    for item in lista_servicios:
        inscritos = len(item["clientes_inscritos"])
        cupos_disponibles = int(item["capacidad_max"]) - inscritos
        print("Datos del servicio")
        print(f"ID: {item["id"]} | Nombre: {item["nombre"]} | Instructor: {item["instructor"]}")
        print(f"Capacidad maxima: {item["capacidad_max"]} | Cupos Disponibles: {cupos_disponibles} | Inscritos: {inscritos} ")
        if inscritos>0:
            print("Estos son los clientes Matriculados:")
            for p in item["clientes_inscritos"]:
                print(f"ID Cliente: {p["id_cliente"]} | Inició el {p["fecha_inicio"]} | Duración: {p["duracion"]}")
        print("="*50)
#Agregamos un cliente al servicio que escogio
def inscripcion_cliente(id_servicio, id_cliente, fecha_inicio="26/09/2026", duracion="1 mes"):
    for item in lista_servicios:
        if item["id"] == id_servicio:
            # Validar si hay cupos
            if (item["capacidad_max"] - len(item["clientes_inscritos"])) > 0:
                # Validar si el cliente ya estaba matriculado en este servicio
                for mat in item["clientes_inscritos"]:
                    if mat["id_cliente"] == id_cliente:
                        print(f"⚠️ El cliente {id_cliente} ya se encuentra matriculado en este servicio.")
                        return
                # Registrar la matrícula completa
                registro = {
                    "id_cliente": id_cliente,
                    "fecha_inicio": fecha_inicio,
                    "duracion": duracion
                }
                item["clientes_inscritos"].append(registro)
                print(f"🤠 Cliente {id_cliente} matriculado en {id_servicio} con éxito ✅")
            else:
                print("🧟‍♂️ No hay espacio lo lamento, inténtalo en otro momento.")
            return
    print(f"❌ El servicio {id_servicio} no encontrado, por favor revisar nuevamente 😕")
#Cancela la subscripcion a un servicio
def cancelar_inscripcion(id_servicio, id_cliente):
    for item in lista_servicios:
        if item["id"] == id_servicio:
            for mat in item["clientes_inscritos"]:
                if mat["id_cliente"] == id_cliente:
                    item["clientes_inscritos"].remove(mat)
                    print(f"👌 Has cancelado la inscripción del cliente {id_cliente} con éxito")
                    return
            print(f"Este id {id_cliente} de cliente no estaba inscrito en la lista")
            return
    print(f"❌ Este servicio {id_servicio} no existe en el sistema ❌")
def modificar_servicio (id_servicio, nuevo_intructor=None, nueva_capacidad=None):
    for item in lista_servicios:
        if item["id"] == id_servicio:
            if nuevo_intructor:
                item["instructor"]=nuevo_intructor
            if nueva_capacidad:
                if nueva_capacidad<len(item["clientes_inscritos"]):
                    print("No se puede redicir la capacidad debajo de la cantidad de inscritos")
                    return
                item["capacidad_max"]=nueva_capacidad
                print(f"El servicio se actualizo correctamente.")
                return
            print(f"El servicio con ID {id_servicio} no esta en esta area.")
#Ahora vamos a hacer el menu para hacer que el cliente pueda escoger lo que desee hacerwhile True:
while True:
    print("="*40)
    print("     🎽Services ForceTech💪      ")
    print("="*40)
    print("1. Crear servicio \n2. Informacion de Servicios \n3. Inscribirse a un servicio \n4. Cancelar Servicio \n5. Modificar Servicio \n6. Volver al menú anterior")
    opcion = int(input("Escoge una opcion (1-5): "))
    if opcion == 1:
        id_serv = input("Ingresa el id del servicio: ").lower()
        nomb = input("Ingrese el nombre del servicio: ").lower()
        instruc = input("Ingresa el nombre del instructor: ").lower()
        try:
            cap_max = int(input("Ingresa el cupo máximo (número): "))
        except ValueError:
            print("❌ El cupo máximo debe ser un número entero (se asignó 10 por defecto).")
            cap_max = 10            
        crear_servicio(id_serv, nomb, cap_max, instruc)
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
    if opcion ==5:
        id_serv = input("Ingresa el id del servicio a modificar: ").lower()
        instruc = input("Nuevo instructor (Enter para omitir): ").lower()
        cap_str = input("Nuevo cupo máximo (Enter para omitir): ")        
        instruc = instruc if instruc.strip() != "" else None
        cap_max = int(cap_str) if cap_str.strip() != "" else None        
        modificar_servicio(id_serv, nuevo_intructor=instruc, nueva_capacidad=cap_max)
    if opcion == 6:
        break