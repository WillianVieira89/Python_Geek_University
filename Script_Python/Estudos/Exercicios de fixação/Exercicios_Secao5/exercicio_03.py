from math import sqrt
from math import pow

numero = int(input("Digite um numero: "))

if numero >= 0:
    raiz_quad = sqrt(numero)
    exponencial = pow(numero, 4)
    print(f"A Raiz Quadrada do numero digitado é {raiz_quad:.0f}, e quadrado do numero é {exponencial:.0f}")

else:
    ("Não é um numero válido")
