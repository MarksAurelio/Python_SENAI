# 41. Crie um programa que peça ao usuário um número inteiro positivo 
# e exiba todos os números de 1 até o número informado.

numero = int(input('Digite um número inteiro e positivo: \n'))

if numero > 0:
    for numero in range(1, numero + 1): 
        print(numero)
elif numero < 0:
    print('Esse número não é positivo')
