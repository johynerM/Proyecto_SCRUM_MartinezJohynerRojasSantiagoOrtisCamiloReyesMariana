#Clientes inscritos	ReporteClientesInscritos(filtros)	Lista de clientes activos, posiblemente por servicio o rango de fechas

def reporte_clientes_inscritos(clientes):
    return [c for c in clientes if c.get("estado") == "activo"]

#Servicios y su capacidad	ReporteServiciosCapacidad()	Cupo máximo vs. inscritos actuales por servicio


#Instructores activos	ReporteInstructoresActivos()	Lista de instructores con estado activo y servicios asignados
 
def reporte_instructores_activos(instructores):
    return [i for i in instructores if i.get("estado") == "activo"]

#Clientes con bajo rendimiento/riesgo alto	ReporteClientesRiesgo(nivel_minimo)	Cruce entre nivel de riesgo y/o asistencia baja

def reporte_clientes_riesgo(clientes, nivel_minimo="alto"):
    niveles = {"bajo": 1, "medio": 2, "alto": 3}
    minimo = niveles.get(nivel_minimo, 3)
    return [c for c in clientes
            if niveles.get(c.get("nivel_riesgo", "bajo"), 1) >= minimo]

#Progreso por servicio	ReporteProgresoPorServicio(servicio_id)	Evolución de evaluaciones físicas de los clientes de ese servicio

def reporte_progreso_por_servicio(evaluaciones, clientes_del_servicio):
    
    progreso = {}
    for cliente_id in clientes_del_servicio:
        progreso[cliente_id] = consultar_historial_evaluaciones(evaluaciones, cliente_id)
    return progreso