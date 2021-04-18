
# EXERCICIO 045 - PEDRA PAPEL TESOURA

from random import randint

itens  = ['Pedra','Papel','Tesoura']
computador = randint(0,2)

print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

jogador = int(input('Qual a sua opção: '))

print('''O computador jogou {}
E o jogador jogou {}'''.format(itens[computador],itens[jogador]))

if computador == 0:
    if jogador == 0:
        print('Empatou!')
    elif jogador == 1:
        print('Jogador venceu!')
    elif jogador == 2:
        print('Computador venceu!')
    else:
        print('Jogada Inválida!')
elif computador == 1:
    if jogador == 0:
        print('Computador venceu!')
    elif jogador == 1:
        print('Empatou!')
    elif jogador == 2:
        print('Jogador venceu!')
    else:
        print('Jogada Inválida!')
elif computador == 2:
    if jogador == 0:
        print('Jogador venceu!')
    elif jogador == 1:
        print('Computador venceu!')
    elif jogador == 2:
        print('Empatou!')
    else:
        print('Jogada Inválida!')
