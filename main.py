from cliente import *
from worker import *
import random
import Queue

fila_tarefas = Queue.Queue()
fila_resultados = Queue.Queue()

NUMERO_DE_LINHAS = 5
NUMERO_DE_COLUNAS = 5
NUMERO_DE_WORKERS = 3


def print_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print ('{} '.format(matriz[i][j])),
        print('\n')


def gera_matriz_mock():
    return [[random.randint(1,9) for x in range(NUMERO_DE_LINHAS)] for y in range(NUMERO_DE_COLUNAS)]


def main():
    matrizA = gera_matriz_mock()
    matrizB = gera_matriz_mock()

    print('##### MATRIZ A #####\n')
    print_matriz(matrizA)
    print('\n##### MATRIZ B #####\n')
    print_matriz(matrizB)

    cliente = Cliente(matrizA, matrizB, fila_resultados)

    cliente.separar_tasks_enfileirar(fila_tarefas)
    cliente.start()

    for i in range(NUMERO_DE_WORKERS):
        t = Worker(i, fila_tarefas, fila_resultados)
        t.start()

    cliente.join()
    print_matriz(cliente.final_matrix)

main()
