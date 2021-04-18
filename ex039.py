
# EXERCICIO 039 - ALISTAMENTO MILITAR

from datetime import date

atual = date.today().year
nascimento = int(input('Qual ano você nasceu? '))
idade = atual - nascimento

print('Quem nasceu em {} no ano de {} vai ter {} anos'.format(nascimento,atual,idade))
if idade == 18:
    print('Você tem que se alistar!')
elif idade < 18:
    saldo = 18 - idade
    print('Você irá se alistar em {} anos'.format(saldo))
    print('Seu alistamento será em {}'.format(atual+saldo))
elif idade > 18:
    saldo = idade - 18
    print('Você deveria ter se alistado a {} anos'.format(saldo))
    print('Seu alistamento foi e {}'.format(atual-saldo))
