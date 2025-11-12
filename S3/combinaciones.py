from itertools import product

# Definir los parámetros del sistema
parametros = {
    "origen": ["Ecuador", "Perú"],
    "destino": ["Chile", "México"],
    "asiento": ["Económico", "Ejecutivo"]
}

# Generar TODAS las combinaciones posibles (diseño factorial completo)
combinaciones_completas = list(product(*parametros.values()))

print(f"Número total de combinaciones: {len(combinaciones_completas)}\n")

for c in combinaciones_completas:
    print(dict(zip(parametros.keys(), c)))
