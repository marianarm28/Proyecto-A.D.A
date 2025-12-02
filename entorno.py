import platform
import sys
import os
import subprocess
import datetime

def obtener_info_cpu_windows():
    """Intenta obtener el nombre exacto de la CPU en Windows"""
    try:
        command = "wmic cpu get name"
        output = subprocess.check_output(command, shell=True).decode().strip()
        # La salida suele ser "Name\nIntel(R) Core(TM)...", así que tomamos la segunda línea
        return output.split('\n')[1].strip()
    except:
        return platform.processor()

def obtener_ram_windows():
    """Intenta obtener la RAM total en GB"""
    try:
        command = "wmic computerSystem get totalPhysicalMemory"
        output = subprocess.check_output(command, shell=True).decode().strip()
        # Salida: "TotalPhysicalMemory\n17000000000..."
        bytes_ram = float(output.split('\n')[1].strip())
        gb_ram = bytes_ram / (1024**3)
        return f"{gb_ram:.2f} GB"
    except:
        return "No disponible (Requiere permisos)"

def generar_reporte_entorno():
    print("="*60)
    print("      REPORTE AUTOMÁTICO DE ENTORNO EXPERIMENTAL")
    print("="*60)
    print(f"Fecha de Ejecución: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 60)
    
    # 1. HARDWARE (CPU y RAM)
    cpu_info = obtener_info_cpu_windows() if platform.system() == "Windows" else platform.processor()
    ram_info = obtener_ram_windows()
    
    print(f"🔹 PROCESADOR (CPU):  {cpu_info}")
    print(f"🔹 MEMORIA RAM:       {ram_info}")
    print(f"🔹 ARQUITECTURA:      {platform.machine()} ({platform.architecture()[0]})")
    print("-" * 60)

    # 2. SOFTWARE (SO y Python)
    print(f"🔸 SISTEMA OPERATIVO: {platform.system()} {platform.release()} (Ver: {platform.version()})")
    print(f"🔸 VERSIÓN PYTHON:    {sys.version.split()[0]}")
    print(f"🔸 IMPLEMENTACIÓN:    {platform.python_implementation()}")
    print("-" * 60)

    # 3. REPRODUCIBILIDAD
    print("✅ GARANTÍA DE REPRODUCIBILIDAD:")
    print("   - Semilla Aleatoria: N/A (Algoritmos deterministas)")
    print("   - Aislamiento: Se recomienda cerrar procesos en segundo plano.")
    print("   - Timer: time.perf_counter() (Alta resolución, ignora clock updates)")
    print("="*60)

if __name__ == "__main__":
    generar_reporte_entorno()