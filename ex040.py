
# EXERCICIO 040 - AQUELE CLÁSSICO DA MÉDIA

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2

print('Com as nota {:.1f} e {:.1f} a média é {:.1f}'.format(n1,n2,media))

if 7> media >= 5:
    print('Recuperação!')
elif media < 5:
    print('Reprovação!')
elif media > 7:
    print('Aprovação!')
