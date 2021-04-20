
# EXERCICIO 058 - JOGO DE ADIVINHAÇÃO

from random import randint

computador = randint(0,10)
print('Acabei de pensar num número entre 0 e 10')
palpite = 0
acertou = False

while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...')
        elif jogador > computador:
            print('Menos...')

print('Acertou em {} tentativas!'.format(palpite))
