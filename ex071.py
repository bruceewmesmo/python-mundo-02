
# EXERCICIO 071 - SIMULADOR DE CAIXA ELETRONICO

valor = int(input('Qual valor vc quer sacar? '))
total = valor
cedula = 50
totalcedulas = 0
while True:
    if total >= cedula:
        total -= cedula
        totalcedulas += 1
    else:
        if totalcedulas > 0:
            print(f'Total de {totalcedulas} cédula de {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula =10
        elif cedula == 10:
            cedula = 1
        totalcedulas = 0
        if total == 0:
            break

print('Volte sempre!')
