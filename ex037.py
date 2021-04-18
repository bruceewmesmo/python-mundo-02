
#   EXERCICIO 037 - CONVERSOR DE BASES NUMERICAS

n = int(input('Digite um número inteiro: '))
print('''Escolha uma base de conversão:
[1] Binário
[2] Octal
[3] Hexadecimal''')
opcao = int(input('Sua oção: '))

if opcao == 1:
    print('{} convertido para Binário é igual a {}'.format(n, bin(n)[2:]))
elif opcao == 2:
    print('{} convertido para Octal é igual a {}'.format(n, oct(n)[2:]))
elif opcao == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Opção invalida!')
