# DIA 04: Construa uma classe pessoa
class Pessoa:
    def __init__(self, nome, endereco, rg, cpf):
        self.nome = nome
        self.endereco = endereco  
        self.rg = rg  
        self.cpf = cpf  

    # Representação do objeto
    def __rep__(self):
        return f'Pessoa: {self.nome}'

    def listar(self):
        return self.nome, self.endereco, self.rg, self.cpf  

    def herança(self):
        return "Testando a herança..."      
