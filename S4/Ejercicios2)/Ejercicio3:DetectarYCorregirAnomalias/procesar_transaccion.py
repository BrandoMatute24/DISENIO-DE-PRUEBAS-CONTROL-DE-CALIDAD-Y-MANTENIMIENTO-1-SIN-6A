# Por Brando Matute

def procesar_transaccion_corregida(monto, tipo, usuario):
    """
    Procesa una transacción aplicando recargos y comisiones.
    - Internacional: recargo del 5% y comisión del 3%.
    - Normal: comisión del 2%.
    - Cliente premium: se descuenta la comisión sobre el total.
    Devuelve "Aprobada" o "Rechazada".
    """
    comision = 0.02
    total = monto

    # Aplicar recargo y comisión especial para transacciones internacionales
    if tipo == "internacional":
        recargo = monto * 0.05           # ahora sí se usa
        total += recargo                 # se suma el recargo al total
        comision = 0.03                  # comisión internacional

    # Leer de forma segura si el usuario es premium (si no tiene atributo, asumimos False)
    es_premium = getattr(usuario, "es_premium", False)

    if es_premium:
        # se descuenta la comisión sobre el total actual
        total = total * (1 - comision)

    # Definir 'resultado' en todos los caminos
    if total > 0:
        resultado = "Aprobada"
    else:
        resultado = "Rechazada"

    return resultado
