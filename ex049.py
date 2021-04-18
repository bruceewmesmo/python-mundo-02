
# EXERCICIO 049 - TABUADA 2.0

n = int(input('Digite um número: '))
for cont in range(1,11):
    print('{:2} x {:2} = {:2}'.format(n,cont,cont*n))
