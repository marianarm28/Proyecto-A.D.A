import time
from contextlib import ContextDecorator

class Timer(ContextDecorator):
    """
    Temporizador de alta precisión para medir tiempos de ejecución.
    Puede usarse como Context Manager (with) o Decorador.
    """
    def __init__(self, name=None):
        self.name = name
        self.start_time = None
        self.end_time = None
        self.duration = None

    def start(self):
        self.start_time = time.perf_counter()

    def stop(self):
        self.end_time = time.perf_counter()
        self.duration = self.end_time - self.start_time

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()