from job import *
from matrix import *
from threading import Thread
import pickle


class Cliente(Thread):
    def __init__(self, matriz_A, matriz_B, bag_server):
        Thread.__init__(self)
        self.matriz_A = Matrix(matriz_A)
        self.matriz_B = Matrix(matriz_B)
        self.bag = bag_server
        self.final_matrix = None

    def separar_tasks_enfileirar(self):
        for i in range(len(self.matriz_A.matriz)):
            for j in range(len(self.matriz_B.matriz[0])):
                task = Job(self.matriz_A.getRow(i), self.matriz_B.getColumn(j), i, j)
                # print('tipo da task: {}'.format(type(task)))
                self.bag.insert_task(pickle.dumps(task))
        self.bag.start_calculate()

    def montar_matriz_resultante(self):
        i = 0
        n_row = self.matriz_A.qtd_linhas
        n_col = self.matriz_B.qtd_colunas
        quantidade_de_elementos_matriz_resultante = n_row * n_col

        matriz_final = [[None for x in range(n_row)] for y in range(n_col)]

        while i < quantidade_de_elementos_matriz_resultante:
            resultado = pickle.loads(self.bag.get_resultado())
            matriz_final[resultado.idxLinha][resultado.idxColuna] = resultado.soma
            i = i + 1

        self.final_matrix = matriz_final

    def run(self):
        self.montar_matriz_resultante()
