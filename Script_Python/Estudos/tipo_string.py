"""
Tipo string

Em Python, um dado é considerado do tipo string  sempre que:

- Estiver entre aspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre aspas duplas -> "uma string", "234", "a", "True", "42.3"
- Estiver entre aspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''
"""
# Estiver entre aspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""

nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina\nJolie'  # \n pula uma linha
print(nome)
print(type(nome))

nome = 'Geek University'
print(nome.upper())  # upper transforma todos os caracteres para caixa alta  --> GEEK UNIVERSITY

nome = 'Geek University'
print(nome.lower())  # lower transforma todos os caracteres para caixa baixa --> geek university

nome = 'Geek University'
print(nome.split())  # split transforma em uma lista de string ->> ['Geek', 'University']

# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,   12,  13,  14 ]
# ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's',  'i', 't', 'y']

nome = 'Geek University'
print(nome[0:4])  # Slice de string
print(nome[5:15])  # Slice de string
# [ 0,      1]
# ['Geek, University]
print(nome.split()[0])
print(nome.split()[1])
print(nome[::-1])  # Comece do primeiro elemento, vá até o ultimo elemento e inverta, inversão de string
print(nome.replace('e', 'i'))  # Substituição de letras

texto = 'socorram me subino onibus em marrocos'
print(texto)
print(texto[::-1])
