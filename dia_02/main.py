# DIA 03: Construa uma classe receita com 4 atributos, peso, tamanho, preco, nome

class Receita:
    def __init__(self, nome, tamanho, peso, preco):
        self.nome = nome
        self.__tamanho = tamanho
        self.__peso = peso
        self.preco = preco

    def __str__(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def setTamanho(self, tamanho):
        self.tamanho = tamanho

    def setPeso(self, peso):
        self.__peso = peso

    def setPreco(self, preco):
        self.__preco = preco

    def getNome(self):
        return self.nome

    def getTamanho(self):
        return self.tamanho

    def getPeso(self):
        return self.__peso

    def getPreco(self):
        return self.__preco

    def salvar(self):
        pass

    def mostrar(self):
        receita = f"""Retorno...
        Nome = {self.nome}
        Tamanho = {self.__tamanho}
        peso = {self.__peso}
        Preco = {self.preco}
        """
        return receita


chocolate = Receita('Chocolate', 'p', 1.5, 45.50)
print(chocolate.mostrar())
            