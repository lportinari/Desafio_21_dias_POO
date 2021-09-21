from pessoa import Pessoa

# Utilizando herança
class Juridica(Pessoa):
    def __init__(self, cnpj, nome_fantasia):
        self.cnpj = cnpj
        self.nome_fantasia = nome_fantasia

# Exercício: Herdar de pessoa 