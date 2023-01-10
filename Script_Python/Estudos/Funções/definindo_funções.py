"""
Definindo Funções

— Funções são pequenos partes de códigos que realizam tarefas específicas:
— Pode ou não receber entradas de dados e retornar uma saída de dados:
— Muito utéis para executar procedimentos similares por repetidas vezes

OBS: Se você escrever uma função que realiza várias tarefas dentro dela:
é bom fazer uma verificação para que a função seja simplificada.

Já utilizamos varías funções desde que iniciamos este curso:
- print()
- len()
- max()
- min()
- count()
_ e muitas outras;
"""

# Exemplo de utilização de funções:

cores = ['verde', 'amarelo', 'branco']

# Utilizando a função integrada (Built-in) do Python print()
#  print(cores)

curso = 'Programação em Python: Essencial'
#  print(curso)

cores.append('roxo')
#  print(cores)

cores.clear()
#  print(cores)

# print(help(print))
# DRY - Don't Repeat Yourself - Não repita você mesmo / Não repita seu código

"""
Em Python, a forma geral de definir uma função é:

def nome_da_função(parâmetros_de_entrada):
    bloco_da_função
    
Onde:
nome_da_função -> SEMPRE com letras minisculas, e se for nome composto, separado por underline (Snake Case):
parâmetros_da_função -> Opcionais, onde tendo mais de um , cada um separado por virgula, podendo ser opcionais ou não;
bloco_da_função -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece.
Neste bloco, pode ter ou não retorno da função

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao Python que
estamos definindo uma função. Também abrimos o bloco de código com o já conhecido dois pontos : que é
utilizado em Python para definir blocos.  
"""


# Definindo a primeira função

def diz_oi():
    print('Oi')

"""
OBS: 
1 - Veja que, dentro das nossas funções podemos utilizar outras funções
2 - Veja que nossa função so executa 1 tarefa, ou seja, a única coisa que ela faz é dizer oi
3 - Veja que está função não recebe nenhum parâmetro de entrada:
4 - Veja que está função não retorna nada
"""

# Utilizando funções

# Chamada de execução
diz_oi()

"""
ATENÇÃO:

Nunca esqueçã de utilizar o parênteses ao executra uma função

Exemplos:

# Errado
diz_oi

# Certo
diz_oi()

# Errado 
diz_oi ()
"""

# Exemplo 2

def cantar_parabens():
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o Aniversariante')

cantar_parabens()

# Em Python podemos inclusive criar variaveis do tipo de uma função e executar esta função atraves da variavel

canta = cantar_parabens
canta()