
# EXERCICIO 062 - SUPER PROGRESSÃO ARITMETICA

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
mais = 10
total = 0

while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo),end = " ")
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))

print('Finalizando...')
print('Foram mostrados {} termos'.format(total))
