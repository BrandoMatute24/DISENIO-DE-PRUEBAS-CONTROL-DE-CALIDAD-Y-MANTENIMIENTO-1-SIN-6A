# Por Brando Matute

from radon.complexity import cc_visit
import ast
from pathlib import Path

RUTA = Path("clasificar_riesgo.py")

def calcular_cc_y_predicados():
    codigo = RUTA.read_text(encoding="utf-8")

    print("== Complejidad ciclomática (radon) ==")
    bloques = cc_visit(codigo)
    for b in bloques:
        if b.name == "clasificar_riesgo":
            print(f"Función: {b.name}")
            print(f"  CC = {b.complexity}")
            print(f"  Línea inicio = {b.lineno}")
    print()

    print("== Predicados (condiciones if/elif) ==")
    tree = ast.parse(codigo)

    class PredVisitor(ast.NodeVisitor):
        def visit_If(self, node):
            condicion = ast.unparse(node.test)
            print(f"Línea {node.lineno}: {condicion}")
            self.generic_visit(node)

    PredVisitor().visit(tree)

if __name__ == "__main__":
    calcular_cc_y_predicados()
