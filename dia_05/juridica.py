from pessoa import Pessoa

# Utilizando herança
class Juridica(Pessoa):
    def __init__(self, cnpj, nome_fantasia):
        self.cnpj = cnpj
        self.nome_fantasia = nome_fantasia

    def __rep__(self):
        return f'Nome fantasia: {self.nome_fantasia}'

    def listar(self):
        return f"cnpj: {self.cnpj}, Nome fantasia: {self.nome_fantasia}"

    def set_cnpj(self, value):
        self.cnpj = value

    def set_nome_fantasia(self, value):
        self.nome_fantasia = value