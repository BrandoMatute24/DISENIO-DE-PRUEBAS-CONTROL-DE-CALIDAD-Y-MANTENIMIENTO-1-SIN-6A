def procesar_transaccion(monto, tipo, usuario):
    comision = 0.02
    total = monto
    
    if tipo == "internacional":
        recargo = monto * 0.05  # ❌ Definida pero no usada
        comision = 0.03
    
    if usuario.es_premium:  # ❌ usuario puede no tener .es_premium
        total = monto * (1 - comision)
    
    # ❌ 'resultado' no está definida en todos los caminos
    if total > 0:
        resultado = "Aprobada"
    
    return resultado
