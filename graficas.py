import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

ARCHIVO_ENTRADA = "resultados_experimento.csv"
CARPETA_SALIDA = "graficas"

def generar_graficas():
    # 1. Cargar datos
    if not os.path.exists(ARCHIVO_ENTRADA):
        print(f"❌ No existe {ARCHIVO_ENTRADA}")
        return

    df = pd.read_csv(ARCHIVO_ENTRADA)
    
    # Filtramos errores
    df = df[df['Tiempo_Segundos'] >= 0]
    
    # Creamos carpeta
    os.makedirs(CARPETA_SALIDA, exist_ok=True)
    
    # Configuración de estilo
    sns.set_theme(style="whitegrid")
    
    # ---------------------------------------------------------
    # GRÁFICA 1: TIEMPO vs P (Log Scale) - La clásica
    # ---------------------------------------------------------
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x='Valor_P', y='Tiempo_Segundos', hue='Algoritmo', marker="o", errorbar=None)
    plt.xscale('log')
    plt.yscale('log')
    plt.title('Complejidad Temporal: Tiempo vs P (Escala Log-Log)')
    plt.ylabel('Tiempo (segundos)')
    plt.xlabel('Valor P (Caminos)')
    plt.grid(True, which="both", ls="--", linewidth=0.5)
    plt.savefig(f"{CARPETA_SALIDA}/1_tiempo_log.png", dpi=300)
    plt.close()
    
    # ---------------------------------------------------------
    # GRÁFICA 2: OPERACIONES BÁSICAS vs P (La verdad matemática)
    # ---------------------------------------------------------
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x='Valor_P', y='Ops_Basicas', hue='Algoritmo', marker="s", errorbar=None)
    plt.xscale('log')
    plt.yscale('log')
    plt.title('Complejidad Abstracta: Operaciones Básicas vs P')
    plt.ylabel('Número de Operaciones (Log)')
    plt.xlabel('Valor P')
    plt.savefig(f"{CARPETA_SALIDA}/2_operaciones_log.png", dpi=300)
    plt.close()

    # ---------------------------------------------------------
    # GRÁFICA 3: HEATMAP DE TIEMPOS (Impacto Visual)
    # ---------------------------------------------------------
    # Preparamos datos para matriz: Filas=Algoritmo, Col=P, Valor=Tiempo Promedio
    pivot_table = df.pivot_table(values='Tiempo_Segundos', index='Algoritmo', columns='Valor_P', aggfunc='mean')
    
    plt.figure(figsize=(12, 6))
    # Usamos escala logarítmica en el color para que se noten las diferencias
    from matplotlib.colors import LogNorm
    sns.heatmap(pivot_table, annot=True, fmt=".2e", cmap="YlOrRd", norm=LogNorm(), cbar_kws={'label': 'Tiempo (s)'})
    plt.title('Mapa de Calor: Rendimiento por Instancia')
    plt.savefig(f"{CARPETA_SALIDA}/3_heatmap_tiempos.png", dpi=300)
    plt.close()

    # ---------------------------------------------------------
    # GRÁFICA 4: COMPARACIÓN DE BARRAS (Para un P mediano)
    # ---------------------------------------------------------
    # Elegimos un P que todos hayan completado (ej: 252)
    P_target = 252
    df_small = df[df['Valor_P'] == P_target]
    
    if not df_small.empty:
        plt.figure(figsize=(8, 6))
        sns.barplot(data=df_small, x='Algoritmo', y='Ops_Basicas', hue='Algoritmo', errorbar='sd')
        plt.yscale('log')
        plt.title(f'Costo Computacional (Ops) para P={P_target}')
        plt.ylabel('Operaciones (Log)')
        plt.savefig(f"{CARPETA_SALIDA}/4_barras_P{P_target}.png", dpi=300)
        plt.close()

    # ---------------------------------------------------------
    # GRÁFICA 5: MEMORIA CONSUMIDA vs P (Complejidad Espacial)
    # ---------------------------------------------------------
    plt.figure(figsize=(10, 6))
    # Filtramos recursivo puro en instancias grandes si es necesario para que no rompa la escala
    sns.lineplot(data=df, x='Valor_P', y='Memoria_Peak_Bytes', hue='Algoritmo', marker="^")
    
    plt.xscale('log')
    plt.yscale('log') # Escala Logarítmica también en memoria (Bytes vs KB vs MB)
    plt.title('Complejidad Espacial: Consumo de Memoria RAM')
    plt.ylabel('Memoria Pico (Bytes) - Log')
    plt.xlabel('Valor P')
    plt.savefig(f"{CARPETA_SALIDA}/5_memoria_log.png", dpi=300)
    plt.close()

    print(f"✅ Gráficas generadas exitosamente en /{CARPETA_SALIDA}")

if __name__ == "__main__":
    generar_graficas()