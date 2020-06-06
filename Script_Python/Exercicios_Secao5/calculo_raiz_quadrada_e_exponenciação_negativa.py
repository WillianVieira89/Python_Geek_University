from math import sqrt

num1 = float(input('digite um numero: '))

if num1 > 0:
    raiz_quad = sqrt(num1)
    print(f'A raiz quadrada do numero digitado é {raiz_quad:.2f}')

else:
    print(f'O quadrado do numero digitado é {num1 ** 2:.2f}')
