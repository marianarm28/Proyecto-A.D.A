from proyecto.comun import encontrar_contacto_generico, METRICAS
import sys

sys.setrecursionlimit(20000)

# Cache manual
memo_cache = {}

def C_memo_interna(m, n):
    METRICAS["calls"] += 1 # Contamos la llamada (sea recursiva o lookup)
    
    state = (m, n)
    if state in memo_cache:
        # Si está en caché, solo retornamos (costo O(1), no sumamos ops de cálculo)
        return memo_cache[state]
    
    if n == 0 or n == m:
        return 1
    if n > m:
        return 0
    
    # Operación básica: Suma
    METRICAS["ops"] += 1
    res = C_memo_interna(m - 1, n - 1) + C_memo_interna(m - 1, n)
    
    memo_cache[state] = res
    return res

def encontrar_contacto_memo(P):
    memo_cache.clear() # Limpiamos antes de empezar la búsqueda de P
    return encontrar_contacto_generico(P, C_memo_interna)