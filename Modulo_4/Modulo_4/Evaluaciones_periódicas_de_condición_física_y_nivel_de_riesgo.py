#RegistrarEvaluacionFisica(cliente_id, fecha, métricas) — guarda datos como peso, % grasa corporal, resistencia, fuerza, etc. (según lo que maneje tu proyecto).


#CalcularNivelDeRiesgo(cliente_id) — aplica la lógica/reglas de negocio (por ejemplo, según edad, condición médica, resultados de evaluación, asistencia) para clasificar el riesgo (bajo/medio/alto).


#ActualizarNivelDeRiesgo(cliente_id, nuevo_nivel) — persiste el cambio de nivel de riesgo, probablemente con fecha y motivo del cambio.


#ConsultarHistorialEvaluaciones(cliente_id) — devuelve la evolución de las evaluaciones físicas en el tiempo (esto alimenta el reporte de "progreso por servicio").