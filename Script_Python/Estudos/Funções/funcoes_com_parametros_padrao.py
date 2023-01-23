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

"""

# Exemplo mais complexo

def mostra_info(nome='Geek', instrutor=False):
    if nome=='Geek' and instrutor:
        return 'Bem vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'

print(mostra_info())
print(mostra_info(instrutor=True))
print(mostra_info(instrutor=False))
print(mostra_info('Ozzy'))
print(mostra_info(nome='Stephany'))
