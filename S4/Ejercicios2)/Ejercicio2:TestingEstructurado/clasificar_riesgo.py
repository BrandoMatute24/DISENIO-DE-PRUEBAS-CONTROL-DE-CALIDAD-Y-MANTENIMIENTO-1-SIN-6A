def clasificar_riesgo(edad, historial, monto):
    if edad < 25:
        if historial == "malo":
            return "ALTO"
        else:
            return "MEDIO"
    else:
        if monto > 50000:
            return "ALTO"
        elif historial == "excelente":
            return "BAJO"
        else:
            return "MEDIO"