from threading import Thread
import pickle


class Bag(Thread):
    def __init__(self, fila_tarefas, fila_resultados):
        self.fila_tarefas = fila_tarefas
        self.fila_resultados = fila_resultados

    def insert_task(self, job):
        print('entrou no insert_task')
        p = pickle.loads(job)
        print('tipo do job -> {}'.format(type(job)))
        self.fila_tarefas.put(p)
        return True

    def insert_result(self, job):
        print('entrou no insert_result')
        self.fila_resultados.put(job)
        return True

    def get_tarefa(self):
        print('entrou no get_tarefa')
        return self.fila_tarefas.get()

    def get_resultado(self):
        print('entrou no get_resultado')
        return pickle.dumps(self.fila_resultados.get())

    def calcula_resultado(self):
        print('entrou no calcula_resultado')
        job = self.fila_tarefas.get()
        print('Bag calculando produto')
        job.calcula_produto()
        self.fila_resultados.put(job)

    def is_fila_tarefas_empty(self):
        print('entrou no is_fila_tarefas_empty')
        return self.fila_tarefas.empty()

    def is_fila_resultados_empty(self):
        print('entrou no is_fila_resultados_empty')
        return self.fila_resultados_empty()

    def run(self):
        print('entrou no run')
        while not self.fila_tarefas.empty():
            self.calcula_resultado()
