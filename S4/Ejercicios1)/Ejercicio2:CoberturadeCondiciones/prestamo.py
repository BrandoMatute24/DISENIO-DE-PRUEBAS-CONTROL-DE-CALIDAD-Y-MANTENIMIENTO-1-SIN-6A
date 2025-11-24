# Por Brando Matute

def autorizar_prestamo(edad, ingreso, historial_crediticio):
    if edad >= 18 and ingreso >= 2000 and historial_crediticio == "bueno":
        return "APROBADO"
    return "RECHAZADO"
