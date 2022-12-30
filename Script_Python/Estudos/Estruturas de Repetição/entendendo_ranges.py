"""
Ranges

- Precisamos conhecer o loop for para usarmos os ranges
- Precisamos conhecer o range para trabalhar melhor com o loop for

Ranges são utilizado para gerar sequências numéricas, não de forma aleatória, mas sim
de maneira especificada.

Formas gerais:

# Forma 1

range(valor_de_parada)

OBS: valor_de_parada não inclusive (inicio padrão 0, e passo de 1 em 1)

# Forma 2

range(valor_de_inicio, valor_de_parada)

OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo a passo de 1 em 1)

# Forma 3

range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo especificado pelo usuário)

# Forma 4 (Inversa)

range(valo_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo especificado pelo usuário)

"""

# Forma 1
for num in range(11):
    print(num)

# Forma 2
for num in range(1, 11):
    print(num)

# Forma 3

for num in range(0, 110, 10):
    print(num)

# Forma 4 (regressão numérica)

for num in range(10, -1, -1):
    print(num)