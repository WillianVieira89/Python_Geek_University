"""
Tipo Float

Tipo real, decimal

Casas decimais

OBS: O separador de casas decimais em Python é o ponto não a vírgula.
"""

# Errado do ponto de vista do Float, mas gera uma tupla
valor = 1, 44
print(valor)
print(type(valor))

# Certo do ponto de vista float
valor = 1.44
print(valor)
print(type(valor))

# É possível fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um float para um int

"""
OBS: Ao converter valores float para inteiros nós perdemos precisão
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos
variavel = 5j  #atribuição de numeros complexos
print(variavel)
print(type(variavel))

