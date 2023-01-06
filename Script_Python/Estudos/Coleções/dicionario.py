"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários, Python são
conhecidos por mapas.

Dicionários são coleções do tipo chave/valor.
Dicionários são representados por {}.

print(type({}))

OBS: Sobre dicionários
    — Chave e Valor são separados por dois pontos 'chave: valor';
    — Tanto chave quanto valor podem ser de qualquer tipo de dado;
    — Podemos misturar tipo de dados


# Criação de dicionários

# Forma 1 (Mais comum)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguay'}

print(paises)
print(type(paises))

# Forma 2 (Menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')
print(paises)
print(type(paises))

# Acessando elementos

# Forma 1 - Acessando via chaves, da mesma forma que lista/tupla
print(paises['br'])
#  print(paises['ru'])

# OBS: Caso tentarmos fazer um acesso utilizando uma chave que não existe, teremos um KeyError

# Forma 2 - Acessando via get -  Recomendada

print(paises.get('br'))
print(paises.get('ru'))

# Caso o get não encontre o objeto com a chave informada será retronado o Valor None e não será gerado KeyError

pais = paises.get('ru')

if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')

# Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada
pais = paises.get('ru', 'Não encontrado')
print(f'Encontrei o país {pais}')

# Podemos verificar se determinada chave se sencontra em um dicionário
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']


# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla dicionário, como chaves
# de dicionários

# Tuplas, por exemplo são bastante interesantes de serem utilizadas como chave de dicionários
# Pois, as mesmas são imutáveis

localidades = {
    (35.6755, 39.6917): 'Escritorio em Tokyo',
    (40.6889, 39.6217): 'Escritorio em Nova York',
    (37.6877, 39.6457): 'Escritorio em São Paulo'
}

print(localidades)
print(type(localidades))

"""
