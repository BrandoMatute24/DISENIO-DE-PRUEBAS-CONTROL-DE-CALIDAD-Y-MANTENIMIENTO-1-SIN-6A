# Por Brando Matute

from pyDOE3 import ff2n
import pandas as pd

diseño = ff2n(3)

df = pd.DataFrame(diseño, columns=["Temperatura", "Tiempo", "Rejilla"])

print(df)
