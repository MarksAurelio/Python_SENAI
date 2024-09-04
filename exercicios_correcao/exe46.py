# 46. Desenvolva um programa que pergunte ao usuário para inserir 10 números 
# e, ao final, exiba a média dos números inseridos.

total = int()


for i in range (1, 11):
    numero = int(input(f'Informe o número {i}: '))
    total += numero

media = total / 10
print('a média é: ', media)
