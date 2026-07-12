# Módulo que almacena y gestiona los datos de las tareas en memoria

_tareas = []

def obtener_todas() -> list:
    return _tareas

def agregar(descripcion: str) -> dict:
    tarea = {"descripcion": descripcion, "completada": False}
    _tareas.append(tarea)
    return tarea

def completar(indice: int) -> dict:
    if indice < 0 or indice >= len(_tareas):
        raise IndexError("El número de tarea no existe.")
    _tareas[indice]["completada"] = True
    return _tareas[indice]

def eliminar(indice: int) -> dict:
    if indice < 0 or indice >= len(_tareas):
        raise IndexError("El número de tarea no existe.")
    return _tareas.pop(indice)

def total_tareas() -> int:
    return len(_tareas)
