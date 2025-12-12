import pandas as pd

casos = pd.DataFrame([
    ["TC01", "Transferencia válida", 3, 3],
    ["TC02", "Transferencia sin saldo", 3, 2],
    ["TC03", "Login con credenciales válidas", 3, 2],
    ["TC04", "Login incorrecto", 2, 2],
    ["TC05", "Pago básico", 2, 2],
    ["TC06", "Actualizar perfil", 1, 1],
], columns=["ID", "Descripción", "Impacto", "Probabilidad"])

casos["Riesgo"] = casos["Impacto"] * casos["Probabilidad"]

print(casos.sort_values("Riesgo", ascending=False))