class Matrix():
    def __init__(self, matriz):
        # @todo escrever validação pra ver se u numero de colunas é
        # igual pra todas as linhas
        self.matriz = matriz

    # Retorna uma lista com os
    # elementos da linha cujo índice é passado por parâmetro
    def getRow(self, index):
        elementos = []
        for i in range(len(self.matriz[index])):
            elementos.append(self.matriz[index][i])

        return elementos

    # Retorna uma lista com os
    # elementos da coluna cujo índice é passado por parâmetro
    def getColumn(self, index):
        elementos = []
        for i in range(len(self.matriz[index])):
            elementos.append(self.matriz[i][index])

        return elementos
