# Por Brando Matute

from typing import Iterable

def validar_contraseña(pw, diccionario: Iterable[str] | None = None):
    """
    Reglas:
      - Longitud entre 6 y 10 (inclusive).
      - No debe estar en el diccionario (lista negra).
      - No restringimos tipos de caracteres (se permiten símbolos/espacios).
    Retorna un string con el resultado.
    """
    if not isinstance(pw, str):
        return "Error: tipo inválido"
    if diccionario is None:
        diccionario = {"password", "123456", "qwerty", "letmein"}

    n = len(pw)
    if n < 6 or n > 10:
        return "Error: longitud inválida"
    if pw in diccionario:
        return "Error: en diccionario"
    return "Válida"