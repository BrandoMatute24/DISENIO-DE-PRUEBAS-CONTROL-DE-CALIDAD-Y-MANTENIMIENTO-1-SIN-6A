# Por Brando Matute

def dividir(a, b):
    """
    Divide a entre b.

    Reglas:
    - b no puede ser 0
    - a y b deben ser números (int o float)
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a y b deben ser números")

    if b == 0:
        raise ValueError("No se puede dividir para cero")

    return a / b

def es_mayor_de_edad(edad):
    """
    Retorna True si edad >= 18.

    Reglas:
    - edad debe ser un entero
    - edad no puede ser negativa
    """
    if not isinstance(edad, int):
        raise TypeError("La edad debe ser un entero")

    if edad < 0:
        raise ValueError("La edad no puede ser negativa")

    return edad >= 18
