altura = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo: ")

homem = (72.7 * altura) - 58
mulher = (62.1 * altura) - 44.7

if sexo == "masculino":
    print(f"Seu peso ideal é: {homem:.2f} quilos")

else:
    print(f"Seu peso ideal é: {mulher:.2f} quilos")
