from math import sqrt

num = int(input('digite um numero: '))

if num > 0:
    raiz_quad = sqrt(num)
    print(f'A raiz quadrada do numero digitado é {raiz_quad:.2f}')

else:
    print('Esse é um numero invalido')
