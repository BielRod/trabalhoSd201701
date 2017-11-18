from threading import Thread


class Worker(Thread):
    def __init__(self, num, bag):
        Thread.__init__(self)
        self.num = num
        self.bag = bag

    def doJob(self):
        try:
            job = self.bag.get_tarefa()
            # print('woker {} calculando produto'.format(self.num))
            job.calcula_produto()
            self.bag.insert_result(job)
        except:
            bag.insert_task(job)

    def run(self):
        while not self.bag.is_fila_tarefas_empty():
            self.doJob()
