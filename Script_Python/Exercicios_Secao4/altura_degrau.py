degrau = float(input('digite a altura do seu degrau em cm: '))
altura = float(input('digite a altura que deseja alcançar em mts: ')) * 100
quantidade_degraus = altura // degrau
print(f'A quantidade de degraus necessarios para atingir'
      f'a altura desejada é {quantidade_degraus:.0f}')
