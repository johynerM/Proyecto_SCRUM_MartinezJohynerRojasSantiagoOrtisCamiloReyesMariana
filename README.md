# Proyecto Scrum - Gimnasio ForceTech

Sistema de gestión en consola desarrollado en Python para el control de usuarios, servicios, matrículas, evaluaciones físicas y reportes del Gimnasio ForceTech.

---

## 📋 Tabla de Contenidos
- [Descripción General](#descripción-general)
- [Contenido del Proyecto](#contenido-del-proyecto)
- [Funcionalidades por Módulo](#funcionalidades-por-módulo)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Contribuyentes](#contribuyentes)

---

## 📌 Descripción General

El **Sistema Gimnasio ForceTech** es una solución informática que permite administrar los procesos clave del gimnasio: desde el registro y autenticación de usuarios y clientes, pasando por la gestión de servicios deportivos y matriculamiento, hasta la evaluación del estado físico y generación de reportes gerenciales.

---

## 🚀 Funcionalidades por Módulo

### 1. Módulo Principal (`main_prueba.py`)

Es el punto de entrada al sistema. Despliega el menú principal y redirecciona el flujo de ejecución hacia cada módulo especializado del programa mediante la importación y llamada de sus funciones correspondientes.

![Texto Alternativo](imagenes\imagen_menu.jpeg)

### 2. Módulo 1: Gestión de Usuarios y Autenticación (`modulo_usuarios.py` y `logica_usuarios.py`)
Este proyecto consiste en un módulo en Python diseñado para la interfaz y gestión de usuarios dentro de un sistema de gimnasio. Permite registrar diferentes tipos de roles, administrar credenciales de acceso, iniciar/cerrar sesión y consultar perfiles personalizados según las responsabilidades o información de cada tipo de usuario.

El módulo expone una interfaz de consola interactiva organizada mediante menús. Se conecta con el módulo logica_usuarios.py para procesar la captura de datos, validar credenciales y almacenar o consultar la información de la sesión activa del usuario.

* Funcionalidades Principales
    1.	Registro de Usuarios:
o	Solicita información básica como ID, contraseña, nombres, apellidos, dirección, celular y teléfono fijo.
o	Solicita información dinámica dependiendo del rol elegido (Cliente, Instructor o Administrador).
o	Envía los datos procesados hacia logica_usuarios.py.
    2.	Inicio de Sesión:
o	Permite ingresar ID y contraseña.
o	Revisa mediante la lógica si las credenciales son válidas y activa la sesión en el sistema.
    3.	Consulta de Perfil:
o	Muestra la información del usuario actualmente autenticado.
o	Adapta los campos mostrados según el rol de la persona activa (por ejemplo: nivel de riesgo para clientes, disponibilidad para instructores, etc.).
    4.	Cierre de Sesión:
o	Desconecta al usuario activo del sistema y resetea la sesión en la lógica.
    5.	Menú Interactivo:
o	Bucle while con opciones dinámicas que muestra de forma constante quién es el usuario que tiene la sesión activa.

![Texto Alternativo](imagenes\modulo_1.jpeg)

### 3. Módulo 2: Gestión de Servicios y Clientes (`modulo_2_servicios_clientes.py`)

Por medio de un submenú el usuario podrá visualizar diferentes opciones que podra realizar sin ningun problema tales como la información de servicios disponibles, la inscripción o cancelacion de algún servicio en el cual este registrado/a, también se podrá crear o modificar los servicios que existen en el sistema si eres un administrador. 


  1. **Propósito General y Alcance:**
     Este módulo administra la oferta de actividades, disciplinas y servicios que ofrece el gimnasio, así como el control y asignación directa de los clientes hacia cada uno de ellos. Permite mantener un control estructurado de los horarios, entrenadores a cargo y la disponibilidad de cupos en tiempo real.

  2. **Estructura de Datos y Persistencia:**
     - **Estructura Dinámica:** Maneja la información a través de diccionarios y listas indexadas por códigos o nombres de servicio.
     - **Campos Gestionados:** Cada servicio registrado contiene atributos clave como `Nombre del Servicio`, `Entrenador Asignado`, `Horarios de Clase`, `Cupo Máximo`, `Cupos Ocupados` y `Estado` (Activo/Inactivo).

  3. **Funciones Principales y Flujo de Trabajo:**
     - **Función `crear_servicio()`:** Permite al administrador o entrenador añadir nuevas disciplinas al gimnasio. Solicita y valida que los campos requeridos no estén vacíos, asigna un entrenador responsable y define el límite de aforo permitido.
     - **Función `listar_servicios()`:** Procesa la lista de actividades registradas y las muestra en pantalla de forma limpia y organizada. Para evitar errores de tipo `KeyError` ante datos incompletos, utiliza la extracción segura mediante `.get('clave', 'N/A')`. Si no existen registros activos, notifica al usuario con un mensaje de alerta sin romper el flujo del programa.
     - **Función `asignar_cliente_a_servicio()`:** Coordina la inscripción de los usuarios en los diferentes servicios. Realiza validaciones en orden:
       1. Verifica que el cliente esté previamente registrado en el sistema.
       2. Comprueba que el servicio exista y esté en estado **Activo**.
       3. Evalúa la disponibilidad de aforo (`Cupos Ocupados < Cupo Máximo`). Si hay disponibilidad, incrementa el contador y efectúa la vinculación; de lo contrario, notifica que el cupo se encuentra agotado.
     - **Función `menu_servicios()`:** Es la interfaz de interacción del módulo. Muestra las opciones disponibles en consola y captura la opción ingresada por el usuario, redirigiéndolo a la función lógica correspondiente mediante estructuras condicionales (`if-elif-else`).

![Texto Alternativo](imagenes\modulo_2.jpeg)

### 4. Módulo 3: Servicios y Matrículas (`modulo_3_servicio_matricula.py`)
Encargado de la gestión económica y administrativa de las inscripciones.
- **Inicialización de Servicios Base:** Carga la oferta inicial de servicios disponibles.
- **Matriculamiento:** Registro de pagos, asignación de planes y control de vigencias de suscripción.

![Texto Alternativo](imagenes\modulo_3.jpeg)

### 5. Módulo 4: Seguimiento, Evaluación y Reportes (`Modulo_4_Modulo_4/`)
El Módulo 4 se encarga de medir el progreso de los clientes y generar la información de salida del sistema. Permite registrar la asistencia a clases/servicios, llevar evaluaciones periódicas de condición física con actualización automática del nivel de riesgo, y generar los reportes clave para la toma de decisiones (clientes inscritos, capacidad de servicios, instructores activos, clientes en riesgo y progreso por servicio).

1. **Propósito General y Alcance:**
   Este módulo administra el seguimiento del desempeño de cada cliente a lo largo del tiempo y produce los reportes que consumen otros módulos o el equipo administrativo, sin gestionar directamente los datos maestros de clientes, servicios o instructores (esos se reciben desde los módulos correspondientes).

2. **Estructura de Datos y Persistencia:**
   Maneja tres colecciones principales como listas de diccionarios:
   - **Asistencias:** `cliente`, `servicio`, `fecha`, `estado`.
   - **Evaluaciones:** `cliente`, `fecha`, `métricas físicas`.
   - **Referencia a Clientes:** Referencia directa para actualizar su campo `nivel_riesgo`.

3. **Funciones Principales y Flujo de Trabajo:**
   - **Registro de Asistencia:**
     - **Función `registrar_asistencia()`:** Registra la asistencia de un cliente a una clase/servicio en una fecha específica (presente, ausente o tarde).
     - **Función `consultar_asistencia_por_cliente()`:** Devuelve el historial completo de asistencia de un cliente.
     - **Función `consultar_asistencia_por_servicio()`:** Devuelve la lista de clientes que asistieron a un servicio en una fecha dada.
     - **Función `calcular_porcentaje_asistencia()`:** Calcula el porcentaje de asistencia de un cliente, usado como insumo para el nivel de riesgo.
   - **Evaluaciones Físicas y Nivel de Riesgo:**
     - **Función `registrar_evaluacion_fisica()`:** Guarda los resultados de una evaluación física (peso, grasa corporal, etc.) de un cliente en una fecha determinada.
     - **Función `calcular_nivel_de_riesgo()`:** Determina el nivel de riesgo (bajo, medio o alto) combinando el porcentaje de asistencia y la última evaluación física.
     - **Función `actualizar_nivel_de_riesgo()`:** Actualiza el nivel de riesgo guardado en el registro del cliente.
     - **Función `consultar_historial_evaluaciones()`:** Devuelve todas las evaluaciones físicas registradas de un cliente, base del reporte de progreso.
   - **Generación de Reportes:**
     - **Función `reporte_clientes_inscritos()`:** Genera el listado de clientes actualmente activos/inscritos.
     - **Función `reporte_servicios_capacidad()`:** Genera el reporte de capacidad máxima vs. cupos ocupados por servicio.
     - **Función `reporte_instructores_activos()`:** Genera el listado de instructores con estado activo.
     - **Función `reporte_clientes_riesgo()`:** Genera el listado de clientes cuyo nivel de riesgo es igual o superior al indicado.
     - **Función `reporte_progreso_por_servicio()`:** Genera el historial de evaluaciones de todos los clientes inscritos en un servicio, mostrando su progreso.
---

![Texto Alternativo](imagenes\modulo_4.jpeg)

## 📁 Estructura del Proyecto

```text
.
├── main_prueba.py                                      # Menú principal y punto de entrada
├── modulo_usuarios.py                                  # Interfaz del Módulo 1 (Menú de Usuarios)
├── logica_usuarios.py                                  # Lógica y persistencia de usuarios (Módulo 1)
├── modulo_2_servicios_clientes.py                      # Gestión de Servicios y Clientes (Módulo 2)
├── modulo_3_servicio_matricula.py                      # Servicios y Matrículas (Módulo 3)
└── Modulo_4_Modulo_4/                                  # Módulo 4: Reportes y Evaluaciones
    ├── Generacion_de_reportes.py                       # Generación de reportes de capacidad
    └── Evaluaciones_periodicas_de_condicion_fisica_y_nivel_de_riesgo.py # Evaluaciones físicas
``` 

## Contribuyentes 
- Johyner Martinez (Product Owner), 
- Mariana Reyes (SCRUM Master), 
- Sebastian Rojas (Equipo de Desarrollo), 
- Camilo Ortiz (Equipo de Desarrollo).