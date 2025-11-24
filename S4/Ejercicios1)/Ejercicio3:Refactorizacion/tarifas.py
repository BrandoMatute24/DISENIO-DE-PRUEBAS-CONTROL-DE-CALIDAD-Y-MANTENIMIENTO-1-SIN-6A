# Por Brando Matute

# Version Original

def calcular_tarifa_original(edad, es_estudiante, es_senior, dia_semana, hora):
    tarifa = 10
    
    if edad < 12:
        tarifa = 5
    elif edad >= 65:
        tarifa = 6
    
    if es_estudiante:
        tarifa *= 0.8
    
    if es_senior:
        tarifa *= 0.7
    
    if dia_semana in ["sabado", "domingo"]:
        tarifa *= 1.5
    
    if hora >= 18:
        tarifa *= 1.2
    
    return tarifa



# Version Refactorizada

def base_tarifa_por_edad(edad):
    if edad < 12:
        return 5
    if edad >= 65:
        return 6
    return 10

def factor_por_persona(es_estudiante, es_senior):
    factor = 1.0
    if es_estudiante:
        factor *= 0.8
    if es_senior:
        factor *= 0.7
    return factor

def factor_por_dia(dia_semana):
    return 1.5 if dia_semana in ("sabado", "domingo") else 1.0

def factor_por_hora(hora):
    return 1.2 if hora >= 18 else 1.0

def calcular_tarifa_refactorizada(edad, es_estudiante, es_senior, dia_semana, hora):
    tarifa = base_tarifa_por_edad(edad)
    tarifa *= factor_por_persona(es_estudiante, es_senior)
    tarifa *= factor_por_dia(dia_semana)
    tarifa *= factor_por_hora(hora)
    return tarifa
