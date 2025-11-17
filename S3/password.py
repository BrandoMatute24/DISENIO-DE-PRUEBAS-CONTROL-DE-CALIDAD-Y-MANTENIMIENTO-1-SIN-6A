# Por Brando Matute

def es_password_segura(password: str) -> bool:
    """
    Devuelve True si la contraseña es "segura":
    - Al menos 8 caracteres
    - Al menos una mayúscula
    - Al menos una minúscula
    - Al menos un dígito
    """
    if len(password) < 8:
        return False

    tiene_mayus = any(c.isupper() for c in password)
    tiene_minus = any(c.islower() for c in password)
    tiene_num = any(c.isdigit() for c in password)

    return tiene_mayus and tiene_minus and tiene_num
