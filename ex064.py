
# EXERCICIO 064 - TRATANDO VÁRIOS VALORES

n = 0
cont = 0
soma = 0
n = int(input('Digite um número: '))

while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um número: '))
    
print('Foram digitados {} números que somam {}'.format(cont, soma))