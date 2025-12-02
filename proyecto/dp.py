from proyecto.comun import encontrar_contacto_generico, METRICAS

def C_dp(m, n):
    METRICAS["calls"] += 1 # 1 llamada a la función principal
    
    if n < 0 or n > m: return 0
    if n == 0 or n == m: return 1
    if n > m // 2: n = m - n
    
    fila = [1] * (n + 1)
    
    # Ciclo principal
    for i in range(2, m + 1):
        # Ciclo interno
        # Range(min(i - 1, n), 0, -1)
        inicio = min(i - 1, n)
        
        # Contamos iteraciones del bucle interno (donde ocurre la magia)
        METRICAS["calls"] += (inicio) 
        
        for j in range(inicio, 0, -1):
            # Operación básica: Suma (fila[j] + fila[j-1])
            METRICAS["ops"] += 1
            fila[j] = fila[j] + fila[j - 1]
            
    return fila[n]

def encontrar_contacto_dp(P):
    return encontrar_contacto_generico(P, C_dp)