from threading import Thread


class Worker(Thread):
    def __init__(self, num, filaOrigem, filaDestino):
        Thread.__init__(self)
        self.num = num
        self.filaOrigem = filaOrigem
        self.filaDestino = filaDestino

    def doJob(self):
        job = self.filaOrigem.get()
        print('woker {} calculando produto'.format(self.num))
        job.calcula_produto()
        self.filaDestino.put(job)

    def run(self):
        while not self.filaOrigem.empty():
            self.doJob()
