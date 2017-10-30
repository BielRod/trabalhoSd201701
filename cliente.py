from . import Job
from . import Matrix
from threading import Thread


class Cliente(Thread):
    def __init__(self, matrizA, matrizB, filaDestino):
        Thread.__init__(self)
        self.matriz_A = Matrix(matriz_A)
        self.matriz_B = Matrix(matriz_B)
        self.fila_destino = filaDestino
        self.quantidade_de_elementos_matriz_resultante = # fazer o calculo para ver quantos elementos a resultante deve ter

    def separar_tasks_enfileirar(self,fila):
        taskList = []
        for i in range(len(self.matrizA.matriz)):
            for j in range(len(self.matrizB.matriz[0])):
                task = Job(self.matrizA.getRow(i), self.matrizB.getColumn(j), i, j)
                fila.put(task)

    def montar_matriz_resultante(self):
        i = 0
        numero_de_linhas = 
        
        while i < quantidade_de_elementos_matriz_resultante:
            resultado = self.filaDestino.get()

    def run(self):
        
