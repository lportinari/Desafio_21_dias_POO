from pessoa import Pessoa
from juridica import Juridica


eu = Pessoa('Luciano', 'rua x, 111', '9.999.999-9', '000.000.000.00')
print(eu.listar())

empresario = Juridica('112.555.006/0001-50', 'google')
print(empresario.herança())