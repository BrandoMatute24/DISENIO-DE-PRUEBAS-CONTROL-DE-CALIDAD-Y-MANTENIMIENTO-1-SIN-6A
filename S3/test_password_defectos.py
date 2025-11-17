# Por Brando Matute

from password import es_password_segura


def test_falla_si_no_cumple_longitud_minima():
    # Defecto: olvidar validar longitud mínima
    assert es_password_segura("Aa1") is False
    assert es_password_segura("Abc12") is False


def test_falla_si_no_tiene_mayusculas():
    # Defecto: no verificar presencia de mayúsculas
    assert es_password_segura("segura123") is False


def test_falla_si_no_tiene_minusculas():
    # Defecto: no verificar minúsculas
    assert es_password_segura("SEGURA123") is False


def test_falla_si_no_tiene_numeros():
    # Defecto: olvidar validar que tenga dígitos
    assert es_password_segura("SeguraSegura") is False


def test_acepta_password_totalmente_valida():
    # Caso positivo: debe pasar si NO tiene ninguno de los defectos anteriores
    assert es_password_segura("Segura123") is True
