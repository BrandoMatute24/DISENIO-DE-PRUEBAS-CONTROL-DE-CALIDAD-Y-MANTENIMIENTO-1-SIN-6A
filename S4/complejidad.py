# Por Brando Matute

def clasificar_numero(n):
    if n > 0:
        if n % 2 == 0:
            return "positivo par"
        else:
            return "positivo impar"
    elif n < 0:
        return "negativo"
    else:
        return "cero"

def contar_positivos(lista):
    count = 0
    for x in lista:
        if x > 0:
            count += 1
    return count

def buscar_elemento(lista, objetivo):
    i = 0
    while i < len(lista):
        if lista[i] == objetivo:
            return True
        i += 1
    return False
