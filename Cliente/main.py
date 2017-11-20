from cliente import *
import xmlrpclib
import random

from datetime import datetime

# fila_tarefas = Queue.Queue()
# fila_resultados = Queue.Queue()
# bag_of_tasks = Bag(fila_tarefas, fila_resultados)

bag_server = xmlrpclib.ServerProxy('http://localhost:8000',allow_none=True)
bag_server.init_bag()
NUMERO_DE_LINHAS = 10
NUMERO_DE_COLUNAS = 10



def print_matriz(matriz,output):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            output.write('{} '.format(matriz[i][j])),
        output.write('\n')


def gera_matriz_mock():
    return [[random.randint(1,9) for x in range(NUMERO_DE_LINHAS)] for y in range(NUMERO_DE_COLUNAS)]


def main():
    log = open('exec_log.txt','w')
    matrizA = gera_matriz_mock()
    matrizB = gera_matriz_mock()

    log.write('##### MATRIZ A #####\n')
    print_matriz(matrizA,log)
    log.write('\n##### MATRIZ B #####\n')
    print_matriz(matrizB,log)

    cliente = Cliente(matrizA, matrizB, bag_server)

    cliente.separar_tasks_enfileirar()
    cliente.start()

#    for i in range(NUMERO_DE_WORKERS):
#        t = Worker(i, bag_of_tasks)
#        t.start()

    cliente.join()
    log.write('\n#### MATRIZ FINAL ####\n')
    print_matriz(cliente.final_matrix,log)

start_time = datetime.now()
main()
print 'tempo de execucao: {}'.format(datetime.now() - start_time)
