import json
import os

import pytest

from ejercicio13 import (
    ARCHIVO_INVENTARIO,
    CARPETA_DATOS,
    agregar_producto,
    cargar_inventario,
    guardar_inventario,
    mostrar_inventario,
    vender_producto,
)

EXPECTED_QUANTITY_AFTER_ADD = 10
EXPECTED_QUANTITY_AFTER_SELL = 5


class MockInput:
    def __init__(self, inputs):
        self.inputs = inputs
        self.call_count = 0

    def __call__(self, prompt):
        val = self.inputs[self.call_count]
        self.call_count += 1
        return val

@pytest.fixture(autouse=True)
def limpiar_archivo():
    """Crea y limpia el archivo de inventario antes y después de cada prueba."""
    os.makedirs(CARPETA_DATOS, exist_ok=True)
    if os.path.exists(ARCHIVO_INVENTARIO):
        os.remove(ARCHIVO_INVENTARIO)

    with open(ARCHIVO_INVENTARIO, "w", encoding="utf-8") as f:
        json.dump([], f)

    yield

    if os.path.exists(ARCHIVO_INVENTARIO):
        os.remove(ARCHIVO_INVENTARIO)

def test_agregar_producto(capsys, monkeypatch):
    """Debe agregar un producto al inventario."""
    mock_input = MockInput(["Producto A", "10", "5.0"])
    monkeypatch.setattr("rich.console.Console.input", mock_input)

    inventario = cargar_inventario()
    agregar_producto(inventario)

    inventario_actualizado = cargar_inventario()
    assert len(inventario_actualizado) == 1
    assert inventario_actualizado[0]["nombre"] == "Producto A"
    assert inventario_actualizado[0]["cantidad"] == EXPECTED_QUANTITY_AFTER_ADD

def test_vender_producto(capsys, monkeypatch):
    """Debe disminuir el stock de un producto vendido."""
    inventario_inicial = [{"nombre": "Producto B", "cantidad": 15, "precio": 5.0}]
    guardar_inventario(inventario_inicial)

    mock_input = MockInput(["Producto B", "5"])
    monkeypatch.setattr("rich.console.Console.input", mock_input)

    inventario = cargar_inventario()
    vender_producto(inventario)

    inventario_actualizado = cargar_inventario()
    assert inventario_actualizado[0]["cantidad"] == EXPECTED_QUANTITY_AFTER_ADD

def test_vender_producto_stock_insuficiente(capsys, monkeypatch):
    """No debe vender si el stock es insuficiente."""
    inventario_inicial = [{"nombre": "Producto C", "cantidad": 5, "precio": 2.0}]
    guardar_inventario(inventario_inicial)

    mock_input = MockInput(["Producto C", "10"])
    monkeypatch.setattr("rich.console.Console.input", mock_input)

    inventario = cargar_inventario()
    vender_producto(inventario)

    salida = capsys.readouterr().out
    assert "No hay suficiente stock disponible" in salida

    inventario_actualizado = cargar_inventario()
    assert inventario_actualizado[0]["cantidad"] == EXPECTED_QUANTITY_AFTER_SELL

def test_mostrar_inventario_con_datos(capsys):
    """Debe mostrar una tabla con el inventario."""
    inventario = [
        {"nombre": "Producto D", "cantidad": 20, "precio": 1.5},
        {"nombre": "Producto E", "cantidad": 10, "precio": 2.5},
    ]
    mostrar_inventario(inventario)
    salida = capsys.readouterr().out
    assert "INVENTARIO ACTUAL" in salida
    assert "Producto D" in salida
    assert "20" in salida
    assert "1.50" in salida

def test_mostrar_inventario_vacio(capsys):
    """Debe indicar que el inventario está vacío."""
    mostrar_inventario([])
    salida = capsys.readouterr().out
    assert "El inventario está vacío" in salida
