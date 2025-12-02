import pytest
from proyecto.recursivo import caminos_recursivo, encontrar_contacto_recursivo



#  PRUEBAS PARA C(r,c)


def test_caminos_inicial_00():
    """
    Verifica el caso base mínimo:
    C(0,0) debe ser igual a 1,
    ya que no existe movimiento posible.
    """
    assert caminos_recursivo(0, 0) == 1


def test_caminos_solo_derecha():
    """
    Verifica que cuando r = 0, únicamente se puede mover a la derecha.
    Por tanto, C(0,c) debe ser siempre 1.
    """
    assert caminos_recursivo(0, 5) == 1


def test_caminos_solo_arriba():
    """
    Verifica que cuando c = 0, solo existen movimientos hacia arriba.
    Por eso, C(r,0) debe ser 1.
    """
    assert caminos_recursivo(7, 0) == 1


def test_caminos_cuadricula_1x1():
    """
    En una cuadrícula 1x1 existen exactamente 2 caminos:
    (Derecha → Arriba) o (Arriba → Derecha).
    """
    assert caminos_recursivo(1, 1) == 2


def test_caminos_valor_conocido_3_2():
    """
    Prueba un valor conocido del problema:
    C(3,2) = 10.
    """
    assert caminos_recursivo(3, 2) == 10



# PRUEBAS PARA encontrar_contacto(P)


def test_contacto_P_invalido():
    """
    Si P <= 1, según la regla del problema NO existe solución válida
    para (m, n) porque debe cumplirse n > 1.
    """
    assert encontrar_contacto_recursivo(1) is None
    assert encontrar_contacto_recursivo(0) is None


def test_contacto_P_10():
    """
    Caso principal del problema:
    P = 10 debe devolver (3,2).
    """
    assert encontrar_contacto_recursivo(10) == (3, 2)


def test_contacto_P_6():
    """
    Caso pequeño válido:
    P = 6 debe devolver (2,2).
    """
    assert encontrar_contacto_recursivo(6) == (2, 2)


def test_contacto_P_sin_solucion():
    """
    Si P no corresponde al valor de ningún C(m,n),
    la función debe regresar None.
    Ejemplo: P = 7 no tiene solución válida.
    """
    assert encontrar_contacto_recursivo(7) is None


def test_contacto_P_252():
    """
    Caso válido más grande:
    P = 252 corresponde a (5,5).
    """
    assert encontrar_contacto_recursivo(252) == (5, 5)
