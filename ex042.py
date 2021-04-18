
# EXERCICIO 042 - ANALISANDO TRIANGULOS

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3 :
        print('Forma um triangulo equilátero')
    elif r1 != r2 != r3 != r1
        print('Forma um triangulo escaleno')
    else:
        print('Forma um triangulo isoseles')
else:
    print('Não é possível formar um triangulo com essas retas')

