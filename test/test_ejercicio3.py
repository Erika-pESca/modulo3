import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import unittest

from Ejerciciosfinalespython.actividad3_contador_de_llamadas import crear_contador


class TestFabricaContadores(unittest.TestCase):

    def test_incremento_basico(self):
        """
        Verifica que un solo contador se incremente correctamente de 1 en 1.
        """
        contador = crear_contador()

        # Primera llamada
        self.assertEqual(contador(), 1, "La primera llamada debe devolver 1.")

        # Segunda llamada
        self.assertEqual(contador(), 2, "La segunda llamada debe devolver 2.")

    def test_persistencia_de_estado(self):
        """
        Verifica que el contador recuerde su estado a través de múltiples llamadas.
        """
        contador = crear_contador()

        # Llamamos 5 veces para verificar que el estado persiste
        for expected in range(1, 6):
            self.assertEqual(contador(), expected, f"En la llamada {expected}, el valor debe ser {expected}.")

    def test_independencia_contador(self):
        """
        Verifica el requisito principal: que los contadores sean completamente
        independientes entre sí (prueba de Closure).
        """
        # Crear dos instancias de la "fábrica"
        contador_a = crear_contador()
        contador_b = crear_contador()

        # 1. Usar A y verificar su estado
        self.assertEqual(contador_a(), 1, "A debe iniciar en 1.")

        # 2. Usar B varias veces
        self.assertEqual(contador_b(), 1, "B debe iniciar en 1, independientemente de A.")
        self.assertEqual(contador_b(), 2, "B debe incrementarse correctamente.")

        # 3. Volver a usar A y verificar que continúa su conteo (persistencia)
        # El valor esperado es 2 + 1 = 3
        self.assertEqual(contador_a(), 2, "A debe continuar desde 2, sin ser afectado por B.")
        self.assertEqual(contador_a(), 3, "A debe continuar incrementándose correctamente.")

    def test_nonlocal_aplicado(self):
        """
        Verifica indirectamente que se está modificando la variable 'conteo'
        del scope externo, esencial para el closure. Si retorna '1' en la
        segunda llamada, 'nonlocal' no funcionó.
        """
        contador = crear_contador()
        contador()  # 1

        # Si la segunda llamada es > 1, 'nonlocal' funcionó.
        self.assertGreater(contador(), 1,
                           "El contador debe ser mayor a 1 después de múltiples llamadas, verificando el 'nonlocal'.")


# --- Ejecución de las pruebas ---
if __name__ == '__main__':
    # Usamos unittest.main() con argumentos para que funcione correctamente en entornos interactivos
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
