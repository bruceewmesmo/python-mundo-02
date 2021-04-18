
# EXERCICIO 048 - SOMA IMPARES MULTIPLOS DE 3

soma = 0
cont = 0

for cont in range(1,501,2):
    if cont % 3 == 0:
        cont += 1
        soma += cont

print('A soma dos {} impares multiplos de 3 é {}'.format(cont,soma))
