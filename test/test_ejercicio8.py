import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import pytest
from ejercicio8 import transformar_texto

# Pruebas para el Ejercicio 8: Transformación de Datos con List y Dictionary Comprehensions


@pytest.fixture
def texto_de_prueba():
    """Fixture que proporciona un texto de ejemplo para las pruebas."""
    return (
        "La programación funcional es un paradigma de programación declarativa "
        "basado en el uso de funciones matemáticas. El código es predecible."
    )


def test_transformar_texto(texto_de_prueba):
    """Verifica la lista de palabras filtradas y el diccionario de longitudes."""
    palabras_filtradas, conteo_longitudes = transformar_texto(texto_de_prueba)

    # 1. Verificar la lista de palabras (más de 5 letras, en mayúsculas, sin puntuación)
    palabras_esperadas = [
        "PROGRAMACIÓN",
        "FUNCIONAL",
        "PARADIGMA",
        "PROGRAMACIÓN",
        "DECLARATIVA",
        "BASADO",
        "FUNCIONES",
        "MATEMÁTICAS",
        "CÓDIGO",
        "PREDECIBLE",
    ]
    assert sorted(palabras_filtradas) == sorted(palabras_esperadas)

    # 2. Verificar el diccionario de longitudes
    conteo_esperado = {
        "PROGRAMACIÓN": 12,
        "FUNCIONAL": 9,
        "PARADIGMA": 9,
        "DECLARATIVA": 11,
        "BASADO": 6,
        "FUNCIONES": 9,
        "MATEMÁTICAS": 11,
        "CÓDIGO": 6,
        "PREDECIBLE": 10,
    }
    # Nota: "PROGRAMACIÓN" aparece dos veces, pero en el diccionario solo hay una clave.
    assert conteo_longitudes == conteo_esperado


def test_sin_palabras_largas():
    """Verifica el comportamiento cuando no hay palabras que cumplan el criterio."""
    texto = "El sol es luz y calor. Fin."
    palabras_filtradas, conteo_longitudes = transformar_texto(texto)
    assert palabras_filtradas == []
    assert conteo_longitudes == {}


def test_con_puntuacion_y_mayusculas_mixtas():
    """Prueba con un texto que mezcla mayúsculas, minúsculas y puntuación."""
    texto = "Python, un lenguaje versátil. ¡Excelente!"

    palabras_filtradas, conteo_longitudes = transformar_texto(texto)

    palabras_esperadas = ["PYTHON", "LENGUAJE", "VERSÁTIL", "EXCELENTE"]
    conteo_esperado = {"PYTHON": 6, "LENGUAJE": 8, "VERSÁTIL": 8, "EXCELENTE": 9}

    assert sorted(palabras_filtradas) == sorted(palabras_esperadas)
    assert conteo_longitudes == conteo_esperado
