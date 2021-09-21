# DIA 03: Construa uma classe receita com 4 atributos, peso, tamanho, preco, nome

class Receita:
    def __init__(self, nome, tamanho, peso, preco):
        self.nome = nome
        self.tamanho = tamanho
        self.peso = peso
        self.preco = preco

    def __str__(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def setTamanho(self, tamanho):
        self.nome = tamanho

    def setPeso(self, peso):
        self.idade = peso

    def setPreco(self, preco):
        self.idade = preco

    def getNome(self):
        return self.nome

    def getTamanho(self):
        return self.tamanho

    def getPeso(self):
        return self.peso

    def getPreco(self):
        return self.preco

    def salvar(self):
        pass

    def mostrar(self):
        receita = f"""Retorno...
        Nome = {self.nome}
        Tamanho = {self.tamanho}
        peso = {self.peso}
        Preco = {self.preco}"
        """
        return receita


chocolate = Receita('Chocolate', 'p', 1.5, 45.50)
print(chocolate.mostrar())
            