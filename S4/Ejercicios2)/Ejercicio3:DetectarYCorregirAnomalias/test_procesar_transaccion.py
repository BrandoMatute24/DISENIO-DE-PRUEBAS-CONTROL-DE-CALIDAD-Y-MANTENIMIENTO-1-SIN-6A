# Por Brando Matute

import types
from procesar_transaccion import procesar_transaccion_corregida

def crear_usuario(es_premium=None):
    """Crea objetos tipo usuario para probar distintos escenarios."""
    user = types.SimpleNamespace()
    if es_premium is not None:
        user.es_premium = es_premium
    return user

def test_transaccion_nacional_no_premium_aprobada():
    usuario = crear_usuario(es_premium=False)
    resultado = procesar_transaccion_corregida(1000, "nacional", usuario)
    assert resultado == "Aprobada"


def test_transaccion_internacional_no_premium_aprobada():
    usuario = crear_usuario(es_premium=False)
    resultado = procesar_transaccion_corregida(1000, "internacional", usuario)
    assert resultado == "Aprobada"

def test_transaccion_internacional_premium_aprobada():
    usuario = crear_usuario(es_premium=True)
    resultado = procesar_transaccion_corregida(1000, "internacional", usuario)
    assert resultado == "Aprobada"


def test_usuario_sin_atributo_es_premium_no_revienta():
    # usuario sin atributo es_premium → debe asumirse como no premium (False)
    usuario = crear_usuario()  # sin es_premium
    resultado = procesar_transaccion_corregida(1000, "nacional", usuario)
    assert resultado == "Aprobada"

def test_transaccion_con_monto_no_positivo_rechazada():
    usuario = crear_usuario(es_premium=False)
    resultado = procesar_transaccion_corregida(0, "nacional", usuario)
    assert resultado == "Rechazada"
