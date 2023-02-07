"""
**kwargs

Poderiamos chamar esse parâmetro de **xis, mas por convenção chamamos de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras
em uma tupla, o **kwargs exige que utilizemos parâmetros nomeados, e transforma esses
parâmetros extras em um dicionário

# Exemplo

def cores_favoritas(**kwargs):
    print(kwargs)

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

def cores_favoritas(**kwargs):
    for pessoas, cor in kwargs.items():
        print(f'A cor favorita de {pessoas.title()} é {cor}')

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# OBS: Os parâmetros *args e **kwargs não são obrigatórias

# Exemplo mais complexo

def cumprimemto_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek"
    return 'Não tenho certeza quem você é'

print(cumprimemto_especial())
print(cumprimemto_especial(geek='Python'))
print(cumprimemto_especial(geek='Oi'))
print(cumprimemto_especial(geek='Especial'))

# Nas nossas funções podemos ter (NESTA ORDEM):
# - parâmetros obrigatórios
# - *args
# - Parâmetros default (não obrigatórios)
# - **kwargs

def minha_função(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)

minha_função(33, 'Willian')
minha_função(18, 'Felicity', 4, 3, 5, solteiro=True)
minha_função(34, 'Felipe', eu='Não', voce='Vai')
minha_função(19, 'Carla', 9, 4, 3, java=False, python=True)

# Entenda porquê é importante manter a ordem dos parâmetros na declaração

# Função declarada com os parâmetros na ordem correta

def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]

print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))
----------------------------------------------------------------------------------------
# Função declarada com a ordem incorreta
def mostra_info(a, b, instrutor='Geek', *args,  **kwargs):
    return [a, b, args, instrutor, kwargs]

print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))
---------------------------------------------------------------------------------------
# Desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']}{kwargs['sobrenome']}"


nomes = {'nome': 'Felicity ', 'sobrenome': 'Jones'}
print(mostra_nomes(**nomes))
"""

def soma_multiplos_numeros(a, b, c):
    print(a + b + c)

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
dicionario = dict(a=1, b=2, c=3)  # OBS os nomes das chaves em um dicionário devem ser mesmos dos parametros da função
dicionario2 = dict(d=1, e=2, f=3)

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)
soma_multiplos_numeros(**dicionario)
soma_multiplos_numeros(**dicionario2)  # Retorna um TypeError


7'/'