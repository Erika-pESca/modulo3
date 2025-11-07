import os

import pytest

from ejercicio11 import ARCHIVO_TAREAS, agregar_tarea, mostrar_tareas, ver_tareas


@pytest.fixture(autouse=True)
def limpiar_archivo():
    """Crea y limpia el archivo de tareas antes y después de cada test."""
    if os.path.exists(ARCHIVO_TAREAS):
        os.remove(ARCHIVO_TAREAS)
    yield
    if os.path.exists(ARCHIVO_TAREAS):
        os.remove(ARCHIVO_TAREAS)


def test_agregar_tarea_crea_archivo():
    """Debe crear el archivo si no existe y agregar una tarea."""
    agregar_tarea("Comprar pan")
    assert os.path.exists(ARCHIVO_TAREAS)
    with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as f:
        contenido = f.read().strip()
    assert contenido == "Comprar pan"


def test_agregar_varias_tareas_y_ver_tareas():
    """Debe agregar varias tareas y devolverlas correctamente."""
    tareas = ["Lavar ropa", "Estudiar Python", "Hacer ejercicio"]
    for tarea in tareas:
        agregar_tarea(tarea)
    leidas = ver_tareas()
    assert leidas == tareas


def test_ver_tareas_archivo_no_existente():
    """Si el archivo no existe, debe devolver una lista vacía."""
    if os.path.exists(ARCHIVO_TAREAS):
        os.remove(ARCHIVO_TAREAS)
    tareas = ver_tareas()
    assert tareas == []


def test_mostrar_tareas_vacias(capsys):
    """Debe mostrar el mensaje de que no hay tareas registradas."""
    mostrar_tareas([])
    salida = capsys.readouterr().out
    assert "No hay tareas registradas" in salida


def test_mostrar_tareas_con_datos(capsys):
    """Debe mostrar las tareas en formato de tabla."""
    tareas = ["Hacer compras", "Pagar facturas"]
    mostrar_tareas(tareas)
    salida = capsys.readouterr().out
    assert "Hacer compras" in salida
    assert "Pagar facturas" in salida
    assert "Lista de Tareas" in salida
