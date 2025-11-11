def calcular_descuento(edad):
    if edad < 0:
        return "Error: edad inválida"
    if edad < 18:
        return "Descuento infantil"
    elif edad > 65:
        return "Descuento tercera edad"
    else:
        return "Sin descuento"
