
# EXERCICIO 066 - VARIOS NUMEROS COM FLAG

n = soma = total = 0

while n != 999:
    n = int(input('Digite um valor ou 999 para parar: '))
    if n == 999:
        break
    total += 1
    soma += n

print(f'Foram digitados {total} valores e a soma dos valores foi {soma}')
