
# EXERCICIO 067 - TABUADA 3.0

while True:
    n = int(input('Quer a tabuada de qual valor? '))
    if n < 0:
        break
    for cont in range(1,11):
        print('{:2} x {:2} = {:2}'.format(n,cont,cont*n))

print('Tabuada encerrada!')
