"""
Entendendo o *args

- O *args é um parâmetro, como outro qualquer. Isso significa que você poderá
chamar de qualquer coisa, desde que comece com asterisco

Exemplo

*xis

Mas por convenção, utilizamos *args para defini-lo

Mas o que é o *args

O parâmetro *args utilizado numa função, coloca os valores extras informados como entrada
em uma tupla. Então desde já se lembre que tuplas são imutáveis

# Exemplo

def soma(num1=1, num2=2, num3=3, num4=4):
    return num1 + num2 + num3 + num4

print(soma(4, 6, 9))
print(soma(4, 6))
print(soma(4, 6, 9, 5))

# Exemplo

# Entendendo *args

def soma_todos_valores(nome, email, *args):
    return sum(args)

print(soma_todos_valores('Willian', 'teste@teste.com.br', 1, 2, 3))
print(soma_todos_valores('Willian', 'teste@teste.com.br'))
print(soma_todos_valores('Willian', 'teste@teste.com.br', 1))
print(soma_todos_valores('Willian', 'teste@teste.com.br', 2, 3))
print(soma_todos_valores('Willian', 'teste@teste.com.br', 2, 3, 4))
print(soma_todos_valores('Willian', 'teste@teste.com.br', 3, 4, 5, 6))
print(soma_todos_valores('Willian', 'teste@teste.com.br', 12.4, 22.6))

# Outro exemplo de utilização do *args

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem vindo Geek!!'
    return 'Eu não tenho certeza quem você é ...'

print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1 , 'University', 3.145))

"""


def soma_todos_valores(*args):
    return sum(args)

# Desempacotador
numeros = [1, 2, 3, 4, 5, 6, 7]
print(soma_todos_valores(*numeros))

# OBS: O asterisco serve para que informenos ao Python que estamos
# a passar como argumento uma coleção de dados. Desta forma, ele saberá
# que precisará antes desempacotar estes dados.
