valor_dia = 30.00
dias_trabalhado = int(input('digite a quantidade de dias trabalhados: '))
pagamento = (dias_trabalhado * valor_dia) * 0.92
print(f'O valor do pagamento com desconto de 8% de imposto de renda é R$ {pagamento}')
