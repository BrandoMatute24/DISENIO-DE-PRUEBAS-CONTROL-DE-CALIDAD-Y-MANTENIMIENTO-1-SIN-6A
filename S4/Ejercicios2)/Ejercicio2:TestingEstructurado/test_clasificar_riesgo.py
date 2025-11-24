# Por Brando Matute

import pytest
from clasificar_riesgo import clasificar_riesgo

@pytest.mark.parametrize(
    "edad, historial, monto, esperado",
    [
        (20, "malo", 30000, "ALTO"),       # Camino 1
        (20, "bueno", 30000, "MEDIO"),     # Camino 2
        (25, "malo", 60000, "ALTO"),       # Camino 3
        (25, "excelente", 30000, "BAJO"),  # Camino 4
        (25, "malo", 30000, "MEDIO"),      # Camino 5
    ]
)
def test_caminos_base_clasificar_riesgo(edad, historial, monto, esperado):
    assert clasificar_riesgo(edad, historial, monto) == esperado
