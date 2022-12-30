largura = int(input('digite a largura do terreno: '))
comprim = int(input('digite o comprimento do terreno: '))
tela = float(input('digite o valor da tela: '))
custo = (largura * comprim) * tela
print(f'O valor para cercar o terreno com a tela é de {custo:.2f} reais')
