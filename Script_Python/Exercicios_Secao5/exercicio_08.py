nota1 = float(input('digite sua nota: '))
nota2 = float(input('digite sua nota: '))

if nota1 < 0 or nota1 > 10:
    print(f'O valor {nota1:.2f} é um Valor invalido')

if nota2 < 0 or nota2 > 10:
    print(f'O valor {nota2:.2f} é um Valor invalido')

else:
    media_nota = (nota1 + nota2) / 2
    print(f"A média das notas é {media_nota:.2f}")
