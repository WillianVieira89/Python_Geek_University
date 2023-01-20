"""
Funções com Parâmetro (de entrada)

— Funções que recebem dados para serem processados na mesma;

Se nós pensarmos num programa qualquer, geralmente temos:

entrada -> processamento -> saída

Se nós pensarmos numa função, ja sabemos que temos funções que:
— Não Possuem entrada;
— Não possuem saída;
— Possuem entrada, mas não possuem saída;
— Não possuem entrada, mas possuem saída;
— Possuem entrada e saída


# Refatorando uma função

def quadrado(numero):
    #  return numero * numero
    return numero ** 2

print(quadrado(7))
print(quadrado(5))
print(quadrado(3))

ret = quadrado(6)
print(ret)

print(quadrado())  # TypeError

# Refatorando a função
def cantar_parabens(aniversariante):
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o {aniversariante}!')

cantar_parabens('Willian')

# Funções podem ter n parâmetros de entrada. Ou seja, podemos receber como entrada
# em uma função quantos parâmetros forem necessários. Eles são separados por vírgula

# Exemplo

def soma(a, b): # no escopo da função se designa o parametro a e b no exemplo
    return a + b
def multiplica(num1, num2):
    return num1 * num2
def outra(num1, b, msg):
    return (num1 + b) * msg

print(soma(2, 5)) # no escopo do print se designa o argumento
print(multiplica(10, 20))
print(outra(5, 1, 'Python '))

# OBS:  Se a gente informar um número errado de parâmetro ou argumentos, teremos TypeError

def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'

print(nome_completo('Willian', 'Vieira'))

# A diferença entre parâmetros e argumentos

# Parâmetros são variaveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função;

# A ordem dos parâmetros importa!
nome = 'Felicity'
sobrenome = 'Jones'

print(nome_completo(sobrenome, nome))

# Argumentos nomeados ( Keyword Arguments)

# Caso utilizemos nomes dos parâmetros nos argumentos para informa-los, podemos
# utilizar qualquer ordem

print(nome_completo(nome='Willian', sobrenome='Vieira'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Vieira', nome='Willian'))
"""

# erro comum na utilização do return

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total

lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

tupla = (1, 2, 3, 4, 5, 6, 7)
print(soma_impares(tupla))