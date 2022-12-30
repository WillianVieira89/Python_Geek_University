"""
Estruturas de repetição

Loop for

Loop ->  Estrutura de repetição
For ->  Uma dessas estruturas

Python

for item in iterável:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 3, 5, 7, 9]

- Range
    numeros = range(1, 10)

Apertar o CTRL + Print abre a pagina de ajuda

Tabela de Emojis
https://apps.timwhitlock.info/emoji/tables/unicode

"""

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # temos que transformar em uma lista

# Exemplo de for 1 (iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo 2 de for (iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo 3 de for (iterando sobre um range)
"""
(valor_inicial, valor_final)
OBS: O valor final não é inclusive (1, 10) valor irá do 1 até 9
1
2
3
4
5
6
7
8
9
10 - Não incluído
"""
for numero in range(1, 10):
    print(numero)
"""
Enumerate
((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' '), (5, 'U')...)
"""
for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):  # Quando não precisamos de um valor, podemos descartá-lo utilizando um underline (_)
    print(letra)

for valor in enumerate(nome):
    print(valor)

for valor in enumerate(nome):
    print(valor[0])

for valor in enumerate(nome):
    print(valor[1])

qtd = int(input('Quantas vezes esse loop deve rodar? '))

for n in range(1, qtd+1):
    print(f'Imprimindo {n}')

qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

nome = 'Geek University'
for letra in nome:  # imprimi toda a palavra em uma linha, não pulando para a linha debaixo
    print(letra, end='')

# Original: U+1F60D
# Modificado: U0001F605

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F605' * num)
