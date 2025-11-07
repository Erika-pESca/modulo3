import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import pytest
from Ejerciciosfinalespython.actividad6_procesamiento_datos import (
    calcular_precios_con_descuento,
)

# Pruebas para el Ejercicio 6: Procesamiento de Datos con map y lambda


@pytest.fixture
def lista_de_productos():
    """Fixture que proporciona una lista de productos para las pruebas."""
    return [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000},
        {"nombre": "Zapatos", "precio": 120000},
        {"nombre": "Corbata", "precio": 30000},
    ]


def test_calcular_precios_con_descuento(lista_de_productos):
    """Verifica que el descuento del 10% se aplica correctamente a cada producto."""
    precios_esperados = [
        50000 * 0.9,  # 45000.0
        80000 * 0.9,  # 72000.0
        120000 * 0.9,  # 108000.0
        30000 * 0.9,  # 27000.0
    ]

    precios_calculados = calcular_precios_con_descuento(lista_de_productos)

    # Usamos pytest.approx para manejar posibles imprecisiones con números de punto flotante
    assert precios_calculados == pytest.approx(precios_esperados)


def test_producto_con_precio_cero():
    """Verifica que un producto con precio cero resulta en un descuento de cero."""
    productos = [{"nombre": "Gratis", "precio": 0}]
    precios_esperados = [0.0]

    precios_calculados = calcular_precios_con_descuento(productos)

    assert precios_calculados == pytest.approx(precios_esperados)


def test_diferentes_precios(lista_de_productos):
    """Prueba con una mezcla de precios, incluyendo enteros y flotantes."""
    productos_mixtos = lista_de_productos + [
        {"nombre": "Calcetines", "precio": 15500.50}
    ]
    precios_esperados = [
        50000 * 0.9,
        80000 * 0.9,
        120000 * 0.9,
        30000 * 0.9,
        15500.50 * 0.9,
    ]

    precios_calculados = calcular_precios_con_descuento(productos_mixtos)

    assert precios_calculados == pytest.approx(precios_esperados)
