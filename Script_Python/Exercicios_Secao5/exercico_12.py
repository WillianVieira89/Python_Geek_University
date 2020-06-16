from math import log

numero = int(input("Digite um numero: "))

if numero < 0:
    print("Numero invalido")

if numero >= 0:
    logaritmo = log(numero, 2)
    print(f"O logaritmo do numero digitado é {logaritmo:.2f}")
