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
s = {1, 2, 3}

s.add(4)
s.add(4)  # Duplicidade não gera erro. Simplesmente é ignorado e não é adicionado
print(s)

# Remover elementos em um conjunto
s = {1, 2, 3}

# Forma 1
s.remove(3)  # Não é índice! Informamos o valor a ser removido
print(s)

# OBS: Caso o valor não seja encontrado será retornado um KeyError. Nenhum valor é retornado

# Forma 2

s.discard(2)
print(s)

# OBS: Caso o valor não seja encontrado nenhum erro será retornado

# Copiando um conjunto para outro ...

s = {1, 2, 3}
print(s)

# Forma 1 - Deep Copy
novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

# Forma 2 - Shallow Copy

novo = s

novo.add(4)
print(novo)
print(s)

s = {1, 2, 3}
print(s)

# Podemos remover todos os itens de um conjunto

s.clear()
print(s)

# Métodos Matemáticos de Conjuntos

# Imagine que temos dois conjuntos: Um contendo estudantes do curso de Python e um
# contendo estudantes do curso de Java.

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1 - Utilizando union

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2 - Utilizando o caractere pipe(|)

unicos2 = estudantes_python | estudantes_java
print(unicos2)

# Veja que alguns alunos que estudam Python também estudam Java

# Gerar um conjunto de estudantes que estão em ambos os cursos

# Forma 1 - Utilizando intersection

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando o &

ambos2 = estudantes_python & estudantes_java
print(ambos2)


# Gerar um conjunto de estudantes que não estão no outro curso

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)
"""

# Soma*, Valor Maximo*, Valor Minimo*, Tamanho
# * Se os valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
