
# EXERCICIO 054 - GRUPO DA MAIORIDADE

from datetime import date

atual = date.today().year
maior = 0
menor = 0

for cont in range(1,8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(cont)))
    idade = atual - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1

print('Das sete pessoas, {} são maiores de idade e {} são menores de idade'.format(maior,menor))
