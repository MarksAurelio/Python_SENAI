# 34. Escreva um programa que peça ao usuário um número 
# e verifique se ele é positivo, negativo ou zero.

numero = float(input('Digite um número: \n'))

if numero > 0:
    print('Número positivo')
elif numero < 0:
    print('Número negativo')
else:
    print('Número igual a 0')
    