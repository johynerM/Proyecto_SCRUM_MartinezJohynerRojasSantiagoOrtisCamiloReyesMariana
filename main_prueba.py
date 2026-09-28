# ==========================================
# ARCHIVO PRINCIPAL DE EJECUCIÓN DEL SISTEMA
# ==========================================

# 1. Módulos raíz
import modulo_usuarios
import modulo_2_servicios_clientes

# 2. Módulo 3 (Servicios y Matrículas)
from modulo_3 import modulo_3_servicio_matricula as mod_3
# 3. Módulo 4 (Reportes, Asistencia y Evaluaciones)
from Modulo_4.Modulo_4 import Generacion_de_reportes as mod_4_reportes
from Modulo_4.Modulo_4 import Evaluaciones_periodicas_de_condicion_fisica_y_nivel_de_riesgo as mod_4_evaluaciones

def menu_principal():
    # Inicializar servicios base si aplica
    if hasattr(mod_3, 'inicializar_servicios_base'):
        mod_3.inicializar_servicios_base()

    while True:
        print("\n" + "="*45)
        print("     🏋️‍♂️ GIMNASIO FORCETECH - SISTEMA 🏋️‍♂️")
        print("="*45)
        print("1. Módulo de Usuarios y Autenticación")
        print("2. Módulo de Servicios y Clientes (Módulo 2)")
        print("3. Módulo de Matrículas y Asignaciones (Módulo 3)")
        print("4. Módulo de Reportes y Evaluaciones (Módulo 4)")
        print("5. Salir del programa")
        print("="*45)

        opcion = input("Elija una opción (1-5): ").strip()

        if opcion == "1":
            if hasattr(modulo_usuarios, 'menú_principal'):
                modulo_usuarios.menú_principal()
            elif hasattr(modulo_usuarios, 'menu_usuarios'):
                modulo_usuarios.menu_usuarios()
            else:
                print("⚠️ Función del menú de usuarios no encontrada.")

        elif opcion == "2":
            # Llamada al módulo 2 (Gestión interactiva de servicios)
            if hasattr(modulo_2_servicios_clientes, 'listar_servicios'):
                modulo_2_servicios_clientes.listar_servicios()

        elif opcion == "3":
            # Módulo 3: Servicios y Matrículas
            mod_3.listar_servicios()

        elif opcion == "4":
            # Submenú para conectar el Módulo 4
            print("\n--- 📊 REPORTES Y EVALUACIONES ---")
            print("1. Ver capacidad de servicios")
            print("2. Reporte de clientes inscritos")
            print("3. Volver")
            sub_op = input("Seleccione una opción: ")
            
            if sub_op == "1":
                informe = mod_4_reportes.reporte_servicios_capacidad(mod_3.lista_servicios)
                print(informe)
            elif sub_op == "2":
                print("Regresando...")

        elif opcion == "5":
            print("\n¡Gracias por usar el sistema ForceTech! Hasta luego.")
            break
        else:
            print("❌ Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu_principal()