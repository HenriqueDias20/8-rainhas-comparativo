import time
import psutil
import os

def medir_execucao(func):
    start = time.time()
    process = psutil.Process(os.getpid())
    mem_inicio = process.memory_info().rss
    resultado = func()
    mem_fim = process.memory_info().rss
    fim = time.time()
    return {
        "tempo": fim - start,
        "memoria_kb": (mem_fim - mem_inicio) / 1024,
        "resultado": resultado
    }
