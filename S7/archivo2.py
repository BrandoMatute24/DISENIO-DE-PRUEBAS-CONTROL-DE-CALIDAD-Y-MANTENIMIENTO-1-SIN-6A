# Evaluador simple de riesgo basado en impacto y probabilidad

# Escalas sugeridas por ISTQB: 1=bajo, 2=medio, 3=alto

funcionalidades = {
    "Login": {"impacto": 3, "probabilidad": 2},
    "Transferencia": {"impacto": 3, "probabilidad": 3},
    "Pagos": {"impacto": 2, "probabilidad": 2},
    "Perfil": {"impacto": 1, "probabilidad": 1},
}

def calcular_riesgo(f):
    return f["impacto"] * f["probabilidad"]

riesgos = {k: calcular_riesgo(v) for k, v in funcionalidades.items()}

for f, r in sorted(riesgos.items(), key=lambda x: x[1], reverse=True):
    print(f"{f}: Riesgo = {r}")
