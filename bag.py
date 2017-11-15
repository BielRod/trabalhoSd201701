from threading import Thread


class Bag(Thread):
    def __init__(self, fila_tarefas, fila_resultados):
        self.fila_tarefas = fila_tarefas
        self.fila_resultados = fila_resultados

    def insert_task(self, job):
        self.fila_tarefas.put(job)

    def insert_result(self, job):
        self.fila_resultados.put(job)

    def get_tarefa(self):
        return self.fila_tarefas.get()

    def get_resultado(self):
        return self.fila_resultados.get()

    def calcula_resultado(self):
        job = self.fila_tarefas.get()
        print('Bag calculando produto')
        job.calcula_produto()
        self.fila_resultados.put(job)

    def is_fila_tarefas_empty(self):
        return self.fila_tarefas.empty()

    def is_fila_resultados_empty(self):
        return self.fila_resultados_empty()

    def run(self):
        while not self.fila_tarefas.empty():
            self.calcula_resultado()
