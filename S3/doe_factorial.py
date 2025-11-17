# Por Brando Matute

from pyDOE3 import ff2n

def casos_prueba():
    diseño = ff2n(3)

    mapas = [
        {-1: "Temp Baja",  1: "Temp Alta"},
        {-1: "Tiempo Corto", 1: "Tiempo Largo"},
        {-1: "Rejilla Cerrada", 1: "Rejilla Abierta"}
    ]

    # Convertir cada fila del diseño en un caso de prueba con valores reales
    return [
        (mapas[0][int(t)], mapas[1][int(x)], mapas[2][int(r)])
        for t, x, r in diseño
    ]

