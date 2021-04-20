
# EXERCICIO 055 - MAIOR E MENOR DA SEQUENCIA

maior = 0
menor = 0

for p in range(1,6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p ==1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso foi de {} kg e o menor de {} kg'.format(maior,menor))