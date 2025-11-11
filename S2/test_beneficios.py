import pytest
from beneficios import beneficios_cliente

@pytest.mark.parametrize("es_miembro,plazo_incumplido,es_15_renta,esperado", [
    # R1: V, V, F  → (miembro, al día, no 15ª) -> descuento
    (True,  False, False, ["Descuento 20%"]),
    # R2: V, V, V  → (miembro, al día, 15ª) -> descuento + camiseta
    (True,  False, True,  ["Descuento 20%", "Camiseta"]),
    # R3: V, F, F  → (miembro, incumplió, no 15ª) -> sin beneficios
    (True,  True,  False, []),
    # R4: F, -, -  → (no miembro) -> sin beneficios
    (False, False, False, []),

    # Casos adicionales para cerrar huecos:
    # no miembro en 15ª -> sigue sin beneficios
    (False, False, True, []),
    # miembro que incumple en 15ª -> sin beneficios
    (True,  True,  True, []),
])
def test_beneficios_cliente(es_miembro, plazo_incumplido, es_15_renta, esperado):
    assert beneficios_cliente(es_miembro, plazo_incumplido, es_15_renta) == esperado
