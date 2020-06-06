altura = float(input("Digite sua altura: ")
sexo = input("Digite seu sexo: ")

if sexo == masculino:
    homens = (72.7 * altura) - 58
    print("Seu peso ideal é: {homens}")

else:
    mulheres = (62.1 * altura) - 44.7
    print("Seu peso ideal é: {mulheres}")
