# Por Brando Matute

def suma_lista(numeros):
    total = 0
    for n in numeros:
        total += n
    return total

def buscar_mayor(numeros):
    if not numeros:
        return None
    mayor = numeros[0]
    for n in numeros[1:]:
        if n > mayor:
            mayor = n
    return mayor

def normalizar(valores):
    if not valores:
        return []
    minimo = min(valores)
    maximo = max(valores)
    rango = maximo - minimo
    if rango == 0:
        return [1 for _ in valores]
    return [(v - minimo) / rango for v in valores]
