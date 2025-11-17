# Por Brando matute

from hypothesis import given
from hypothesis import strategies as st
from suma import suma_lista

# Estrategia:
# - Una lista de enteros (mínimo 1 elemento)
# - Una constante entera c
@given(
    st.lists(st.integers(), min_size=1, max_size=20),
    st.integers()
)
def test_suma_metamorfica_constante(lista, c):
    suma_original = suma_lista(lista)

    # Transformación metamórfica: sumar c a cada elemento
    lista_transformada = [x + c for x in lista]
    suma_transformada = suma_lista(lista_transformada)

    # Relación metamórfica que debe cumplirse siempre
    assert suma_transformada == suma_original + c * len(lista)
