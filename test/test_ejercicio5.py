import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import ejercicio5 as act5
import pytest

# Pruebas para el Ejercicio 5: Calculadora de Impuestos con Scope Global


def test_actualizar_tasa_iva():
    """Verifica que la función `actualizar_tasa_iva` modifica la variable global."""
    # Valor inicial
    tasa_original = act5.TASA_IVA

    # Actualizar la tasa
    nueva_tasa = 0.25
    act5.actualizar_tasa_iva(nueva_tasa)

    # Verificar que la variable global ha cambiado
    assert act5.TASA_IVA == nueva_tasa

    # Restaurar la tasa original para no afectar otras pruebas
    act5.actualizar_tasa_iva(tasa_original)


NEW_IVA_RATE = 0.10

def test_calcular_iva_despues_de_actualizar():
    """Verifica que el cálculo del IVA usa la nueva tasa después de la actualización."""
    # Reiniciar la tasa a un valor conocido
    act5.actualizar_tasa_iva(0.19)

    # Calcular IVA con la tasa inicial
    precio = 200
    assert act5.calcular_iva(precio) == pytest.approx(38.0)

    # Actualizar la tasa
    nueva_tasa = NEW_IVA_RATE
    act5.actualizar_tasa_iva(nueva_tasa)

    # Verificar que el cálculo del IVA utiliza la nueva tasa
    assert act5.calcular_iva(precio) == pytest.approx(20.0)
    assert act5.TASA_IVA == NEW_IVA_RATE

    # Restaurar la tasa original al final de la prueba
    act5.actualizar_tasa_iva(0.19)
