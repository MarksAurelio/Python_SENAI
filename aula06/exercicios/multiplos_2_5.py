# 37. Desenvolva um algoritmo que peça ao usuário para digitar um número 
# e verifique se ele é múltiplo de 2 ou de 5.

numero1 = int(input('Digite um número: \n'))

if numero1 % 2 == 0 or numero1 % 5 == 0:
    print("O número é múltiplo de 2 ou de 5.")
else:
    print("O número não é múltiplo de 2 nem de 5.")
