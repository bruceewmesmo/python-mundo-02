
# EXERCICIO 069 - ANALISE DE DADOS DO GRUPO

tot18 = 0
totalhomem = 0
totalmulher20 = 0

while True:
    idade =  int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]:' )).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totalhomem += 1
    if sexo == 'F' and idade < 20:
        totalmulher20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Total de maiores de 18 anos: {tot18}')
print(f'Total de homens: {totalhomem}')
print(f'Total de mulheres abaixo de 20 anos: {totalmulher20}')
