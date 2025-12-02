import csv
import math
from collections import defaultdict

ARCHIVO_ENTRADA = "resultados_experimento.csv"
ARCHIVO_SALIDA  = "estadisticas_completas.csv"

def cargar_datos():
    datos = defaultdict(list)
    
    try:
        with open(ARCHIVO_ENTRADA, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                alg = row["Algoritmo"]
                P = int(row["Valor_P"])
                
                # Convertimos a float/int, manejando errores (-1)
                t = float(row["Tiempo_Segundos"])
                ops = float(row["Ops_Basicas"])
                calls = float(row["Llamadas_Iteraciones"])
                
                if t >= 0: # Solo si fue una ejecución exitosa
                    clave = (alg, P)
                    datos[clave].append((t, ops, calls))
    except FileNotFoundError:
        print(f"❌ Error: No se encuentra {ARCHIVO_ENTRADA}. Ejecuta experimento.py primero.")
        return {}
        
    return datos

def calcular_stats(lista_tuplas):
    # lista_tuplas = [(t1, ops1, calls1), (t2, ops2, calls2), ...]
    n = len(lista_tuplas)
    if n == 0: return (0,0,0,0,0,0)

    # Desempaquetar
    tiempos = [x[0] for x in lista_tuplas]
    ops     = [x[1] for x in lista_tuplas]
    calls   = [x[2] for x in lista_tuplas]

    # Promedios
    prom_t = sum(tiempos) / n
    prom_ops = sum(ops) / n
    prom_calls = sum(calls) / n

    # Desviación Estándar (Population)
    dev_t = math.sqrt(sum((x - prom_t)**2 for x in tiempos) / n)
    dev_ops = math.sqrt(sum((x - prom_ops)**2 for x in ops) / n)
    # dev_calls suele ser 0 porque el algoritmo es determinista, pero la calculamos igual
    dev_calls = math.sqrt(sum((x - prom_calls)**2 for x in calls) / n)

    return prom_t, dev_t, prom_ops, dev_ops, prom_calls, dev_calls

def generar_reporte():
    datos = cargar_datos()
    if not datos: return

    print(f"\nGenerando estadísticas extendidas en '{ARCHIVO_SALIDA}'...")
    
    with open(ARCHIVO_SALIDA, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Encabezados potentes
        headers = [
            "Algoritmo", "P", "Muestras",
            "Tiempo_Prom(s)", "Tiempo_Dev",
            "Ops_Prom", "Ops_Dev",
            "Calls_Prom", "Calls_Dev"
        ]
        writer.writerow(headers)
        
        # Imprimir tabla bonita en consola
        print("-" * 100)
        print(f"{'Algoritmo':<15} {'P':<8} {'T_Prom(s)':<12} {'Ops_Prom':<15} {'Calls_Prom':<15}")
        print("-" * 100)

        for (alg, P) in sorted(datos.keys(), key=lambda x: (x[1], x[0])):
            stats = calcular_stats(datos[(alg, P)])
            # stats = (prom_t, dev_t, prom_ops, dev_ops, prom_calls, dev_calls)
            
            # Escribir CSV
            row = [alg, P, len(datos[(alg, P)])] + list(stats)
            writer.writerow(row)
            
            # Imprimir Consola (Resumido)
            print(f"{alg:<15} {P:<8} {stats[0]:<12.6f} {int(stats[2]):<15} {int(stats[4]):<15}")

    print("-" * 100)
    print("✅ Reporte Estadístico Completo Generado.")

if __name__ == "__main__":
    generar_reporte()