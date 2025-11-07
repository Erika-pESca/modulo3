import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import pytest
from ejercicio7 import (
    filtrar_estudiantes_aprobados,
)

# Pruebas para el Ejercicio 7: Filtrado de Estudiantes con filter


@pytest.fixture
def lista_de_estudiantes():
    """Fixture que proporciona una lista de estudiantes para las pruebas."""
    return [
        ("Ana", 4.5),  # Aprueba
        ("Juan", 2.8),  # No aprueba
        ("Maria", 3.9),  # Aprueba
        ("Carlos", 2.9),  # No aprueba
        ("Luisa", 3.0),  # Aprueba (límite exacto)
        ("Pedro", 5.0),  # Aprueba
    ]


def test_filtrar_estudiantes_aprobados(lista_de_estudiantes):
    """Verifica que solo los estudiantes con nota >= 3.0 son retornados."""
    estudiantes_aprobados_esperados = [
        ("Ana", 4.5),
        ("Maria", 3.9),
        ("Luisa", 3.0),
        ("Pedro", 5.0),
    ]

    resultado = filtrar_estudiantes_aprobados(lista_de_estudiantes)

    # Comparamos las listas. El orden debe ser el mismo que el de entrada.
    assert resultado == estudiantes_aprobados_esperados


def test_ningun_estudiante_aprueba():
    """Verifica que se retorna una lista vacía si ningún estudiante aprueba."""
    estudiantes = [("Juan", 2.8), ("Carlos", 2.9), ("Marta", 1.5)]
    assert filtrar_estudiantes_aprobados(estudiantes) == []


def test_todos_los_estudiantes_aprueban():
    """Verifica que se retorna la lista completa si todos los estudiantes aprueban."""
    estudiantes = [("Ana", 4.5), ("David", 3.1), ("Elena", 5.0)]
    assert filtrar_estudiantes_aprobados(estudiantes) == estudiantes


def test_notas_limite():
    """Prueba con notas que están justo en el límite de aprobación."""
    estudiantes = [("Justo Aprobado", 3.0), ("Casi Aprobado", 2.99)]
    estudiantes_aprobados_esperados = [("Justo Aprobado", 3.0)]

    resultado = filtrar_estudiantes_aprobados(estudiantes)

    assert resultado == estudiantes_aprobados_esperados
