from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import Queue

from bag import *
from worker import *

NUMERO_DE_WORKERS = 2
server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=SimpleXMLRPCRequestHandler,
                            allow_none=True)
server.register_introspection_functions()

fila_tarefas = Queue.Queue()
fila_resultados = Queue.Queue()
bag_of_tasks = Bag(fila_tarefas, fila_resultados)

server.register_instance(bag_of_tasks)


def start_calculate():
    # metodo que o cliente chama quando ele acabou de colocar as tarefas
    for i in range(NUMERO_DE_WORKERS):
        t = Worker(i, bag_of_tasks)
        t.start()
    bag_of_tasks.start()


server.register_function(start_calculate)
server.serve_forever()
