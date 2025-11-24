def calcular_impuesto(salario, dependientes, es_jubilado):
    impuesto_base = salario * 0.15
    descuento = 0
    
    if dependientes > 0:
        descuento = dependientes * 500
    
    if es_jubilado:
        descuento += salario * 0.05
    
    impuesto_final = impuesto_base - descuento
    return max(0, impuesto_final)
