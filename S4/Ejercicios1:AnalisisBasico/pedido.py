# Por Brando Matute

def procesar_pedido(cantidad, es_miembro, tiene_descuento):
    total = cantidad * 10
    
    if es_miembro:
        total *= 0.9
    
    if tiene_descuento:
        total *= 0.95
    
    return total
