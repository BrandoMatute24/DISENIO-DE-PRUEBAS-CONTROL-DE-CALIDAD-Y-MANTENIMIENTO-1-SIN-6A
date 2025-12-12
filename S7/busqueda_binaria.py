# Por Brando Matute

def busqueda_binaria(lista, objetivo):
    """
    Realiza una búsqueda binaria en una lista ordenada.

    Parámetros:
    - lista: Lista de elementos ordenados.
    - objetivo: Elemento a buscar.

    Retorna:
    - Índice del objetivo si se encuentra en la lista; -1 si no está presente.
    """
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1
