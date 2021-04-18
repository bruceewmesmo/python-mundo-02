
# EXERCICIO 043 - IMC

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso/(altura**2)

if imc <= 18.5:
    print('Seu IMC é {:.1f} e está abaixo do peso'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é {:.1f} e está com o peso ideal'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é {:.1f} e está com sobrepeso'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é {:.1f} e está com obesidade'.format(imc))
elif imc >= 40:
    print('Seu IMC é {:.1f} e está com obesidade mórbida'.format(imc))
