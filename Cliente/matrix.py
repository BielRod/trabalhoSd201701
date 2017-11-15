class Matrix():
    def __init__(self, matriz):
        # @todo escrever validacao pra ver se u numero de colunas eh
        # igual pra todas as linhas
        self.matriz = matriz
        self.qtd_linhas = len(matriz)
        self.qtd_colunas = len(matriz[0])

    # Retorna uma lista com os
    # elementos da linha cujo indice eh passado por parametro
    def getRow(self, index):
        elementos = []
        for i in range(len(self.matriz[index])):
            elementos.append(self.matriz[index][i])

        return elementos

    # Retorna uma lista com os
    # elementos da coluna cujo indice eh passado por parametro
    def getColumn(self, index):
        elementos = []
        for i in range(len(self.matriz[index])):
            elementos.append(self.matriz[i][index])

        return elementos
