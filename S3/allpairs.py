from allpairspy import AllPairs

parametros = [
    ["Ecuador", "Perú"],
    ["Chile", "México"],
    ["Económico", "Ejecutivo"]
]

# Generar combinación por pares
for i, pares in enumerate(AllPairs(parametros)):
    print(f"Prueba {i + 1}: {pares}")
