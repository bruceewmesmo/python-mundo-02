
# EXERCICIO 061 = PROGRESSAO ARITMÉTICA

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1

while cont <= 10:
    print('{} -> '.format(termo),end = " ")
    termo += razao
    cont += 1
print('Acabou!')
