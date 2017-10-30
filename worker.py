from threading import Thread

class Worker(Thread):
    def __init__(self, num, filaOrigem, filaDestino):
        Thread.__init__(self)
        self.num = num
        self.fila = fila

    def doJob(self):
        job = filaOrigem.get()
        print('woker %d calculando produto'.format(self.num))
        job.calcula_produto()
        filaDestino.put(job)

    def run(self):
        while not filaOrigem.empty():
            doJob()