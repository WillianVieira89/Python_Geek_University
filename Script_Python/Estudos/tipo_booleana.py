"""
Tipo Booleano

Àlgebra Booleana, criado por George Boole

2 constantes, Verdadeiro ou Falso

True => Verdadeiro
False => Falso

OBS: Sempre com a inicial em maiscula

Errado:

true, false

Certo:

True, False
"""

ativo = False
print(ativo)

"""
Operações Basícas
"""

# Negação (not):
"""
Fazendo a negação se o valor booleano for verdadeiro o resultado será falso, se for falso o resultado
será verdadeiro. Ou seja , o contrario
"""
print(not ativo)
logado = False

# Ou (or):
"""
È uma operação binária, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro

True or True => True
True or False => True
False or True => True
False or False => False
"""
print(ativo or logado)

# E (and):
"""
Também é uma operação binaria, ou seja, depende de dois valores. Ambos devem ser verdadeiros.

True and True => True
True and False => False
False and True => False
False and False => False
"""