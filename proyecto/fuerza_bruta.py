from proyecto.comun import encontrar_contacto_generico, METRICAS

def factorial_con_conteo(k):
    res = 1
    for i in range(2, k + 1):
        METRICAS["ops"] += 1 # Multiplicación
        METRICAS["calls"] += 1 # Iteración
        res *= i
    return res

def C_formula_manual(m, n):
    METRICAS["calls"] += 1 # Llamada principal
    
    # Numerador: m! (ojo: la fórmula es binom(m, n))
    num = factorial_con_conteo(m)
    
    # Denominador: n! * (m-n)!
    den1 = factorial_con_conteo(n)
    den2 = factorial_con_conteo(m - n)
    
    # Operación final: Multiplicación del den y División
    METRICAS["ops"] += 2 
    
    return num // (den1 * den2)

def encontrar_contacto_fuerza_bruta(P):
    return encontrar_contacto_generico(P, C_formula_manual)