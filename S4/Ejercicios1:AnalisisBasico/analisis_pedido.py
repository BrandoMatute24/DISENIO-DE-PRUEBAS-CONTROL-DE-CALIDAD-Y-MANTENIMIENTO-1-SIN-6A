# Por Brando Matute

import ast
import itertools
from pedido import procesar_pedido

with open("pedido.py", "r", encoding="utf-8") as f:
    source = f.read()

# Aqui se parsea el código a un árbol de sintaxis (AST)
tree = ast.parse(source)

# Aqui se cuentan los predicados (if) recorriendo el AST
class PredicateCounter(ast.NodeVisitor):
    def __init__(self):
        self.if_count = 0

    def visit_If(self, node):
        self.if_count += 1
        # Se sigue recorriendo si es que hay if anidados
        self.generic_visit(node)

counter = PredicateCounter()
counter.visit(tree)

num_predicados = counter.if_count
complejidad_ciclomatica = num_predicados + 1
caminos_base = complejidad_ciclomatica

print(f"Número de predicados: {num_predicados}")
print(f"Complejidad ciclomática: {complejidad_ciclomatica}")
print(f"Número de caminos base: {caminos_base}")

# Se generan los casos de prueba para cubrir todas las combinaciones de ramas
print("\nCasos de prueba sugeridos (cantidad fija en 10):")
cantidad = 10
for es_miembro, tiene_descuento in itertools.product([False, True], repeat=2):
    resultado = procesar_pedido(cantidad, es_miembro, tiene_descuento)
    print(f"cantidad={cantidad}, es_miembro={es_miembro}, tiene_descuento={tiene_descuento} -> total={resultado}")
