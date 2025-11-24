# Por Brando Matute

import ast
from collections import defaultdict

RUTA_ARCHIVO = "impuestos.py"
NOMBRE_FUNCION = "calcular_impuesto"


class DUVisitor(ast.NodeVisitor):
    def __init__(self, params, func_lineno):
        self.params = set(params)
        self.func_lineno = func_lineno

        self.locals = set()

        self.defs = defaultdict(list)
        self.c_uses = defaultdict(list)
        self.p_uses = defaultdict(list)

        self.in_predicate = False

    # -------- DEF (asignaciones) --------

    def visit_Assign(self, node: ast.Assign):
        for target in node.targets:
            if isinstance(target, ast.Name):
                name = target.id
                self.locals.add(name)
                self.defs[name].append(node.lineno)
        self.generic_visit(node)

    def visit_AugAssign(self, node: ast.AugAssign):
        if isinstance(node.target, ast.Name):
            name = node.target.id
            self.locals.add(name)
            self.defs[name].append(node.lineno)
        self.generic_visit(node)

    # -------- P-USE (condiciones) --------

    def visit_If(self, node: ast.If):
        self.in_predicate = True
        self.visit(node.test)
        self.in_predicate = False

        for stmt in node.body + node.orelse:
            self.visit(stmt)

    # -------- C-USE / P-USE (lecturas) --------

    def visit_Name(self, node: ast.Name):
        if not isinstance(node.ctx, ast.Load):
            return

        name = node.id

        if name not in self.params and name not in self.locals:
            return

        if self.in_predicate:
            self.p_uses[name].append(node.lineno)
        else:
            self.c_uses[name].append(node.lineno)


def calcular_du_pairs(visitor: DUVisitor, params, func_lineno):
    du_pairs = defaultdict(list)

    for var in set(params) | set(visitor.defs) | set(visitor.c_uses) | set(visitor.p_uses):
        # línea de definición de parámetros (firma)
        def_lines = []
        if var in params:
            def_lines.append(func_lineno)   # DEF implícita en la firma

        def_lines.extend(visitor.defs.get(var, []))
        def_lines = sorted(set(def_lines))

        use_lines = sorted(set(visitor.c_uses.get(var, []) + visitor.p_uses.get(var, [])))

        if not use_lines:
            continue

        # Para cada DEF, asociar los USE posteriores hasta la siguiente DEF
        for i, d in enumerate(def_lines):
            next_def = def_lines[i + 1] if i + 1 < len(def_lines) else float('inf')
            for u in use_lines:
                if d < u < next_def:
                    du_pairs[var].append((d, u))

    return du_pairs


def analizar_funcion():
    with open(RUTA_ARCHIVO, "r", encoding="utf-8") as f:
        source = f.read()

    tree = ast.parse(source)

    funcion_obj = None
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == NOMBRE_FUNCION:
            funcion_obj = node
            break

    if funcion_obj is None:
        print(f"No se encontró la función {NOMBRE_FUNCION}")
        return

    params = [arg.arg for arg in funcion_obj.args.args]
    func_lineno = funcion_obj.lineno

    visitor = DUVisitor(params, func_lineno)
    visitor.visit(funcion_obj)

    print(f"Análisis DEF / USE de la función '{NOMBRE_FUNCION}':\n")
    print("Parámetros (DEF implícito en la firma):", params)

    print("\nVariables locales y parámetros:")
    todas_vars = set(params) | set(visitor.defs) | set(visitor.c_uses) | set(visitor.p_uses)

    for var in sorted(todas_vars):
        print(f"\nVariable '{var}':")

        if var in visitor.defs:
            print(f"  DEF  en líneas: {sorted(set(visitor.defs[var]))}")
        else:
            if var in params:
                print("  DEF  en líneas: [parámetro de entrada]")
            else:
                print("  DEF  en líneas: []")

        print(f"  C-USE en líneas: {sorted(set(visitor.c_uses.get(var, [])))}")
        print(f"  P-USE en líneas: {sorted(set(visitor.p_uses.get(var, [])))}")

    # ---- Cálculo de caminos DU ----
    du_pairs = calcular_du_pairs(visitor, params, func_lineno)

    print("\nCaminos DU (DEF -> USE):")
    for var in sorted(du_pairs):
        print(f"\nVariable '{var}':")
        for d, u in du_pairs[var]:
            print(f"  DU: {d} -> {u}")


if __name__ == "__main__":
    analizar_funcion()
