# Por Brando Matute

import itertools
import pytest
from tarifas import calcular_tarifa_original, calcular_tarifa_refactorizada


@pytest.mark.parametrize(
    "edad", [10, 30, 70]
)
@pytest.mark.parametrize(
    "es_estudiante", [False, True]
)
@pytest.mark.parametrize(
    "es_senior", [False, True]
)
@pytest.mark.parametrize(
    "dia_semana", ["lunes", "sabado"]
)
@pytest.mark.parametrize(
    "hora", [10, 19]
)
def test_equivalencia_tarifas(edad, es_estudiante, es_senior, dia_semana, hora):
    original = calcular_tarifa_original(
        edad, es_estudiante, es_senior, dia_semana, hora
    )
    refactor = calcular_tarifa_refactorizada(
        edad, es_estudiante, es_senior, dia_semana, hora
    )
    # Se compara con approx por posibles decimales flotantes
    assert refactor == pytest.approx(original)
