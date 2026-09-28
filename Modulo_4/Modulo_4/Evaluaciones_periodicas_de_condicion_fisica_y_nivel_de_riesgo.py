#RegistrarEvaluacionFisica(cliente_id, fecha, métricas) — guarda datos como peso, % grasa corporal, resistencia, fuerza, etc. (según lo que maneje tu proyecto).

def registrar_evaluacion_fisica(evaluaciones, cliente_id, fecha, metricas):

    registro = {
        "cliente_id": cliente_id,
        "fecha": fecha,
        "metricas": metricas
    }
    evaluaciones.append(registro)
    return registro

#CalcularNivelDeRiesgo(cliente_id) — aplica la lógica/reglas de negocio (por ejemplo, según edad, condición médica, resultados de evaluación, asistencia) para clasificar el riesgo (bajo/medio/alto).

def calcular_nivel_de_riesgo(asistencia_porcentaje, ultima_evaluacion):

    grasa = ultima_evaluacion.get("metricas", {}).get("grasa_corporal", 0)
 
    if asistencia_porcentaje < 40 or grasa > 35:
        return "alto"
    elif asistencia_porcentaje < 70 or grasa > 25:
        return "medio"
    else:
        return "bajo"

#ActualizarNivelDeRiesgo(cliente_id, nuevo_nivel) — persiste el cambio de nivel de riesgo, probablemente con fecha y motivo del cambio.

def actualizar_nivel_de_riesgo(clientes, cliente_id, nuevo_nivel):
    for cliente in clientes:
        if cliente["id"] == cliente_id:
            cliente["nivel_riesgo"] = nuevo_nivel
            return cliente
    return None  # cliente no encontrado

#ConsultarHistorialEvaluaciones(cliente_id) — devuelve la evolución de las evaluaciones físicas en el tiempo (esto alimenta el reporte de "progreso por servicio").

def consultar_historial_evaluaciones(evaluaciones, cliente_id):
    return [e for e in evaluaciones if e["cliente_id"] == cliente_id]