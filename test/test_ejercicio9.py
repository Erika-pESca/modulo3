import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


import pytest
from ejercicio9 import (
    calcular_suma_total,
    concatenar_strings,
)

# Pruebas para el Ejercicio 9: Sumatoria con reduce

# --- Pruebas para la suma de números ---

EXPECTED_SUM_POSITIVE = 15
EXPECTED_SUM_NEGATIVE = 7
EXPECTED_SUM_SINGLE = 100

def test_calcular_suma_total_enteros():
    """Verifica la suma de una lista de números enteros positivos."""
    numeros = [1, 2, 3, 4, 5]
    assert calcular_suma_total(numeros) == EXPECTED_SUM_POSITIVE

def test_calcular_suma_total_con_negativos():
    """Verifica la suma de una lista que incluye números negativos."""
    numeros = [10, -5, 3, -1]
    assert calcular_suma_total(numeros) == EXPECTED_SUM_NEGATIVE

def test_calcular_suma_total_un_elemento():
    """Verifica la suma de una lista con un solo número."""
    assert calcular_suma_total([EXPECTED_SUM_SINGLE]) == EXPECTED_SUM_SINGLE

def test_calcular_suma_total_con_flotantes():
    """Verifica la suma de una lista de números flotantes."""
    numeros = [1.5, 2.5, 3.0]
    assert calcular_suma_total(numeros) == pytest.approx(7.0)

# --- Pruebas para la concatenación de strings ---

def test_concatenar_strings_frase_simple():
    """Verifica la concatenación de una lista de strings para formar una frase."""
    strings = ["Hola", " ", "SENA", "!"]
    assert concatenar_strings(strings) == "Hola SENA!"

def test_concatenar_strings_un_elemento():
    """Verifica la concatenación de una lista con un solo string."""
    assert concatenar_strings(["Python"]) == "Python"

def test_concatenar_strings_con_espacios_y_simbolos():
    """Verifica la concatenación de strings que contienen diversos caracteres."""
    strings = ["reduce ", "es ", "útil.", "\n"]
    assert concatenar_strings(strings) == "reduce es útil.\n"
