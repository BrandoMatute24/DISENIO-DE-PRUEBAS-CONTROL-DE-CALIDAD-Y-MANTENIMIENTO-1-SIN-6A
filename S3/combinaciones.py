from itertools import product

parametros = {
    "origen": ["Ecuador", "Perú"],
    "destino": ["Chile", "México"],
    "asiento": ["Económico", "Ejecutivo"]
}

combinaciones_completas = list(product(*parametros.values()))

print(f"Número total de combinaciones: {len(combinaciones_completas)}\n")
for c in combinaciones_completas:
    print(dict(zip(parametros.keys(), c)))
