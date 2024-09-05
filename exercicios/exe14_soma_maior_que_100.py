# 14. Desenvolva um algoritmo que peça ao usuário para digitar dois números 
# e verifique se a soma deles é maior que 100.

numero1 = int(input('Digite o primeiro número: \n'))
numero2 = int(input('Digite o segundo número: \n'))

soma = numero1 + numero2

if soma > 100:
    print('A soma é maior que 100')
