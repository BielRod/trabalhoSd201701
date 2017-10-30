from . import Cliente
from . import Worker
import random
import Queue

fila_tarefas = Queue.Queue()
fila_resultados = Queue.Queue()

NUMERO_DE_LINHAS = 10
NUMERO_DE_COLUNAS = 10
NUMERO_DE_WORKERS = 10

def gera_matriz_mock():
    return [[random.random(1,20) for x in range(NUMERO_DE_LINHAS - 1)] for y in range(NUMERO_DE_COLUNAS - 1)]

def main():
    matrizA = gera_matriz_mock()
    matrizB = gera_matriz_mock()

    cliente = Cliente(matrizA, matrizB)

    cliente.separar_tasks_enfileirar(fila_tarefas)
    
    for i in range(NUMERO_DE_WORKERS - 1):
        t = Worker(i, fila_tarefas, fila_resultados)
        t.start()