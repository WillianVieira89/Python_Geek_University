"""
Funções com Parâmetros Padrão (Default Parameters)

- Funções onde a passagem de parâmetro seja opcional;

# Exemplo de função onde a passagem de parâmetro seja opcional
print('Geek University')

print()

# Exemplo de função onde a passagem de parâmetro seja obrigatória
def quadrado(numero):
    return numero ** 2

print(quadrado(3))
print(quadrado())  # TypeError

def exponencial(numero=5, potencia=2):
    return numero ** potencia

print(exponencial(2, 3))
print(exponencial(3, 2))

print(exponencial(3))  # Por Padrão eleve ao quadrado
print(exponencial(3, 5))   # Eleva a potência informada pelo usuário

# OBS:
# Se o usuario passar somente 1 argumento, este será atribuido ao parametro numero, e sera calculado o quadrado deste numero;
# Se o usuario passar 2 argumentos, o primeiro será atribuido ao parametro numero e o segundo ao argumento potência. Então
# será calculado a potência

print(exponencial())


# OBS: Em funções Python, os parâmetros com valores default (padrão) devem sempre estar ao final da declaração

# Erro!!!                              # Correto!!!!
def teste(num=2, potencia):            def teste(potencia, num=2):
    return num ** potencia                 return num ** potencia

print(teste(6))                        print(teste(6))

# Exemplo mais complexo

def mostra_info(nome='Geek', instrutor=False):
    if nome=='Geek' and instrutor:
        return 'Bem vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que o senhor era o instrutor'
    return f'Olá {nome}'

print(mostra_info())
print(mostra_info(instrutor=True))
print(mostra_info(instrutor=False))
print(mostra_info('Ozzy'))
print(mostra_info(nome='Stephany'))

# Por quê utilizar parâmetros com valor default?

- Nos permite ser mais flexíveis nas funções;
- Evita erros com parâmetros incorretos;
- Nos permite trabalhar com exemplos mais legíveis de código;

# Quais tipos de dados podemos utilizar como valores default para parâmetros?
- Qualquer tipo de dados:
    - Números, strings, floats, booleanos, listas, tuplas, dicionários, funções e etc;

# Exemplos

def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo - Evitar problemas e confusões...

# Variáveis globais
# Variáveis locais

instrutor = 'Geek'  # variável global

def diz_oi():
    instrutor = 'Python'  # variável local
    return f'Oi {instrutor}'

print(diz_oi())

# OBS: Se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferência

def diz_oi():
    prof = 'Geek'  # variável local
    return f'Olá {prof}'

print(diz_oi())
print(prof)  # NameError


# ATENÇÂO com variáveis globais (Se puder evitar, evite)

total = 0
def incrementa():
    total = total + 1  # UnboundLocalError ( a variável local está sendo utilizada para processamento sem ter sido inicializada)
    return total

print(incrementa())

# ATENÇÂO com variáveis globais (Se puder evitar, evite)

total = 0
def incrementa():
    global total  # Avisando que queremos utilizar a variável global

    total = total + 1
    return total

print(incrementa())
print(incrementa())
print(incrementa())
print(incrementa())

# Podemos ter funções declaradas dentro de funções, e também tem uma forma especial de escopo de variável

def fora():
    contador = 0
    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()

print(fora())
print(fora())
print(fora())
print(fora())

print(dentro())  # NameError
"""

