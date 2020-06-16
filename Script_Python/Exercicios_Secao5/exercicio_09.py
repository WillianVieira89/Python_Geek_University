salario  = float(input("Digite seu salario: "))
emprestimo = float(input("Digite o valor do emprestimo: "))
prestacoes = int(input("Digite a quantidade de prestações: "))

valor_prestacao = emprestimo / prestacoes
percentual = salario * 0.2


if valor_prestacao > percentual:
    print("não concedido")

else:
    print("concedido")


