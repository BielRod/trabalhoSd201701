from cliente import *
import xmlrpclib
import random

from datetime import datetime

# fila_tarefas = Queue.Queue()
# fila_resultados = Queue.Queue()
# bag_of_tasks = Bag(fila_tarefas, fila_resultados)

bag_server = xmlrpclib.ServerProxy('http://localhost:8000',allow_none=True)
NUMERO_DE_LINHAS = 3
NUMERO_DE_COLUNAS = 3



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

    cliente = Cliente(matrizA, matrizB, bag_server)

    cliente.separar_tasks_enfileirar()
    cliente.start()

#    for i in range(NUMERO_DE_WORKERS):
#        t = Worker(i, bag_of_tasks)
#        t.start()

    cliente.join()
    print_matriz(cliente.final_matrix)

start_time = datetime.now()
main()
print 'tempo de execucao: {}'.format(datetime.now() - start_time)
