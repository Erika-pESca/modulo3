import pytest

from ejercicio10 import explorar_estructura, resultados

NUM_RESULTADOS_LISTA_SIMPLE = 3
EXPECTED_MAX_DEPTH = 3


@pytest.fixture(autouse=True)
def limpiar_resultados():
    """Limpia la lista global antes de cada test."""
    resultados.clear()
    yield
    resultados.clear()


def test_explorar_lista_simple():
    """Debe identificar correctamente los tipos y niveles en una lista simple."""
    explorar_estructura([1, 2, 3])
    assert len(resultados) == NUM_RESULTADOS_LISTA_SIMPLE
    assert resultados == [(1, 2, "int"), (2, 2, "int"), (3, 2, "int")]


def test_explorar_diccionario_anidado():
    """Debe identificar claves de diccionario y valores anidados."""
    data = {"a": 1, "b": {"c": 2}}
    explorar_estructura(data)
    assert ("a", 1, "dict key") in resultados
    assert (1, 2, "int") in resultados
    assert ("b", 1, "dict key") in resultados
    assert ("c", 2, "dict key") in resultados
    assert (2, 3, "int") in resultados


def test_explorar_tupla_y_conjunto():
    """Debe manejar tuplas y conjuntos correctamente."""
    data = (1, {2, 3})
    explorar_estructura(data)
    tipos = [t[2] for t in resultados]
    assert "int" in tipos
    assert "set" not in tipos  # el conjunto se explora internamente


def test_explorar_vacio():
    """No debe agregar nada si la estructura está vacía."""
    explorar_estructura([])
    assert resultados == []


def test_profundiad_correcta_en_anidacion():
    """Verifica que la profundidad aumenta correctamente en estructuras anidadas."""
    data = [[1, [2, [3]]]]
    explorar_estructura(data)
    profundidades = [p for _, p, _ in resultados]
    assert max(profundidades) > EXPECTED_MAX_DEPTH
