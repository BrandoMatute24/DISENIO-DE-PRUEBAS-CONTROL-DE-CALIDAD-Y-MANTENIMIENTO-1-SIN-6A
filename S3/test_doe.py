# Por Brando Matute

import pytest
from doe_factorial import casos_prueba

@pytest.mark.parametrize("temp, tiempo, rejilla", casos_prueba())
def test_combinaciones_validas(temp, tiempo, rejilla):
    # Aquí iría la función real a probar.
    # Esto es solo un ejemplo para demostrar el test.
    resultado = True  

    assert resultado is True
