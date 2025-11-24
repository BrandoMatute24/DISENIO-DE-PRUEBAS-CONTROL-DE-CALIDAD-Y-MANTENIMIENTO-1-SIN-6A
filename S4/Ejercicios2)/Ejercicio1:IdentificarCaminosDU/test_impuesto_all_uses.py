# Por Brando Matute

import pytest
from impuestos import calcular_impuesto

@pytest.mark.parametrize(
    "salario, dependientes, es_jubilado, descripcion",
    [
        # Caso A: sin dependientes, no jubilado
        # Cubre DU: 1->2, 1->5, 2->11, 3->11, 11->12, 1->8
        (10000, 0, False, "sin dependientes, no jubilado"),

        # Caso B: sin dependientes, jubilado
        # Cubre DU: 1->2, 1->5, 1->8, 1->9, 3->9, 9->11, 2->11, 11->12
        (10000, 0, True, "sin dependientes, jubilado"),

        # Caso C: con dependientes, no jubilado
        # Cubre DU: 1->2, 1->5, 1->6, 6->11, 2->11, 11->12
        (10000, 2, False, "con dependientes, no jubilado"),

        # Caso D: con dependientes, jubilado
        # Cubre DU: 1->2, 1->5, 1->6, 1->8, 1->9, 6->9, 9->11, 2->11, 11->12
        (10000, 2, True, "con dependientes, jubilado"),
    ],
)
def test_all_uses_calcular_impuesto(salario, dependientes, es_jubilado, descripcion):
    impuesto = calcular_impuesto(salario, dependientes, es_jubilado)
    assert isinstance(impuesto, (int, float)), f"Resultado no numérico en caso: {descripcion}"
    assert impuesto >= 0, f"Resultado negativo en caso: {descripcion}"
