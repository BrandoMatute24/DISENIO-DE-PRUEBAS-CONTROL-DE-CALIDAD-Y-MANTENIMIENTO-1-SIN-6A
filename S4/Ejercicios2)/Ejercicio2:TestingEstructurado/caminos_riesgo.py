# Por Brando Matute

from itertools import product
from clasificar_riesgo import clasificar_riesgo


def identificar_camino(edad, historial, monto):
    """
    Asigna un id de camino base según las decisiones.
    Coincide con lo que analizaste a mano:
      C1: edad < 25 y historial == "malo"          -> camino 1
      C2: edad < 25 y historial != "malo"          -> camino 2
      C3: edad >= 25 y monto > 50000               -> camino 3
      C4: edad >= 25, monto <= 50000, hist == exc  -> camino 4
      C5: edad >= 25, monto <= 50000, hist != exc  -> camino 5
    """
    if edad < 25:
        if historial == "malo":
            return 1
        else:
            return 2
    else:
        if monto > 50000:
            return 3
        elif historial == "excelente":
            return 4
        else:
            return 5

def generar_casos_por_camino():
    # Valores candidatos para explorar el espacio
    edades = [20, 22, 25, 30, 35, 40]
    historiales = ["malo", "bueno", "excelente"]
    montos = [30000, 40000, 60000]

    ejemplos_por_camino = {}

    for edad, historial, monto in product(edades, historiales, montos):
        camino = identificar_camino(edad, historial, monto)
        if camino not in ejemplos_por_camino:
            resultado = clasificar_riesgo(edad, historial, monto)
            ejemplos_por_camino[camino] = (edad, historial, monto, resultado)

        # Si ya tenemos los 5 caminos, podemos cortar
        if len(ejemplos_por_camino) == 5:
            break

    print("== Casos de prueba generados por camino base ==")
    for camino in sorted(ejemplos_por_camino):
        edad, historial, monto, resultado = ejemplos_por_camino[camino]
        print(
            f"Camino {camino}: edad={edad}, historial='{historial}', "
            f"monto={monto} -> resultado='{resultado}'"
        )

    print("\n== Formato pytest.parametrize para pegar en el test ==")
    for camino in sorted(ejemplos_por_camino):
        edad, historial, monto, resultado = ejemplos_por_camino[camino]
        print(f"({edad}, '{historial}', {monto}, '{resultado}'),")

if __name__ == "__main__":
    generar_casos_por_camino()
