"""
Loop while

Forma geral

while expressão booleana:
    //execução do loop

O bloco while será repetido enquanto o expressão for verdadeira.

Expressão booleana é toda expressão onde o resultado é verdadeiro ou falso

Exemplo:

num = 5
num < 5
"""

# Exemplo 1
numero = 1

while numero <= 5:
    print(numero)
    numero = numero + 1

# OBS: Em um loop while, é importante que cuidemos co critério de parada

# Exemplo 2

resposta = ' '

while resposta != 'sim':
    resposta = input('Já acabou Jessica? ')
