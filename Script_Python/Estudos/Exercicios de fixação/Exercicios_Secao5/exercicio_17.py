base_maior = float(input("Digite um valor para a base maior: "))
base_menor = float(input("Digite um valor para a base menor: "))
altura = float(input("Digite a altura: "))

if base_maior < 0:
    print("O valor da base maior deve ser um numero positivo")

elif base_menor < 0:
    print("O valor da base menor deve ser um numero positivo")

else:
    trapezio = ((base_maior + base_menor) * altura) / 2
    print(f'A area do trapezio é {trapezio:.2f}')
