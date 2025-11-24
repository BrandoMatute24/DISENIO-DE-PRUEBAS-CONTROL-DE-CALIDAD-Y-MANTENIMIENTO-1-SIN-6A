# Por Brando Matute

import itertools
from prestamo import autorizar_prestamo

valores_edad = {True: 25, False: 17}
valores_ingreso = {True: 2500, False: 1500}
valores_historial = {True: "bueno", False: "malo"}

print("Matriz de pruebas para cobertura de condición múltiple (2^3 = 8 casos):\n")

print("{:<3} {:<5} {:<8} {:<12} {:<3} {:<3} {:<3} {}".format(
    "#", "edad", "ingreso", "historial", "C1", "C2", "C3", "Resultado"
))

contador = 1

for c1, c2, c3 in itertools.product([False, True], repeat=3):
    edad = valores_edad[c1]
    ingreso = valores_ingreso[c2]
    historial = valores_historial[c3]

    resultado = autorizar_prestamo(edad, ingreso, historial)

    print("{:<3} {:<5} {:<8} {:<12} {:<3} {:<3} {:<3} {}".format(
        contador, edad, ingreso, historial, 
        "T" if c1 else "F",
        "T" if c2 else "F",
        "T" if c3 else "F",
        resultado
    ))
    contador += 1
