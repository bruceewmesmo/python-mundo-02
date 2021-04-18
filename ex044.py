
# EXERCICIO 044 - GERENCIADOR DE PAGAMENTOS

preço = float(input('Preço total das compras: R$'))

print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual opção? '))

if opcao == 1:
    total = preço * 0.9
elif opcao == 2:
    total = preço * 0.95
elif opcao == 3:
    total = preço
    parcela = total/2
elif opcao == 4:
    total = preco * 1.20
    nparcelas = int(input('Quantas parcelas? '))
    parcela = total/nparcelas
else:
    print('Opção inválida!')

print('Sua compra de R${} vai custar R${} no final'.format(preço,total))
