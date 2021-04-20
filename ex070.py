
# EXERCICIO 070 - ESTATISTICAS EM PRODUTOS

total = totmil = menor = cont = 0
barato = ' '

while True:
    produto = str(input('Digite o nome do produto: '))
    valor = float(input('Valor do produto: R$'))
    cont += 1
    total += valor
    if valor > 1000:
        totmil += 1
    if cont == 1 or valor < menor:
        menor = valor
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break

print('Fim da compra!')

print(f'O total da compra foi R${total:.2f}')
print(f'Tem {totmil} produtos acima de mil reais')
print(f'O produto mais barato foi {barato} por {menor}')