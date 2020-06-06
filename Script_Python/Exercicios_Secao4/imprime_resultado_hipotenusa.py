from math import sqrt
cat_a = float(input('digite o valor do cateto A: '))
cat_b = float(input('digite o valor do cateto B: '))
hipot = sqrt((cat_a ** 2) + (cat_b ** 2))
print(f'A hipotenusa dos valores digitados nos catetos é {hipot}')
