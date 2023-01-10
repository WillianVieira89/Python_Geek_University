"""
Módulo Collections — Ordered Dict

# Num dicionário a ordem de inserção dos elementos não é garantida
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'chaves={chave}: valor={valor}')

Ordered Dict -> è um dicionário que nos garante a ordem de inserção dos elementos

from collections import OrderedDict
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'chaves={chave}: valor={valor}')
"""

# Entendendo a diferença entre Dict e Ordered Dict

from collections import OrderedDict

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)  # Retorna True já que a ordem dos elementos não importa para o dicionário

# Ordered Dict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})
print(odict1 == odict2)  # # Retorna False já que a ordem dos elementos importa para o OrderedDict
