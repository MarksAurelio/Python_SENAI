# 29. Crie um algoritmo que pergunte ao usuário um número 
# e verifique se ele é múltiplo de 3.

numero = int(input('Digite um número: \n'))

if numero % 3 == 0:
    print('Esse número é múltiplo de 3')
else:
    print('Esse número não é múltiplo de 3')
    