
# EXERCICIO 36 - APROVANDO EMPRÉSTIMO

casa = float(input('Qual o valor do imóvel? R$'))
salario = float(input('Qual o salário do comprador? R$'))
anos = int(input('Em quantos se pretende pagar? '))
minimo = salario * 0.3
prestaçao = casa/(anos * 12)
print('O valor da prestação será de R${:.2f}'.format(prestaçao))
if prestaçao <= minimo:
    print('Empréstimo concedido!')
else:
    print('Emprestimo negado!')