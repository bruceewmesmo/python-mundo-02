
# EXERCICIO 059 - CRIANDO UM MENU DE OPÇÕES

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0

while opcao != 5:
print('''[1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Números novos
    [5] Sair do Programa''')
    opcao = int(input('Qual a sua opção: '))
    if opcao == 1:
        print('A soma de {} e {} é {}'.format(n1,n2,n1+n2))
    elif opcao == 2:
        print('A multiplicação de {} e {} é {}'.format(n1,n2,n1*n2))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior número é o {}'.format(maior))
    elif opcao == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida!')
