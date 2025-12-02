from proyecto.comun import encontrar_contacto_generico, METRICAS
import sys

# Aumentamos límite para pruebas
sys.setrecursionlimit(20000)

def C_recursivo(m, n):
    METRICAS["calls"] += 1 # Una llamada más
    
    if n == 0 or n == m:
        return 1
    if n > m:
        return 0
    
    # Si llega aquí, hará una SUMA (+) -> 1 Operación Básica
    METRICAS["ops"] += 1 
    return C_recursivo(m - 1, n - 1) + C_recursivo(m - 1, n)

def encontrar_contacto_recursivo(P):
    return encontrar_contacto_generico(P, C_recursivo)