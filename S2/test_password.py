# Por Brando Matute

import pytest
from validador import validar_contraseña

@pytest.mark.parametrize("pw,esperado", [
    # Válidas (partición válida + bordes 6 y 10)
    ("abc123", "Válida"),          # 6 chars
    ("abcdefghij", "Válida"),      # 10 chars
    ("hola 12", "Válida"),         # caracteres variados (espacio permitido)

    # Inválidas por longitud
    ("abcde", "Error: longitud inválida"),      # 5
    ("abcdefghijkl", "Error: longitud inválida"),# 12
    ("", "Error: longitud inválida"),

    # Inválidas por diccionario (lista negra)
    ("password", "Error: en diccionario"),
    ("qwerty", "Error: en diccionario"),        # 6 pero en diccionario

    # Tipo inválido
    (None, "Error: tipo inválido"),
])
def test_validar_contraseña(pw, esperado):
    assert validar_contraseña(pw) == esperado
