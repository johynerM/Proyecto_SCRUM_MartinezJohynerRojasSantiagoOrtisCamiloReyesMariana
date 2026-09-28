#RegistrarAsistencia(cliente_id, servicio_id, fecha, estado) — marca presente/ausente/tarde de un cliente en una clase o servicio específico.

def registrar_asistencia(asistencias, cliente_id, servicio_id, fecha, estado):

    registro = {
        "cliente_id": cliente_id,
        "servicio_id": servicio_id,
        "fecha": fecha,
        "estado": estado
    }
    asistencias.append(registro)
    return registro

#ConsultarAsistenciaPorCliente(cliente_id, rango_fechas) — devuelve el historial de asistencia de un cliente.

def consultar_asistencia_por_cliente(asistencias, cliente_id):
    return [a for a in asistencias if a["cliente_id"] == cliente_id]

#ConsultarAsistenciaPorServicio(servicio_id, fecha) — devuelve quién asistió a una clase/servicio en una fecha dada.

def consultar_asistencia_por_servicio(asistencias, servicio_id, fecha):
    return [a for a in asistencias
            if a["servicio_id"] == servicio_id and a["fecha"] == fecha]

#CalcularPorcentajeAsistencia(cliente_id, periodo) — útil como insumo para las evaluaciones de rendimiento.