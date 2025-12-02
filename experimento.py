import csv
import sys
import tracemalloc  # <--- IMPORTANTE: Librería para medir memoria
from proyecto.medicion import Timer
from proyecto.comun import reiniciar_metricas, METRICAS 
from proyecto.recursivo import encontrar_contacto_recursivo
from proyecto.memo import encontrar_contacto_memo
from proyecto.dp import encontrar_contacto_dp
from proyecto.fuerza_bruta import encontrar_contacto_fuerza_bruta

# CONFIGURACIÓN
K_REPETICIONES = 30
ARCHIVO_CSV = "resultados_experimento.csv"
sys.setrecursionlimit(20000)

INSTANCIAS_PEQUENAS = [6, 10, 20] 
INSTANCIAS_MEDIANAS = [70, 252, 924]
INSTANCIAS_GRANDES  = [12870, 184756]

def correr_experimento():
    # AGREGAMOS "Memoria_Peak_Bytes" AL ENCABEZADO
    encabezados = ["Algoritmo", "Valor_P", "Repeticion", "Tiempo_Segundos", "Ops_Basicas", "Llamadas_Iteraciones", "Memoria_Peak_Bytes", "Resultado"]
    
    with open(ARCHIVO_CSV, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(encabezados)

        print(f"Iniciando experimento CON MEMORIA Y MÉTRICAS (K={K_REPETICIONES})...")

        algoritmos_todos = [
            ("Recursivo", encontrar_contacto_recursivo),
            ("Memoizacion", encontrar_contacto_memo),
            ("Prog_Dinamica", encontrar_contacto_dp),
            ("Formula_Math", encontrar_contacto_fuerza_bruta)
        ]
        
        algoritmos_rapidos = [
            ("Memoizacion", encontrar_contacto_memo),
            ("Prog_Dinamica", encontrar_contacto_dp),
            ("Formula_Math", encontrar_contacto_fuerza_bruta)
        ]

        # EJECUCIÓN
        print("\n--- FASE 1: Instancias Pequeñas ---")
        ejecutar_lote(writer, algoritmos_todos, INSTANCIAS_PEQUENAS)

        print("\n--- FASE 2: Instancias Medianas ---")
        ejecutar_lote(writer, algoritmos_rapidos, INSTANCIAS_MEDIANAS)

        print("\n--- FASE 3: Instancias Grandes ---")
        ejecutar_lote(writer, algoritmos_rapidos, INSTANCIAS_GRANDES)
        
    print(f"\n✅ Experimento finalizado. CSV actualizado con Memoria.")

def ejecutar_lote(writer, lista_algoritmos, lista_instancias):
    for nombre_alg, funcion in lista_algoritmos:
        for P in lista_instancias:
            print(f"  -> {nombre_alg} | P={P} ...", end="", flush=True)
            
            mem_acum = 0
            
            for i in range(K_REPETICIONES):
                reiniciar_metricas()
                
                # INICIAR RASTREO DE MEMORIA
                tracemalloc.start()
                
                timer = Timer()
                try:
                    timer.start()
                    res = funcion(P)
                    timer.stop()
                    
                    # CAPTURAR MEMORIA (current, peak) -> Nos interesa el Peak
                    current, peak = tracemalloc.get_traced_memory()
                    
                    tiempo = timer.duration
                    resultado = str(res)
                    ops = METRICAS["ops"]
                    calls = METRICAS["calls"]
                    memoria = peak # Bytes máximos usados
                    
                except RecursionError:
                    timer.stop()
                    tiempo = -1; ops = -1; calls = -1; memoria = -1
                    resultado = "RecursionError"
                except Exception as e:
                    timer.stop()
                    tiempo = -1; ops = -1; calls = -1; memoria = -1
                    resultado = f"Error: {e}"
                finally:
                    # DETENER RASTREO PARA NO ACUMULAR BASURA
                    tracemalloc.stop()

                # Guardar en CSV con la nueva columna
                writer.writerow([nombre_alg, P, i+1, tiempo, ops, calls, memoria, resultado])
                
                if memoria > 0: mem_acum += memoria

            # Feedback visual
            prom_mem = mem_acum / K_REPETICIONES
            print(f" (Mem: {int(prom_mem)} B)")

if __name__ == "__main__":
    correr_experimento()