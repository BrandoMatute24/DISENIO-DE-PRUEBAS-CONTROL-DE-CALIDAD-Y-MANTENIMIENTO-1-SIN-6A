def beneficios_cliente(es_miembro: bool, plazo_incumplido: bool, es_15_renta: bool):
    # Si no es miembro o incumplió el plazo, no hay beneficios
    if not es_miembro or plazo_incumplido:
        return []
    # Miembro y al día: siempre descuento; camiseta sólo si es la 15ª renta
    beneficios = ["Descuento 20%"]
    if es_15_renta:
        beneficios.append("Camiseta")
    return beneficios
