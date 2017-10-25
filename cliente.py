from . import Job
from . import Matrix


class Cliente():
    def __init__(self, matrizA, matrizB):
        self.matrizA = Matrix(matrizA)
        self.matrizB = Matrix(matrizB)

    # implementar o método de separar tasks
    def separar_tasks(self):
        taskList = []
        for i in range(len(self.matrizA)):
            for j in range(len(self.matrizB[0])):
                task = Job(self.matrizA.getRow(i), self.matrizB.getColumn(j))
                taskList.append(task)
