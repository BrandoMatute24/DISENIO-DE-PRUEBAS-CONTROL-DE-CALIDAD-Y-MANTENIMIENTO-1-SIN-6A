from pyDOE3 import ff3n
import pandas as pd

# Generar diseño factorial 2^3 (3 factores binarios)
diseño = ff3n(3)

# Crear un DataFrame con nombres de factores
df = pd.DataFrame(diseño, columns=["Temperatura", "Tiempo", "Rejilla"])

print(df)
