# Por Brando Matute

from radon.complexity import cc_visit, cc_rank

def calcular_complejidad_archivo(ruta_archivo: str):
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        codigo = f.read()
    bloques = cc_visit(codigo)

    print(f"Complejidad ciclomática por bloque en: {ruta_archivo}\n")
    for b in bloques:
        letra = cc_rank(b.complexity)
        print(
            f"- {b.name} (línea {b.lineno}): "
            f"CC = {b.complexity} (rango {letra})"
        )

    complejidad_total = sum(b.complexity for b in bloques)
    print(f"\nComplejidad ciclomática total del archivo: {complejidad_total}")

if __name__ == "__main__":
    calcular_complejidad_archivo("complejidad.py")
