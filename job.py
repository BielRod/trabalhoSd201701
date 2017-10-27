# Classe que representa a tarefa que será executada por cada worker.
class Job():
    def __init__(self, linha, coluna, idxLinha, idxColuna):
        if (len(linha) != len(coluna)):
            raise Exception('linha e coluna devem ter os mesmos tamanhos')

        self.linha = linha
        self.coluna = coluna
        self.idxLinha = idxLinha
        self.idxColuna = idxColuna
        self.soma = None

    def calcula_produto(self):
        soma = 0
        for i in range(len(self.linha)):
            soma += self.linha[i] * self.coluna[i]

        self.soma = soma
        return soma
