import pytest
from descuento import calcular_descuento

@pytest.mark.parametrize("edad,esperado", [
    (0, "Descuento infantil"),     # límite inferior extremo
    (17, "Descuento infantil"),     # límite superior de P1
    (18, "Sin descuento"),          # límite inferior de P2
    (65, "Sin descuento"),          # límite superior de P2
    (66, "Descuento tercera edad")  # límite inferior de P3
])
def test_calcular_descuento(edad, esperado):
    assert calcular_descuento(edad) == esperado
