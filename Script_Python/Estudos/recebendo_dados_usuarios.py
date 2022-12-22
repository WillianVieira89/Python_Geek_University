"""
Recebendo dados do usuario

input() -> Todo dado recebido via input é do tipo String

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas triplas;

Exemplas:
-  Aspas simples -> 'Angelina Jolie'
- Aspas duplas -> "Angelina Jolie"
"""

# - Aspas triplas -> """Angelina Jolie"""

# Entrada de dados
# print('Qual seu nome?')
# nome = input() # Input -> Entrada

nome = input('Qual seu nome? ')

#exemplo de print 'mais atual' a partir do 3.7
print(f'Seja bem-vindo (a){nome}')

# print("Qual a sua idade")
# idade = input()

idade = input('Qual a sua idade? ')

#Processamento

#Saída
#Exemplo de print 'antigo' 2.x
#print('A %s tem %s anos' %(nome, idade))

#Exemplo de print 'antigo' 3.x
#print('A {0} tem {1} anos'.format(nome, idade))

#Exemplo de print 'antigo' 3.7
print(f'A {nome} tem {idade} anos')

"""
#int(idade) => cast
Cast é a 'conversão' de um tipo de dado para outro.
"""

print(f'A {nome} nasceu em {2022 - int(idade)}')