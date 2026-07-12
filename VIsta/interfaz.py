# Módulo encargado de la interfaz de usuario en consola

def mostrar_menu():
    print("\n===== SISTEMA DE TAREAS =====")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")

def solicitar_opcion() -> str:
    return input("Elige una opción: ").strip()

def mostrar_error(mensaje: str):
    print(f"\nError: {mensaje}")

def mostrar_mensaje(mensaje: str):
    print(mensaje)

def solicitar_descripcion() -> str:
    while True:
        descripcion = input("Escribe la descripción de la tarea: ").strip()
        if descripcion:
            return descripcion
        mostrar_error("La descripción no puede estar vacía. Inténtalo de nuevo.")

def ver_tareas(tareas: list):
    if not tareas:
        print("\nNo hay tareas registradas.")
        return

    print("\n--- Lista de tareas ---")
    for i, tarea in enumerate(tareas):
        estado = "✔ Completada" if tarea["completada"] else "✘ Pendiente"
        print(f"{i + 1}. {tarea['descripcion']} - {estado}")

def solicitar_numero_tarea(total: int, accion: str) -> int:
    while True:
        try:
            entrada = input(f"\nIngresa el número de la tarea a {accion}: ").strip()
            numero = int(entrada)
            if 1 <= numero <= total:
                return numero - 1
            else:
                mostrar_error(f"Por favor, ingresa un número entre 1 y {total}.")
        except ValueError:
            mostrar_error("Debes ingresar un número entero.")
