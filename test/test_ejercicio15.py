import json

import pytest

from ejercicio15 import (
    buscar_libro,
    cargar_biblioteca,
    devolver_libro,
    guardar_biblioteca,
    prestar_libro,
    ver_libros_prestados,
)


@pytest.fixture
def biblioteca_tmp(tmp_path):
    """Crea un archivo temporal con datos de ejemplo."""
    datos = [
        {"libro_id": "1", "titulo": "Python Básico", "prestado_a": None},
        {"libro_id": "2", "titulo": "Aprendiendo Flask", "prestado_a": "Ana"},
        {"libro_id": "3", "titulo": "Machine Learning", "prestado_a": None}
    ]
    archivo = tmp_path / "biblioteca.json"
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)
    return archivo, datos


def test_cargar_biblioteca(biblioteca_tmp):
    archivo, datos = biblioteca_tmp
    cargado = cargar_biblioteca(str(archivo))
    assert len(cargado) == len(datos)
    assert cargado[1]["titulo"] == "Aprendiendo Flask"


def test_guardar_biblioteca(tmp_path):
    archivo = tmp_path / "guardar.json"
    datos = [{"libro_id": "99", "titulo": "Test Libro", "prestado_a": None}]
    guardar_biblioteca(str(archivo), datos)

    with open(archivo, "r", encoding="utf-8") as f:
        contenido = json.load(f)
    assert contenido[0]["titulo"] == "Test Libro"


def test_prestar_libro_exitoso(biblioteca_tmp):
    archivo, datos = biblioteca_tmp
    libros = cargar_biblioteca(str(archivo))
    resultado = prestar_libro(libros, "1", "Carlos")
    assert resultado is True
    assert libros[0]["prestado_a"] == "Carlos"


def test_prestar_libro_ya_prestado(biblioteca_tmp):
    archivo, datos = biblioteca_tmp
    libros = cargar_biblioteca(str(archivo))
    resultado = prestar_libro(libros, "2", "Pedro")
    assert resultado is False


def test_prestar_libro_no_encontrado(biblioteca_tmp):
    archivo, datos = biblioteca_tmp
    libros = cargar_biblioteca(str(archivo))
    resultado = prestar_libro(libros, "999", "Luis")
    assert resultado is False


def test_devolver_libro_exitoso(biblioteca_tmp):
    archivo, datos = biblioteca_tmp
    libros = cargar_biblioteca(str(archivo))
    resultado = devolver_libro(libros, "2")
    assert resultado is True
    assert libros[1]["prestado_a"] is None


def test_devolver_libro_no_prestado(biblioteca_tmp):
    archivo, datos = biblioteca_tmp
    libros = cargar_biblioteca(str(archivo))
    resultado = devolver_libro(libros, "1")
    assert resultado is False


def test_buscar_libro(biblioteca_tmp):
    archivo, datos = biblioteca_tmp
    libros = cargar_biblioteca(str(archivo))
    resultados = buscar_libro(libros, "Python")
    assert len(resultados) == 1
    assert resultados[0]["titulo"] == "Python Básico"


def test_ver_libros_prestados(biblioteca_tmp):
    archivo, datos = biblioteca_tmp
    libros = cargar_biblioteca(str(archivo))
    prestados = ver_libros_prestados(libros)
    assert len(prestados) == 1
    assert prestados[0]["prestado_a"] == "Ana"
