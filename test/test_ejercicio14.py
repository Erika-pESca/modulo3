import csv
import json
import os

import pytest

from ejercicio14 import (
    generar_reporte,
    leer_csv,
    leer_json,
)

EXPECTED_ITEM_COUNT = 3


# === FIXTURES ===
@pytest.fixture
def archivos_temporales(tmp_path):
    """Crea archivos CSV y JSON temporales con datos de prueba."""
    ruta_csv = tmp_path / "estudiantes.csv"
    ruta_json = tmp_path / "cursos.json"
    ruta_reporte = tmp_path / "reporte.txt"

    # Crear CSV temporal
    with open(ruta_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "nombre", "edad"])
        writer.writerow(["1", "Ana", "20"])
        writer.writerow(["2", "Luis", "22"])
        writer.writerow(["3", "Camila", "19"])

    # Crear JSON temporal
    cursos = [
        {"nombre": "Matemáticas", "estudiantes": ["1", "2"]},
        {"nombre": "Programación", "estudiantes": ["2", "3"]},
        {"nombre": "Física", "estudiantes": ["1"]},
    ]
    with open(ruta_json, "w", encoding="utf-8") as f:
        json.dump(cursos, f, indent=4)

    return ruta_csv, ruta_json, ruta_reporte


# === TESTS DE LECTURA ===
def test_leer_csv(archivos_temporales):
    """Debe leer correctamente los datos del archivo CSV."""
    ruta_csv, _, _ = archivos_temporales
    estudiantes = leer_csv(ruta_csv)
    assert len(estudiantes) == EXPECTED_ITEM_COUNT
    assert estudiantes[0]["nombre"] == "Ana"


def test_leer_json(archivos_temporales):
    """Debe leer correctamente los datos del archivo JSON."""
    _, ruta_json, _ = archivos_temporales
    cursos = leer_json(ruta_json)
    assert len(cursos) == EXPECTED_ITEM_COUNT
    assert cursos[0]["nombre"] == "Matemáticas"


# === TEST DE GENERACIÓN DE REPORTE ===
def test_generar_reporte(archivos_temporales, capsys):
    """Debe generar un archivo reporte.txt con los datos combinados."""
    ruta_csv, ruta_json, ruta_reporte = archivos_temporales

    estudiantes = leer_csv(ruta_csv)
    cursos = leer_json(ruta_json)
    generar_reporte(estudiantes, cursos, ruta_reporte)

    # Verificar que el archivo se creó
    assert os.path.exists(ruta_reporte)

    # Leer contenido del reporte
    with open(ruta_reporte, "r", encoding="utf-8") as f:
        contenido = f.read()

    assert "Ana" in contenido
    assert "Matemáticas" in contenido
    assert "Luis" in contenido
    assert "Programación" in contenido

    # Verificar salida en consola
    salida = capsys.readouterr().out
    assert "📘 Reporte de Cursos por Estudiante" in salida
    assert "✅ Reporte generado correctamente" in salida
