import math

def generar_listas_validas():
    # Conjuntos para evitar repetidos
    pequenas = set()
    medianas = set()
    grandes = set()
    
    # Recorremos el triángulo de Pascal buscando valores
    # m va incrementando (profundidad)
    for m in range(2, 500): 
        # n va desde 2 hasta m (según la restricción del problema)
        for n in range(2, m + 1):
            
            # Calculamos P
            try:
                P = math.comb(m + n, m)
            except OverflowError:
                continue

            # CLASIFICACIÓN (Ajustada para que el Recursivo sobreviva las pequeñas)
            
            # Grupo 1: Pequeñas (Recursivo funciona bien)
            # Limite aprox: P < 1000
            if 6 <= P <= 1000:
                pequenas.add(P)
                
            # Grupo 2: Medianas (Recursivo empieza a sufrir/morir)
            # Limite aprox: 1,000 < P < 50,000
            elif 1001 <= P <= 50000:
                medianas.add(P)
                
            # Grupo 3: Grandes (Solo DP y Fórmula)
            # P > 50,000
            elif P > 50000 and P < 10**9: # Límite superior razonable
                grandes.add(P)

            # Si ya tenemos suficientes de todas, paramos para no tardar años
            if len(pequenas) > 30 and len(medianas) > 30 and len(grandes) > 30:
                break
        
        if len(pequenas) > 30 and len(medianas) > 30 and len(grandes) > 30:
            break

    # Convertimos a listas ordenadas y tomamos las primeras 25 (para tener margen sobre las 20)
    list_p = sorted(list(pequenas))[:25]
    list_m = sorted(list(medianas))[:25]
    list_g = sorted(list(grandes))[:25]

    print("--- COPIA Y PEGA ESTO EN TU ARCHIVO experimento.py ---\n")
    print(f"INSTANCIAS_PEQUENAS = {list_p}")
    print(f"\nINSTANCIAS_MEDIANAS = {list_m}")
    print(f"\nINSTANCIAS_GRANDES  = {list_g}")

if __name__ == "__main__":
    generar_listas_validas()