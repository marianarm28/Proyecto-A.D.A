# proyecto/comun.py

# Diccionario global para contadores

###Este diccionario registra:
# cuántas operaciones básicas hace cada algoritmo
# cuántas llamadas o iteraciones internas ejecuta

METRICAS = {
    "ops": 0,    # Operaciones básicas (sumas, mult, comparaciones clave)
    "calls": 0,  # Llamadas recursivas o iteraciones del bucle principal
    "max_depth": 0 # (Opcional) Profundidad máxima de recursión
}

def reiniciar_metricas():
    ##Antes de cada repetición del experimento ponemos:
    METRICAS["ops"] = 0
    METRICAS["calls"] = 0
    METRICAS["max_depth"] = 0
    #Esto asegura que cada ejecución comienza desde 0 operaciones y 0 llamadas.

def encontrar_contacto_generico(P, funcion_calculo_combinatorio):
    """
    Motor de búsqueda estandarizado.
    """
    if P <= 0: return None

    m = 2
    while True:
        # PODA LOGICA:
        # Calcular C(m, 2) cuenta como una ejecución del algoritmo,
        # pero para no ensuciar las métricas del "intento exitoso",
        # a veces se excluye. Sin embargo, para ser rigurosos, 
        # deberíamos contar TODO el esfuerzo computacional.
        
        # Nota: Aquí llamamos a la función, ella internamente actualizará METRICAS
        val_minimo = funcion_calculo_combinatorio(m, 2)
        
        if val_minimo > P:
            return None 

        for n in range(2, m + 1):
            valor = funcion_calculo_combinatorio(m, n)

            if valor == P:
                return (m, n)
            
            if valor > P:
                break
        
        m += 1