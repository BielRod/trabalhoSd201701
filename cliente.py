from . import Job
from . import Matrix


class Cliente():
    def __init__(self, matrizA, matrizB):
        self.matrizA = Matrix(matrizA)
        self.matrizB = Matrix(matrizB)

    def separar_tasks_enfileirar(self,fila):
        taskList = []
        for i in range(len(self.matrizA)):
            for j in range(len(self.matrizB[0])):
                task = Job(self.matrizA.getRow(i), self.matrizB.getColumn(j), i, j)
                fila.put(task)