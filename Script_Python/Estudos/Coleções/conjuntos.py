"""
Conjuntos

— Conjuntos em qualquer linguagem de programação, fazemos referência á Teoria dos Conjuntos
da Matemática.

— Aqui no Python, os conjuntos são chamados Sets.

Dito isto, da mesma forma que na matemática:

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos,
mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar
com chaves, valores e itens duplicados

Os conjuntos (sets) são referenciados em Pytho com chaves {}

Diferença entre conjuntos (Set) e Mapas (Dicionários) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;


# Definindo um conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})  # Repare que valores repetidos
print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor ja existente, o mesmo
# será ignorado sem gerar nenhum tipo de erro e não fará parte do conjunto

# Forma 2 - Mais comum

s = set({1, 2, 3, 4, 5, 5})
print(s)
print(type(s))

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')


# Importante lembrar que, além de não termos valores duplicados, não temos ordem

dados = 99, 2, 34, 2, 23, 12, 1, 44, 5, 34

# Lista aceitam valores duplicados logo temos 10 elementos
lista = list(dados)
print(f'Lista: {lista} com {len(lista)} elementos')

# Lista aceitam valores duplicados logo temos 10 elementos
tupla = tuple(dados)
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# Dicionários não aceitam chaves duplicadas, então temos 8 elementos
dicionario = {}.fromkeys(dados, 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')

# Conjuntos não aceitam valores duplicados, então temos 8 elementos
conjunto = set(dados)
print(f'Conjuntos: {conjunto} com {len(conjunto)} elementos')

# Assim como todo outra coleção em Python podemos colocar todos os tipos de dados misturados em Sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente
for valor in s:
    print(valor)


"""
# Usos interessantes com sets

# Imagine que fizemos um formulário de cadastro de visitantes numa feira ou museu e os visitantes
# informam manualmentea cidade de onde vieram.

# Adicionamo-nos cada cidade numa lista Python, ja que numa lista podemos adicionar novos elementos e ter repetição

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'São Paulo', 'Campo Grande', 'Cuiaba']
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos.
# Podemos utilizar o set para isso:

print(len(set(cidades)))

# Adicionando elementos em um conjunto