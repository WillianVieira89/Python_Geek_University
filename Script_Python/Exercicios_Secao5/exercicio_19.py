numero = int(input("Digite um numero: "))

if numero % 3 == 0:
    print(f"{numero} é divisivel por 3")

else:
    print(f"{numero} não é divisivel por 3")

if numero % 5 == 0:
    print(f"{numero} é divisivel por 5")

else:
    print(f"{numero} não é divisivel por 5")

if numero % 3 and numero % 5:
    pass
