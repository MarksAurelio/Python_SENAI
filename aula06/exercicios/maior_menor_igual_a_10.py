# 21. Escreva um algoritmo que peça ao usuário para digitar um número e verifique se ele é maior, menor ou igual a 10.

numero1 = int(input('Digite um número: \n'))

if numero1 > 10:
    print('Esse número é maior que 10')
elif numero1 < 10:
    print('Esse número é menor que 10')
elif numero1 == 10:
    print('Esse número é igual a 10')
