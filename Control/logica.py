# Módulo controlador que coordina el flujo de la aplicación

from Modelo import datos
from VIsta import interfaz

def ejecutar_agregar():
    descripcion = interfaz.solicitar_descripcion()
    tarea = datos.agregar(descripcion)
    interfaz.mostrar_mensaje(f"Tarea '{tarea['descripcion']}' agregada correctamente.")

def ejecutar_ver():
    tareas = datos.obtener_todas()
    interfaz.ver_tareas(tareas)

def ejecutar_completar():
    tareas = datos.obtener_todas()
    if not tareas:
        interfaz.ver_tareas(tareas)
        return

    interfaz.ver_tareas(tareas)
    total = datos.total_tareas()
    
    indice = interfaz.solicitar_numero_tarea(total, "completar")
    try:
        tarea = datos.completar(indice)
        interfaz.mostrar_mensaje(f"Tarea '{tarea['descripcion']}' marcada como completada.")
    except IndexError as e:
        interfaz.mostrar_error(str(e))

def ejecutar_eliminar():
    tareas = datos.obtener_todas()
    if not tareas:
        interfaz.ver_tareas(tareas)
        return

    interfaz.ver_tareas(tareas)
    total = datos.total_tareas()
    
    indice = interfaz.solicitar_numero_tarea(total, "eliminar")
    try:
        tarea = datos.eliminar(indice)
        interfaz.mostrar_mensaje(f"Tarea '{tarea['descripcion']}' eliminada.")
    except IndexError as e:
        interfaz.mostrar_error(str(e))

def iniciar_aplicacion():
    while True:
        interfaz.mostrar_menu()
        opcion = interfaz.solicitar_opcion()

        if opcion == "1":
            ejecutar_agregar()
        elif opcion == "2":
            ejecutar_ver()
        elif opcion == "3":
            ejecutar_completar()
        elif opcion == "4":
            ejecutar_eliminar()
        elif opcion == "5":
            interfaz.mostrar_mensaje("¡Hasta luego!")
            break
        else:
            interfaz.mostrar_error("Opción no válida, intenta de nuevo.")
