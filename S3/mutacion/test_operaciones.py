# Por Brando Matute

from operaciones import es_mayor_edad, descuento


def test_es_mayor_edad():
    assert es_mayor_edad(18) is True
    assert es_mayor_edad(17) is False


def test_descuento():
    assert descuento(100, 10) == 90
    assert descuento(200, 25) == 150
