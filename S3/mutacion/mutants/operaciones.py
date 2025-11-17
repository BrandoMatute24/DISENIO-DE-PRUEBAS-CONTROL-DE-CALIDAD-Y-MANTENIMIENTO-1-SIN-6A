# Por Brando Matute

from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result
def x_es_mayor_edad__mutmut_orig(edad: int) -> bool:
    return edad >= 18
def x_es_mayor_edad__mutmut_1(edad: int) -> bool:
    return edad > 18
def x_es_mayor_edad__mutmut_2(edad: int) -> bool:
    return edad >= 19

x_es_mayor_edad__mutmut_mutants : ClassVar[MutantDict] = {
'x_es_mayor_edad__mutmut_1': x_es_mayor_edad__mutmut_1, 
    'x_es_mayor_edad__mutmut_2': x_es_mayor_edad__mutmut_2
}

def es_mayor_edad(*args, **kwargs):
    result = _mutmut_trampoline(x_es_mayor_edad__mutmut_orig, x_es_mayor_edad__mutmut_mutants, args, kwargs)
    return result 

es_mayor_edad.__signature__ = _mutmut_signature(x_es_mayor_edad__mutmut_orig)
x_es_mayor_edad__mutmut_orig.__name__ = 'x_es_mayor_edad'


def x_descuento__mutmut_orig(precio: float, porcentaje: float) -> float:
    return precio - (precio * porcentaje / 100)


def x_descuento__mutmut_1(precio: float, porcentaje: float) -> float:
    return precio + (precio * porcentaje / 100)


def x_descuento__mutmut_2(precio: float, porcentaje: float) -> float:
    return precio - (precio * porcentaje * 100)


def x_descuento__mutmut_3(precio: float, porcentaje: float) -> float:
    return precio - (precio / porcentaje / 100)


def x_descuento__mutmut_4(precio: float, porcentaje: float) -> float:
    return precio - (precio * porcentaje / 101)

x_descuento__mutmut_mutants : ClassVar[MutantDict] = {
'x_descuento__mutmut_1': x_descuento__mutmut_1, 
    'x_descuento__mutmut_2': x_descuento__mutmut_2, 
    'x_descuento__mutmut_3': x_descuento__mutmut_3, 
    'x_descuento__mutmut_4': x_descuento__mutmut_4
}

def descuento(*args, **kwargs):
    result = _mutmut_trampoline(x_descuento__mutmut_orig, x_descuento__mutmut_mutants, args, kwargs)
    return result 

descuento.__signature__ = _mutmut_signature(x_descuento__mutmut_orig)
x_descuento__mutmut_orig.__name__ = 'x_descuento'
