#Clientes inscritos	ReporteClientesInscritos(filtros)	Lista de clientes activos, posiblemente por servicio o rango de fechas

def reporte_clientes_inscritos(clientes):
    return [c for c in clientes if c.get("estado") == "activo"]

#Servicios y su capacidad	ReporteServiciosCapacidad()	Cupo máximo vs. inscritos actuales por servicio

def reporte_servicios_capacidad(servicios):
    reporte = []
    for s in servicios:
        reporte.append({
            "servicio": s["nombre"],
            "capacidad_max": s["capacidad_max"],
            "inscritos": len(s.get("inscritos", [])),
            "cupos_disponibles": s["capacidad_max"] - len(s.get("inscritos", []))
        })
    return reporte

#Instructores activos	ReporteInstructoresActivos()	Lista de instructores con estado activo y servicios asignados


#Clientes con bajo rendimiento/riesgo alto	ReporteClientesRiesgo(nivel_minimo)	Cruce entre nivel de riesgo y/o asistencia baja


#Progreso por servicio	ReporteProgresoPorServicio(servicio_id)	Evolución de evaluaciones físicas de los clientes de ese servicio