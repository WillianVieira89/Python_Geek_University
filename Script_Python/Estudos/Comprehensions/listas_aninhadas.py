"""
Listas Aninhadas (Nested Lists)

- Algumas linguagens de programação (C/Java) possuem uma estrutura de dados chamadas arrays:
    - Unidimensionais (Arrays/Vetores);
    - Multidimensionais (Matrizes);

Em Python nós temos as listas
"""

# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # matriz 3x3
print(listas)
print(type(listas))

# Com fazemos para acessar os dados?
print(listas[0][1])  # acessa o número 2
print(listas[2][1])  # acessa o número 8

# iterando com ‘loops’ numa lista aninhada
for lista in listas:
    for num in lista:
        print(num)

# List Comprehension
[[print(valor) for valor in lista] for lista in listas]

# Outros Exemplos

# Gerando um tabuleiro/ matriz 3x3
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valores iniciais
print([['*' for i in range(1, 4)] for j in range(1, 4)])
