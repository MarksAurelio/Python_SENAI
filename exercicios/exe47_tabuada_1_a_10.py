# 47. Crie um programa que peça ao usuário um número e exiba a tabuada desse número de 1 a 10.

numero = int(input('Informe um número: \n'))

for i in range(10):
    print(f'{numero} x {i + 1} =', numero * (i+1))
