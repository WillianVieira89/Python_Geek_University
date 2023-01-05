"""
Listas (list)

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem
DINÂMICO e também de podermos colocar QUALQUER tipo de dados.

Linguagens C/Java: Arrays
    — Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array
    será SEMPRE  do tipo inteiro e poderá ter SEMPRE  no máximo 5 valores.

Já em Python:

- Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: As listas não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de dados;
- As listas em Python são representadas por colchetes: []
- As listas são mutáveis: Ou seja, podem mudar constantemente

type([])  # Definição de uma lista

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k' ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University')

#  Podemos facilmente checar se determinado valor está contido na lista
num = 2
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o numero {num}')

#  Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

#  Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em listas

Para adicionar elementos em listas, utilizamos a função append

OBS: com o append, nós so conseguimos adicionar 1 elemento por vez

append e extend ->> sempre o valor é adicionado ao final da fila na lista

lista1.append(43)
print(lista1)

# lista1.append(43,44,45) <<->> irá retornar um erro
lista1.append([8, 3, 11])
print(lista1)

if [8, 3, 11] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67])  # adiciona vários elementos a lista de uma vez diretamente, desde que dentro de uma lista
print(lista1)

lista1.extend('Geek')  # adiciona string separando ela na lista letra a letra
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice
# OBS: Isso não substitui o valor inicial. O mesmo será deslocado para a direita da lista
lista1.insert(2, 'Novo Valor')
print(lista1)

# Podemos facilmente juntar duas listas
# Forma 1
lista6 = lista1 + lista2
print(lista6)

# Forma 2
lista1.extend(lista2)
print(lista1)

# Podemos facilmente inverter uma lista
# Forma 1
lista1.reverse()
print(lista1)

# Forma 2
print(lista1[::-1])  # slice de lista

# Copiar uma lista
lista6 = lista2.copy()
print(lista6)

# Podemos contar a quantidade de elementos de uma lista
print(len(lista1))

# Podemos remover facilmente o último elemento de uma lista
# OBS: O pop não somente remove o último elemento mas também o retorna
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo índice
# OBS: Os elementos á direita deste índice serão deslocados para a esquerda
# OBS: Se não houver elemento no índice informado, teremos o erro IndexError.
lista5.pop(2)
print(lista5)

# Podemos remover todos os itens da lista (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
nova = nova * 3
print(nova)

# Podemos facilmente converter uma string para uma lista

# Exemplo 1
curso = 'Programação em Python: Essencial'
curso = curso.split()  # OBS: Por padrão o split separa os elementos da lista pelo espaço entre elas
print(curso)

# Exemplo 2
curso = 'Programação,em,Python:,Essencial'
curso = curso.split(',')  # OBS: split com indicação do separador
print(curso)

# Convertendo uma lista em uma string
lista7 = ['Programação', 'em', 'Python:', 'Essencial']
# Abaixo estamos falando: Pega a lista7, coloca espaço entre cada elemento e transforma em um string
curso = ' '.join(lista7)
print(curso)

# Abaixo estamos falando: Pega a lista7, coloca um cifrão($) entre cada elemento e transforma em um string
curso = '$'.join(lista7)
print(curso)
# Iterando sobre listas usando for

# Exemplo 1 -->> printa cada elemento da lista
for elemento in lista4:
    print(elemento)

# Exemplo 2 -->> soma os elementos da lista desde que sejam valores inteiros ou float
soma = 0
for elemento in lista4:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 3 -->> soma os elementos desde sejam string
soma = ' '
for elemento in lista2:
    print(elemento)
    soma = soma + elemento
print(soma)

# Iterando sobre listas usando while
carrinho = []
produto = ' '

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazer acesso aos elementos de forma indexada
#           0         1        2        3
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])  # verde
print(cores[1])  # amarelo
print(cores[2])  # azul
print(cores[3])  # branco

# Fazer acesso aos elementos de forma indexada inversa
# Para entender melhor o índice negativo, pense na lista como um círculo, onde
# o final do elemento está ligado ao início da lista
#           0         1        2        3
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[-1])  # branco
print(cores[-2])  # azul
print(cores[-3])  # amarelo
print(cores[-4])  # verde
# print(cores[-5])  # Erro, pois não existe índice -5

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

# Listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)

numeros = [5, 6, 7, 5, 8, 9, 10]

# Em qual índice está o valor 6?
print(numeros.index(6))

# Em qual índice está o valor 9?
print(numeros.index(9))

# print(numeros.index(19)) # Gera ValueError
# OBS: Caso não tenha este elemento na lista, será apresentado erro ValueError
# OBS: Caso tenha mais de um elemento com mesmo valor, retorna o índice do primeiro elemento encontrado
print(numeros.index(5))


# Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar
print(numeros.index(5, 1))  # buscando a partir do indice 1
print(numeros.index(5, 2))  # buscando a partir do indice 2
print(numeros.index(5, 3))  # buscando a partir do indice 3
print(numeros.index(5, 4))  # buscando a partir do indice 4
# OBS: Caso não tenha este elemento na lista, será apresentado erro ValueError

# Podemos fazer busca dentro de um range, inicio/fim
print(numeros.index(8, 3, 6))  # Buscar o indice do valor 8, entre os indices 3 a 6

# Outros métodos não tão importantes mas também são úteis
# Encontrar o índice de um elemento na lista


# Revisão de slicing

#lista[inicio:fim:passo]
# range(inicio:fim:passo)

# Trabalhando com o slice de lista com o parametro 'inicio'

lista = [1, 2, 3, 4]
print(lista[1:])  # Iniciando no indice 1 e pegando todos os elementos restantes

# Trabalhando com o slice de lista com o parametro 'fim'
print(lista[:2])  # começa em 0, pega até o indice 2 – 1.
print(lista[:4])  # começa em 0, pega até o indice 4 – 1.
print(lista[1:3])  # começa em 1, pega até o indice 3 – 1.

# Trabalhando com slice de lista com o parâmetro 'passo'
print(lista[1::2])  # começa em 1, vai até o final, de 2 em 2
print(lista[::2])  # começa em 0, vai até o final de 2 em 2

# Invertendo valores em uma lista

nomes = ['Geek', 'University']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

nomes = ['Geek', 'University']
nomes.reverse()
print(nomes)

# Soma*, Valor maximo*, Valor minimo*, Tamanho
# * Se os valores forem todos inteiros e reais

lista = [1, 2, 3, 4, 5, 6]
print(sum(lista))  # soma todos os itens da lista
print(max(lista))  # pega o maior valor da lista
print(min(lista))  # pega o menor valor da lista
print(len(lista))  # faz a leitura do tamanho da lista

# Transformar uma lista em tupla
lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotamento de listas

lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# OBS: Se tivermos um número diferente de elementos na lista ou variaveis para receber os dados, teremos um Value Error

# Copiando uma lista para outra (Shallow Copy ou Deep Copy)

# Forma 1 Deep Copy

lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista, mas elas
# ficaram totalmente independentes, ou seja, modificando uma lista, não a outra. Isso em Python
# é chamado de Deep Copy (cópia profunda)
"""

# Forma 2 Shallow Copy

lista = [1, 2, 3]
print(lista)

nova = lista  # cópia

print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que ao utilizarmos via atribuição e copiamos os dados da lista para a nova lista, mas
# após realizar modificação numa lista, está modificação refletiu-se em ambas as listas.
# Isso em Python é chamado Shallow Copy.