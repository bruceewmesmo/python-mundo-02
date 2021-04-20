
# EXERCICIOS 056 - ANALISADOR COMPLETO

somaidade = 0
maioridadehomem = 0
mediaidade = 0
totmulher20 = 0
nomemaisvelho = ''

for p in range(1,5):
    print('----- {}ª pessoa -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem  = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem  = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
    
mediaidade = somaidade/4

print('A média de idade do grupo é {}'.format(mediaidade))
print('O homem mais velho é o {} e tem {} anos'.format(nomemaisvelho,maioridadehomem))
print('Existem {} mulheres abaixo de 20 anos'.format(totmulher20))
