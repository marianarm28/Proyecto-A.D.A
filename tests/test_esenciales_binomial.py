import pytest
from proyecto.fuerza_bruta import caminos_binomial as caminos_recursivo
from proyecto.fuerza_bruta import encontrar_contacto_fuerza_bruta as encontrar_contacto_recursivo


# PRUEBAS PARA C(r,c)

def test_caminos_inicial_00():
    """C(0,0)=1."""
    assert caminos_recursivo(0, 0) == 1


def test_caminos_solo_derecha():
    """C(0,c)=1."""
    assert caminos_recursivo(0, 5) == 1


def test_caminos_solo_arriba():
    """C(r,0)=1."""
    assert caminos_recursivo(7, 0) == 1


def test_caminos_cuadricula_1x1():
    """C(1,1)=2."""
    assert caminos_recursivo(1, 1) == 2


def test_caminos_valor_conocido_3_2():
    """C(3,2)=10."""
    assert caminos_recursivo(3, 2) == 10


# PRUEBAS PARA encontrar_contacto(P)

def test_contacto_P_invalido():
    """P<=1 → None."""
    assert encontrar_contacto_recursivo(1) is None


def test_contacto_P_10():
    """P=10 → (3,2)."""
    assert encontrar_contacto_recursivo(10) == (3, 2)


def test_contacto_P_6():
    """P=6 → (2,2)."""
    assert encontrar_contacto_recursivo(6) == (2, 2)


def test_contacto_P_sin_solucion():
    """P=7 → None."""
    assert encontrar_contacto_recursivo(7) is None


def test_contacto_P_252():
    """P=252 → (5,5)."""
    assert encontrar_contacto_recursivo(252) == (5, 5)
